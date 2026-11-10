"""Check this repository's distributable, reader paths, and copy-only install routes."""
import hashlib
import json
from pathlib import Path
import re
import struct
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/repo-cleaner'


def prose(text):
    return re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)


def anchor(text):
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        self.targets.extend(v for k, v in attrs if k in ('href', 'src') and v)


class Integrity(unittest.TestCase):
    def test_installable_package(self):
        text = (SKILL / 'SKILL.md').read_text()
        header = text.split('---', 2)[1]
        self.assertIn('name: repo-cleaner', header)
        self.assertIn('description:', header)
        self.assertLess(len(text.splitlines()), 500)
        for rel in ('agents/openai.yaml', 'assets/repo-brief.md',
                    'references/audit-and-validation.md',
                    'references/readme-and-visuals.md',
                    'references/github-discovery.md'):
            self.assertTrue((SKILL / rel).is_file(), rel)
        self.assertIn('$repo-cleaner', (SKILL / 'agents/openai.yaml').read_text())
        self.assertFalse((SKILL / 'README.md').exists())

    def test_local_document_links(self):
        for path in ROOT.rglob('*.md'):
            text = prose(path.read_text())
            parser = Links()
            parser.feed(text)
            targets = parser.targets + re.findall(r'\]\(([^\s)]+)\)', text)
            for target in targets:
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    continue
                destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
                with self.subTest(source=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue(destination.is_relative_to(ROOT), 'Link leaves repository')
                    self.assertTrue(destination.exists(), 'Missing local target')
                    if parsed.fragment and destination.suffix == '.md':
                        headings = re.findall(r'^#{1,6}\s+(.+)$', prose(destination.read_text()), re.M)
                        self.assertIn(parsed.fragment, [anchor(h) for h in headings])

    def test_documented_install_commands(self):
        guide = (ROOT / 'docs/installation.md').read_text()
        commands = [s for s in re.findall(r'```sh\n(.*?)```', guide, re.S)
                    if s.startswith('test ! -e')]
        self.assertEqual(len(commands), 2)
        expected = {str(p.relative_to(SKILL)): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in SKILL.rglob('*') if p.is_file()}
        for command in commands:
            with tempfile.TemporaryDirectory() as temp:
                import os
                env = dict(os.environ, HOME=temp)
                first = subprocess.run(['bash', '-c', command], cwd=ROOT, env=env,
                                       capture_output=True, text=True)
                self.assertEqual(first.returncode, 0, first.stderr)
                host = '.claude' if '.claude' in command else '.agents'
                installed = Path(temp) / host / 'skills/repo-cleaner'
                actual = {str(p.relative_to(installed)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in installed.rglob('*') if p.is_file()}
                self.assertEqual(expected, actual)
                second = subprocess.run(['bash', '-c', command], cwd=ROOT, env=env,
                                        capture_output=True)
                self.assertNotEqual(second.returncode, 0, 'Existing installation was overwritten')

    def test_topics_and_private_review(self):
        data = json.loads((ROOT / 'docs/repository-metadata.json').read_text())
        self.assertEqual(data['visibility'], 'private')
        self.assertLessEqual(len(data['topics']), 20)
        self.assertEqual(len(data['topics']), len(set(data['topics'])))
        for topic in data['topics']:
            self.assertRegex(topic, r'^[a-z0-9-]{1,50}$')
        self.assertEqual(data['application_status'], 'prepared')

    def test_social_image_spec(self):
        data = (ROOT / 'docs/assets/social-preview.png').read_bytes()
        self.assertEqual(data[:8], b'\x89PNG\r\n\x1a\n')
        self.assertEqual(struct.unpack('>II', data[16:24]), (1280, 640))
        self.assertLess(len(data), 1_000_000)

    def test_badges_are_local_static_labels(self):
        for path in (ROOT / 'docs/assets').glob('badge-*.svg'):
            svg = ET.fromstring(path.read_text())
            self.assertIsNotNone(svg.find('{http://www.w3.org/2000/svg}title'))
            self.assertNotIn('<script', path.read_text())
            self.assertNotIn('100%', path.read_text())


if __name__ == '__main__':
    unittest.main()

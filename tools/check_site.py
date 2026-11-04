from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import sys
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')
root = Path(__file__).resolve().parent.parent / 'dist'


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.title = ''
        self.inside_title = False
        self.in_json = False
        self.json_text = ''
        self.schemas = []
        self.visible = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == 'title': self.inside_title = True
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.in_json = True
            self.json_text = ''

    def handle_data(self, data):
        if self.inside_title: self.title += data
        if self.in_json: self.json_text += data
        else: self.visible.append(data)

    def handle_endtag(self, tag):
        if tag == 'title': self.inside_title = False
        if tag == 'script' and self.in_json:
            self.schemas.append(json.loads(self.json_text))
            self.in_json = False


titles = set()
descriptions = set()
counts = {}
for file in root.glob('*.html'):
    source = file.read_text(encoding='utf-8')
    doc = Document()
    doc.feed(source)
    assert sum(tag == 'h1' for tag, _ in doc.tags) == 1, file
    assert sum(tag == 'main' for tag, _ in doc.tags) == 1, file
    assert any(tag == 'html' and attrs.get('lang') == 'da' for tag, attrs in doc.tags), file
    assert doc.title and doc.title not in titles, file
    titles.add(doc.title)
    meta = {attrs.get('name'): attrs.get('content') for tag, attrs in doc.tags if tag == 'meta'}
    assert meta.get('description') and meta['description'] not in descriptions, file
    descriptions.add(meta['description'])
    ids = [attrs['id'] for tag, attrs in doc.tags if 'id' in attrs]
    assert len(ids) == len(set(ids)), file
    for tag, attrs in doc.tags:
        for key in ('href', 'src'):
            target = attrs.get(key)
            if not target: continue
            url = urlsplit(target)
            if url.scheme or url.netloc: continue
            if not url.path:
                assert not url.fragment or url.fragment in ids, (file, target)
            else:
                local = file.parent / unquote(url.path)
                assert local.is_file(), (file, target)
    assert doc.schemas, file
    for schema in doc.schemas:
        for entity in schema['@graph']:
            assert entity['@type'] != 'Event', 'Event facts are incomplete.'
            if entity['@type'] == 'FAQPage':
                visible = ''.join(doc.visible)
                for question in entity['mainEntity']:
                    assert question['name'] in visible
                    assert question['acceptedAnswer']['text'] in visible
    assert 'codex-preview' not in source and '[TODO:' not in source
    counts[file.name] = len(source)

assert len(counts) == 6
for file in (root/'assets').glob('*.svg'): ET.parse(file)
sitemap = ET.parse(root/'sitemap.xml')
assert len(sitemap.getroot()) == 6
css = (root/'styles.css').read_text(encoding='utf-8')
assert '--bg:#000000' in css and 'repeating-linear-gradient' not in css
assert (root/'assets/creepster.ttf').stat().st_size > 1000
assert (root/'assets/social-card.png').stat().st_size > 1000
print(json.dumps({'pages':list(counts),'unique_titles':len(titles),'unique_descriptions':len(descriptions),
                  'local_links_and_assets':'OK','json_ld_and_faq':'OK','svg_and_sitemap':'OK',
                  'black_background':'OK'}, ensure_ascii=False))

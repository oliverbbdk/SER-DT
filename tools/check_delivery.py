from pathlib import Path
import json
import re

base=Path(__file__).resolve().parent.parent
text=(base/'SE-RODT-aabn-i-browser.html').read_text(encoding='utf-8')
pages=json.loads(re.search(r'<script type="application/json" id="page-data">(.*?)</script>',text,re.S).group(1))
assert len(pages)==6
assert len({page['title'] for page in pages.values()})==6
for route,page in pages.items():
    assert page['schema']['@context']=='https://schema.org'
    assert page['canonical'].startswith('https://')
    assert '<iframe' not in page['html']
    assert not re.search(r'(?:src|href)="assets/',page['html'])
assert 'data-standalone="true"' in text
assert '<script type="application/ld+json" id="site-schema">' in text
assert sum(p['html'].count('class="trailer-preview"') for p in pages.values())==3
assert 'history.replaceState' not in text
for required in ('README.md','dist/styles.css','dist/app.js','docs/SEO-GEO-kontrol.html',
                 'data/FESTIVALDATA.json','data/FILMKILDER.json','data/site.json',
                 'dist/assets/FONT-LICENSE.txt','dist/assets/BEBAS-LICENSE.txt'):
    assert (base/required).is_file(),required
print('OK: six standalone routes, metadata, schema, inline local assets, trailer links and project files.')

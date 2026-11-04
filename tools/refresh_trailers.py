from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
import json
import urllib.parse
import urllib.request

path = Path(__file__).resolve().parent.parent/'data/FILMKILDER.json'
films = json.loads(path.read_text(encoding='utf-8'))

def refresh(film):
    url = 'https://www.youtube.com/oembed?' + urllib.parse.urlencode({'url':film['url'],'format':'json'})
    with urllib.request.urlopen(url, timeout=20) as response:
        metadata = json.load(response)
    assert metadata['author_name'] == film['publisher'], film['key']
    film['thumbnail_url'] = metadata['thumbnail_url']
    film['checked'] = date.today().isoformat()
    return film

updated = list(ThreadPoolExecutor(max_workers=4).map(refresh, films))
path.write_text(json.dumps(updated,ensure_ascii=False,indent=2)+'\n', encoding='utf-8')
print('Rechecked all nine official sources; thumbnail URLs saved, no media downloaded.')

"""Transfer only byte-verified native installer assets on a GitHub runner."""
import hashlib,json,os,subprocess,time,urllib.request
from pathlib import Path
from urllib.parse import urlparse

repo='Ding-spec/organoid-cartography-database-agent'
assert os.environ['GITHUB_REPOSITORY']==repo
api='https://api.github.com/repos/'+repo
config=json.loads(os.environ['OCD_MAC_INSTALLER_DOWNLOADS'])
assert config['tag']=='macos-2026.10.07'
assert config['snapshot_id']=='4e3155030071836f19f2b7a3c9343f2b93838a30d5598315ec9634b1c447fb45'
allowed={'Organoid-Cartography-Database-Agent-macOS-x86_64.dmg',
 'Organoid-Cartography-Database-Agent-macOS-x86_64.002.dmgpart',
 'SHA256SUMS-macOS-x86_64.txt','INSTALL-macOS-x86_64.txt',
 'verification-macOS-x86_64.json','download-verified-macOS-x86_64.json'}
assert {a['name'] for a in config['assets']}==allowed

def request(path,method='GET'):
    req=urllib.request.Request(api+path,method=method,headers={
      'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json'})
    with urllib.request.urlopen(req,timeout=120) as r:
        return None if r.status==204 else json.load(r)

release=request('/releases/tags/'+config['tag'])
assert release['prerelease'] and not release['draft']
assert config['snapshot_id'] in release['body']
root=Path(os.environ['RUNNER_TEMP'])/'ocd-installer-transfer'
root.mkdir(exist_ok=True)
for asset in config['assets']:
    assert 0<asset['size']<2**31
    url=asset['url']
    assert urlparse(url).scheme=='https'
    assert urlparse(url).hostname in ('release-assets.githubusercontent.com','objects.githubusercontent.com')
    print('::add-mask::'+url,flush=True)
    for attempt in range(5):
        try:
            current=request('/releases/'+str(release['id'])+'/assets')
            old=next((a for a in current if a['name']==asset['name']),None)
            if old and old.get('digest')==asset['digest']:
                print('Public asset already verified:',asset['name'],flush=True)
                break
            path=root/asset['name']
            h=hashlib.sha256()
            with urllib.request.urlopen(url,timeout=120) as response,path.open('wb') as output:
                while True:
                    block=response.read(8*1024*1024)
                    if not block:break
                    output.write(block);h.update(block)
            assert path.stat().st_size==asset['size']
            assert 'sha256:'+h.hexdigest()==asset['digest']
            if old:request('/releases/assets/'+str(old['id']),'DELETE')
            subprocess.run(['gh','release','upload',config['tag'],str(path),'--repo',repo],check=True)
            current=request('/releases/'+str(release['id'])+'/assets')
            uploaded=next(a for a in current if a['name']==asset['name'])
            assert uploaded['digest']==asset['digest']
            path.unlink()
            print('Native installer asset uploaded and SHA-256 verified:',asset['name'],flush=True)
            break
        except Exception as error:
            print('Transfer retry:',asset['name'],type(error).__name__,flush=True)
            if attempt==4:raise RuntimeError('Native installer transfer failed: '+asset['name']) from None
            time.sleep(10)
print('Verified Intel Mac installer files are available in the public prerelease.',flush=True)

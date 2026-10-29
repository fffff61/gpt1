from pathlib import Path
from playwright.sync_api import sync_playwright
import json,os
root=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
 launch={'headless':True,'args':['--disable-dev-shm-usage','--use-angle=swiftshader','--enable-unsafe-swiftshader']}
 if os.name=='nt': launch['channel']='msedge'
 else:launch['executable_path']='/usr/bin/chromium';launch['args'].append('--no-sandbox')
 browser=p.chromium.launch(**launch)
 context=browser.new_context(viewport={'width':1280,'height':720})
 page=context.new_page();errors=[];requests=[]
 page.on('pageerror',lambda error:errors.append(str(error)))
 page.on('request',lambda request:requests.append(request.url))
 page.on('console',lambda msg:print('CONSOLE',msg.type,msg.text[:300],flush=True) if msg.type in ['error','warning'] else None)
 page.goto((root/'downloads/RealmGuard-Standalone.html').as_uri(),wait_until='domcontentloaded')
 page.locator('#loading').wait_for(state='hidden',timeout=90000)
 page.screenshot(path=str(root/'downloads/standalone-title.png'))
 page.mouse.click(210,452);page.wait_for_timeout(1000)
 page.mouse.click(1180,322);page.wait_for_timeout(500)
 page.mouse.click(374,488);page.wait_for_timeout(500)
 page.mouse.click(1016,154);page.wait_for_timeout(500)
 page.mouse.click(1105,31);page.wait_for_timeout(1500)
 context.set_offline(True)
 page.reload(wait_until='domcontentloaded')
 page.locator('#loading').wait_for(state='hidden',timeout=90000)
 page.mouse.click(210,530);page.wait_for_timeout(800)
 page.mouse.click(1180,322);page.wait_for_timeout(500)
 page.screenshot(path=str(root/'downloads/standalone-resumed.png'))
 external=[url for url in requests if url.startswith(('http:','https:'))]
 assert not external and not errors,(external,errors)
 print('STANDALONE_FILE_BOOT_SAVE_OFFLINE_RELOAD_CONTINUE_OK',flush=True)
 print('EXTERNAL_NETWORK_REQUESTS=0',flush=True)
 browser.close()

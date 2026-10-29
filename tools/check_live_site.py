import os
from pathlib import Path
from playwright.sync_api import sync_playwright
url=os.environ['GAME_URL']
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome',headless=True,args=['--disable-dev-shm-usage','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
 context=browser.new_context(viewport={'width':1280,'height':720})
 page=context.new_page();errors=[];responses=[]
 page.on('pageerror',lambda error:errors.append(str(error)))
 page.on('response',lambda response:responses.append((response.url,response.status)))
 response=page.goto(url,wait_until='domcontentloaded',timeout=60000)
 assert response.status==200,response.status
 assert page.title()=='神域守卫 · 像素防线',page.title()
 page.locator('#loading').wait_for(state='hidden',timeout=120000)
 Path('live-check').mkdir(exist_ok=True)
 page.screenshot(path='live-check/title.png')
 page.mouse.click(210,452)
 page.wait_for_timeout(1000)
 page.screenshot(path='live-check/gameplay.png')
 assert not errors,errors
 for suffix in ['index.wasm.gz','index.pck']:
  assert any(asset.endswith(suffix) and status==200 for asset,status in responses),(suffix,responses)
 print('LIVE_SITE_HTTP_200_ENGINE_BOOT_AND_START_OK',url,flush=True)
 print('BROWSER_PAGE_ERRORS=0',flush=True)
 browser.close()

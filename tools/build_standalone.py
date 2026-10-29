from pathlib import Path
import json,base64,re,zipfile
root=Path(__file__).resolve().parents[1];dist=root/'dist';out=root/'downloads'
assets={name:base64.b64encode((dist/name).read_bytes()).decode() for name in ['index.wasm.gz','index.pck','index.audio.worklet.js','index.audio.position.worklet.js']}
bootstrap='''const embeddedAssets=__ASSETS__;
function embeddedResponse(path){
 const name=path.split('/').pop();
 const binary=atob(embeddedAssets[name]);
 const bytes=new Uint8Array(binary.length);
 for(let i=0;i<binary.length;i++) bytes[i]=binary.charCodeAt(i);
 return Promise.resolve(new Response(bytes,{headers:{'Content-Type':name.endsWith('.js')?'text/javascript':'application/octet-stream'}}));
}
const embeddedWorklets={};
for(const name of ['index.audio.worklet.js','index.audio.position.worklet.js']){
 embeddedWorklets[name]='data:text/javascript;base64,'+embeddedAssets[name];
}
'''.replace('__ASSETS__',json.dumps(assets,separators=(',',':')))
js=(dist/'index.js').read_text().replace("? fetch(file + '.gz').then(response", "? embeddedResponse(file + '.gz').then(response").replace(': fetch(file);',': embeddedResponse(file);')
js=re.sub(r'function _godot_js_pwa_cb\(p_update_cb\)\{.*?\}function _godot_js_pwa_update','function _godot_js_pwa_cb(p_update_cb){}function _godot_js_pwa_update',js,count=1)
js=js.replace('return `${loadPath}.audio.worklet.js`;','return embeddedWorklets["index.audio.worklet.js"];').replace('return `${loadPath}.audio.position.worklet.js`;','return embeddedWorklets["index.audio.position.worklet.js"];')
html=(dist/'index.html').read_text()
html=re.sub(r'<link[^>]+rel="manifest"[^>]*>','',html)
for name in ['index.icon.png','index.apple-touch-icon.png','index.144x144.png']:
 uri='data:image/png;base64,'+base64.b64encode((dist/name).read_bytes()).decode();html=html.replace(name,uri)
html=html.replace('<script src="index.js"></script>','<script>'+bootstrap+'\n'+js+'</script>')
html=html.replace('"serviceWorker": "index.service.worker.js"','"serviceWorker": ""')
html=html.replace('首次加载约 19 MB；资源缓存完成后可离线游玩。','独立离线版，全部游戏资源已包含在此文件中。')
start=html.index('    navigator.serviceWorker.ready.then(');end=html.index('\n    });',start)+len('\n    });')
html=html[:start]+html[end:]
# A local file has no server URL; all game asset downloads resolve from the embedded payload.
out.mkdir(exist_ok=True)
(out/'RealmGuard-Standalone.html').write_text(html)
with zipfile.ZipFile(out/'RealmGuard-Standalone.zip','w',zipfile.ZIP_DEFLATED) as z:
 z.writestr('使用说明.txt','解压后，使用新版 Microsoft Edge 或 Chrome 打开 RealmGuard-Standalone.html。无需安装程序、无需启动服务器、无需访问外部域名。电脑 WASD 移动，1/2/3 技能；手机横屏使用摇杆。存档属于当前浏览器的本地文件数据。\n')
 z.write(out/'RealmGuard-Standalone.html','RealmGuard-Standalone.html')
print('Standalone HTML', (out/'RealmGuard-Standalone.html').stat().st_size,'bytes')
print('Standalone ZIP', (out/'RealmGuard-Standalone.zip').stat().st_size,'bytes')

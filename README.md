# 神域守卫 · 精绘版

此仓库用于交付当前对话中制作的 Godot 网页防守游戏与可下载独立版。

游戏包含八波防守、四向角色行走、三个技能、六件装备、BOSS 挑战和本地存档。

在线试玩：https://fffff61.github.io/gpt1/

GitHub Pages 已发布，外部真实浏览器实测 HTTP 200、引擎及资源加载、进入战场通过，浏览器 pageerror 为 0。原 ChatGPT Sites 域名在用户浏览器中出现 ERR_FAILED，请使用上述新地址。

## 独立离线版

下载 `downloads/RealmGuard-Standalone.zip` 并解压，使用新版 Edge 或 Chrome 打开其中的 HTML 文件。文件内嵌引擎、高清素材、音效和关卡，不依赖 ChatGPT Sites 域名，也无需安装程序或启动本地服务器。

`dist/` 是静态网页发布目录；`dist/RealmGuard-v0.2-source.zip` 包含完整可编辑 Godot 源码和素材。GitHub Actions 同时上传离线包，并尝试为此仓库配置 GitHub Pages；是否能够启用 Pages 取决于该私有仓库的账户计划和权限。

## 已完成验证

Windows Microsoft Edge 已实测直接打开独立 HTML、保存、断网重载及继续进度，外部网络请求为零。下载包解压一次后打开 HTML 即可。在线备用部署需要仓库所有者先在 Settings → Pages 中将 Source 设为 GitHub Actions，然后运行 Actions → Publish Realm Guard Web。仓库所有者已启用 GitHub Actions 作为 Pages 来源，部署与真实浏览器检查现已通过。

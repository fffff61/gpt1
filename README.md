# 神域守卫 · 精绘版

此仓库用于交付当前对话中制作的 Godot 网页防守游戏与可下载独立版。

游戏包含八波防守、四向角色行走、三个技能、六件装备、BOSS 挑战和本地存档。

当前 ChatGPT Sites 域名在用户浏览器中出现 ERR_FAILED，正在准备备用发布和离线交付。

## 独立离线版

下载 `downloads/RealmGuard-Standalone.zip` 并解压，使用新版 Edge 或 Chrome 打开其中的 HTML 文件。文件内嵌引擎、高清素材、音效和关卡，不依赖 ChatGPT Sites 域名，也无需安装程序或启动本地服务器。

`dist/` 是静态网页发布目录；`dist/RealmGuard-v0.2-source.zip` 包含完整可编辑 Godot 源码和素材。GitHub Actions 同时上传离线包，并尝试为此仓库配置 GitHub Pages；是否能够启用 Pages 取决于该私有仓库的账户计划和权限。

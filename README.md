# pcs-alfred-workflow

百度网盘 Alfred workflow

## 安装

环境准备：`pip3 install BaiduPCS-Py`

下载 Workflow 并安装 [https://github.com/zacksleo/pcs-alfred-workflow/releases]

## 登录

1. 在网页版百度网盘登录成功后， 从 cookie 中分别 找到 BDUSS, STOKEN 做为以下输入

2. `pcs:login {bduss} {stoken}`

![登录截图](.github/screenshot/pcs-login.png)

## 浏览目录

`pcs`

![浏览目录](.github/screenshot/pcs-root.png)

![浏览目录](.github/screenshot/pcs-dir.png)

## 搜索文件

`pcs {keyword}`

![搜索文件](.github/screenshot/pcs-search-default.png)

![搜索文件](.github/screenshot/pcs-search.png)

## 快捷键

1. 使用 Cmd, 在浏览器中打开
2. 使用 Alt(Option), 在上级目录中打开
3. 使用 Shift, 打开客户端

## 参考

API参考 [[https://github.com/PeterDing/BaiduPCS-Py]]
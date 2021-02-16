import json
import sys

bduss, stoken = sys.argv[1].split()

data = {'bduss': bduss, 'stoken': stoken}
json.dump(data, open('token.json', 'w'))
print(json.dumps({
    "items": [
        {
            "uid": "desktop",
            "type": "file",
            "title": "登录成功",
            "subtitle": "使用 pcs 搜索文件",
            "arg": "pcs",
            "icon": {
                "type": "fileicon",
                "path": "~/Desktop"
            }
        }
    ]
}))

import json
import sys
import os

bduss, stoken = sys.argv[1].split()
if not os.path.isdir(os.getenv("alfred_workflow_cache")):
    os.mkdir(os.getenv("alfred_workflow_cache"), mode=0o777)

data = {'bduss': bduss, 'stoken': stoken}
json.dump(data, open(os.getenv("alfred_workflow_cache") + '/token.json', 'w'))
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
            },
            "autocomplete": ""
        }
    ]
}))

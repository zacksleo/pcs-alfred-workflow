from typing import Optional, Dict, List, Tuple, Callable, IO
import json
import sys
from datetime import datetime
from baidupcs_py.baidupcs import BaiduPCSApi
from baidupcs_py.baidupcs.inner import (
    PcsFile)
import os
from baidupcs_py.utils import format_date, human_size

global api


def getIcon(file):
    icon = 'misc.png'
    paths = file.path.split(".")
    ext = paths[len(paths)-1]
    if file.is_dir:
        icon = 'folder.png'
    elif ext == 'html':
        icon = 'code.png'
    elif ext == 'excel':
        icon = 'excel.png'
    elif ext == 'doc' or ext == 'docx':
        icon = 'word.png'
    elif ext == 'mp3':
        icon = 'music.png'
    elif ext == 'pptx':
        icon = 'ppt.png'
    elif ext == 'txt':
        icon = 'txt.png'
    elif ext == 'zip' or ext == 'rar':
        icon = 'zip.png'
    else:
        icon = 'misc.png'

    return {
        "path":  icon
    }


def getFileName(path):
    paths = path.split("/")
    return paths[len(paths)-1]


def getFileSize(size):
    if(size == 0):
        return "\t"
    return human_size(size)


def handleFiles(query, files):
    items = []

    # PcsFile(path='/电影视频', is_dir=True, is_file=False, fs_id=950822986357574, size=0, md5=None, block_list=None, category=6, user_id=144138022, ctime=1519787106, mtime=1519787106, local_ctime=1519787106, local_mtime=1519787106, server_ctime=1519787106, server_mtime=1519787106, shared=None)
    if query.startswith("/"):
        paths = query.split("/")
        path = "/" + "/".join(paths[0:len(paths)-1])
        items.append({
            "valid": "true",
            "uid": 0,
            "type": "default",
            "title": "..",
            "subtitle": "返回上级目录",
            "arg": path,
            "autocomplete": path,
            "icon": {
                "path": 'folder.png'
            }
        })
    for file in files:
        # print(file)
        items.append({
            "valid": "true",
            "uid": file.fs_id,
            "type": "default",
            "title": getFileName(file.path),
            "subtitle": file.path + ' ' + getFileSize(file.size) + format_date(file.mtime),
            "arg": file.path,
            "autocomplete": file.path if file.is_dir else '',
            "icon": getIcon(file),
            "mods": {
                "shift": {
                    "valid": "true",
                    "arg": str(file.fs_id),
                    "subtitle": '在客户端中打开'
                },
                "alt": {
                    "valid": "true",
                    "arg": "/".join(file.path.split("/")[:-1]),
                    "subtitle": '在上级目录中打开'
                },
                "cmd": {
                    "valid": "true",
                    "arg": file.path if file.is_dir else "/".join(file.path.split("/")[:-1]),
                    "subtitle": '在网页中打开'
                },
            },
        })

    print(json.dumps({"items": items}))


def run():
    query = sys.argv[1]
    files = []
    if query == '':
        files = api.list("/")
    elif query.startswith('/'):
        files = api.list(query)
    else:
        files = api.search(query, "/", True)
    handleFiles(query, files)


if __name__ == '__main__':
    token = json.load(open('token.json', 'r'))
    api = BaiduPCSApi(bduss=token['bduss'], cookies={
        "BDUSS": token['bduss'],
        "STOKEN": token['stoken']
    })
    sys.exit(run())

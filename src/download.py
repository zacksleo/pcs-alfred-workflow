import requests
import json
import sys
import os

def get_seq(obj):
    params = {
        'browserId': os.getenv("browserId"),
        'downloadInfo': '{"method":"DownloadSelfOwnItems","uk":"'+os.getenv('uk_unique')+'","filelist":[{"isdir":"'+obj['isdir']+'","md5":"'+obj['md5']+'","size":"'+obj['size']+'","server_path":"'+obj['server_path']+'","fs_id":'+obj['fs_id']+'}]}',
    }
    # print(params)
    response = requests.post('https://pan.baidu.com/api/invoker/send', data=params)
    return response.json()['seq']


def run():
    params = {
        "fs_id": os.getenv("fs_id"),
        "isdir": os.getenv("isdir"),
        "md5": os.getenv("md5"),
        "server_path": os.getenv("server_path"),
        "size": os.getenv("size"),
        "uk": os.getenv("uk"),
    }
    print(get_seq(params))

if __name__ == '__main__':
    sys.exit(run())

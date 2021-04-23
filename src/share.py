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


def run():
    link = api.share(os.getenv("server_path"))
    print(os.getenv("name")+","+link.url)


if __name__ == '__main__':
    token = json.load(
        open(os.getenv("alfred_workflow_cache") + '/token.json', 'r'))
    api = BaiduPCSApi(bduss=token['bduss'], cookies={
        "BDUSS": token['bduss'],
        "STOKEN": token['stoken']
    })
    sys.exit(run())

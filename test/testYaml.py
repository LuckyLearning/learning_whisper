import os

import yaml

filepath = "config.yml"

if not os.path.exists(filepath):
    print("#"*20)
    print("文件不存在")

with open(filepath, encoding="utf8") as f:
    config = yaml.safe_load(f)
    print(config)
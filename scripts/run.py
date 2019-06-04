import hashlib
import time
import os
import json

DEBUG_ = False

CURRENT_DIR = os.path.abspath((os.path.dirname(__file__)))

FILE_NAMES = os.listdir(CURRENT_DIR)

FLAT_FILE_NAMES = {
    file: hashlib.md5(file.encode('utf-8')).hexdigest() + '.' + file.split(".")[1] for file in filter(lambda x : x.split(".")[1] not in  ["py", "DS_Store", "json"], FILE_NAMES)
}

out = "current.json"

content = []

print(content)
for file in FLAT_FILE_NAMES:
    if not DEBUG_: os.rename(file, FLAT_FILE_NAMES[file])
    content.append({
        "title": "",
        "src": FLAT_FILE_NAMES[file]
    })
    

with open(out, 'w') as f:
    if not DEBUG_:
        l = json.dumps(content)
        f.write(l)
    else:
        print(content)
import shutil
import os
from pathlib import Path
import datetime

rime_path = os.path.join(os.environ.get("AppData"), "Rime")
wanxiang_schema_path = os.path.join(rime_path, "wanxiang.schema.yaml")
wanxiang_pinyin_schema_path = os.path.join(rime_path, "wanxiang_pinyin.schema.yaml")
if os.path.exists(wanxiang_schema_path):
    shutil.copy(wanxiang_schema_path, wanxiang_pinyin_schema_path)
    with open(wanxiang_pinyin_schema_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 2. 在内存中进行替换
    new_content = content.replace("schema_id: wanxiang", "schema_id: wanxiang_pinyin")
    # 如果你确定要直接覆盖原文件，可以这样做：
    with open(wanxiang_pinyin_schema_path, "w", encoding="utf-8") as file:
        file.write(new_content)

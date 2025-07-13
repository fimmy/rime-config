import shutil
import os
from pathlib import Path
import datetime

rime_path = os.path.join(os.environ.get("AppData"), "Rime")
wanxiang_schema_path = os.path.join(rime_path, "wanxiang.schema.yaml")
wanxiang_double_schema_path = os.path.join(rime_path, "wanxiang_double.schema.yaml")
bak_dir_path = os.path.join(rime_path, "bak")
if os.path.exists(wanxiang_schema_path):
    # if os.path.exists(wanxiang_double_schema_path):
    #     p = Path(wanxiang_double_schema_path)
    #     bak_file_path = os.path.join(
    #         bak_dir_path,
    #         f'{p.stem}_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}{p.suffix}',
    #     )
    #     shutil.copy(wanxiang_double_schema_path, bak_file_path)
    shutil.copy(wanxiang_schema_path, wanxiang_double_schema_path)

    with open(wanxiang_double_schema_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 2. 在内存中进行替换
    new_content = content.replace("schema_id: wanxiang", "schema_id: wanxiang_double")

    # 如果你确定要直接覆盖原文件，可以这样做：
    with open(wanxiang_double_schema_path, "w", encoding="utf-8") as file:
        file.write(new_content)

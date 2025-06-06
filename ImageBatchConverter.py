# pip install pillow

from PIL import Image
from pathlib import Path

Folder = Path("H:\\Test")

From = "*.jfif"
To = "*.jpg"

for jfif in Folder.rglob(From):
    try:
        img=Image.open(jfif)
        jpg = jfif.with_suffix(To)
        img.save(jpg, "JPEG")
        jfif.unlink()  # 移除原jfif檔
        print("轉檔成功 : "+str(jfif))
    except Exception as e:
        print("轉檔失敗 : "+str(jfif)+" E : "+str(e));

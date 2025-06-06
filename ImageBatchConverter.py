# pip install pillow

from PIL import Image
from Pathlib import Path

Folder = Path("H:\\Test")

From = "*.jfif"
To = "*.jpg"

for jfif in Folder.rglob(From):
    try:
        img=Image.open(jfif)
        jpg = jfif.with_suffix(To)
        img.save(jpg, "JPEG")
        jfif.unlink()  # ������jfif��
        print("���ɦ��\ : "+jfif)
    except Exception as e:
        print("���ɥ��� : "+jfif+" e");

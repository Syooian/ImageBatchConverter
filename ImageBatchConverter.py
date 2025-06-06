# pip install pillow

from PIL import Image
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

# 啟動 tkinter 並隱藏主視窗
root = tk.Tk()
root.withdraw()

# 彈出視窗讓使用者選擇資料夾
folder_selected = filedialog.askdirectory(title="請選擇要轉換的資料夾")
if not folder_selected:
    print("未選擇資料夾，程式結束。")
    exit(0)

Folder = Path(folder_selected)

# 讓使用者手動輸入副檔名（不需加點）
From = input("輸入來源檔案的副檔名 (e.g. jpg, gif, png, jfif)： ").strip()
To = input("請輸入要轉換成什麼檔案類型 (e.g. jpg, gif, png)：").strip()

for jfif in Folder.rglob(f"*.{From}"):
    try:
        img = Image.open(jfif)
        jpg = jfif.with_suffix(f".{To}")
        img.save(jpg, "JPEG")
        jfif.unlink()  # 移除原jfif檔
        img.close() #釋放影像物件
        print("轉檔成功 : "+str(jfif))
    except Exception as e:
        print("轉檔失敗 : "+str(jfif)+" E : "+str(e))

# pip install pillow

from PIL import Image
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

# 啟動 tkinter 並隱藏主視窗
root = tk.Tk()
root.withdraw()

# 彈出視窗讓使用者選擇資料夾
folder_selected = filedialog.askdirectory(title="請選擇要搜尋的資料夾")
if not folder_selected:
    print("未選擇資料夾，程式結束。")
    exit(0)

Folder = Path(folder_selected)

DIC={}

for File in Folder.rglob("*.*"):
    try:
        #取副檔名
        ext=File.suffix.lower().lstrip('.')#去掉點

        # 判斷 DIC 中是否已有該副檔名的紀錄
        if ext in DIC:
            DIC[ext]+=1
        else:
            DIC[ext] = 1
    except Exception as e:
        print("EX : "+str(e))

Total=0

#列出所有副檔名的數量
for Key, Value in DIC.items():
    print(f"{Key} : {Value}")
    Total+=Value

print(f"總檔案數 : {Total}")
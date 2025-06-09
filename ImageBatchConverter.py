# pip install pillow

from PIL import Image
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import datetime

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
Delete = input("是否刪除原始檔案？(y/n)：").strip().lower()
Log =input("是否記錄轉換過程？(y/n)：").strip().lower()
LogArray=[]

def ShowLog(Str):
    LogArray.append("轉檔成功 : "+str(jfif))
    #print(LogStr)

for jfif in Folder.rglob(f"*.{From}"):
    try:
        img = Image.open(jfif)
        if img.mode!= 'RGB':  # 確保影像是RGB模式，否則轉換可能會失敗
            img = img.convert('RGB')

        jpg = jfif.with_suffix(f".{To}")
        img.save(jpg, "JPEG")
        if Delete == 'y':
            jfif.unlink()  # 移除原jfif檔
        img.close() #釋放影像物件

        ShowLog("轉檔成功 : "+str(jfif))
    except Exception as e:
        ShowLog("轉檔失敗 : "+str(jfif)+" E : "+str(e))

#寫入記錄檔
if Log == 'y':
    log_file = Folder / f"Log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(log_file, 'w', encoding='utf-8') as log:
        log.write(f"轉換 {From} 到 {To} ，刪除原始檔案 : {'是' if Delete == 'y' else '否'}"+"\n")
        for entry in LogArray:
            log.write(entry + '\n')
    print(f"轉換記錄已儲存至 {log_file}")
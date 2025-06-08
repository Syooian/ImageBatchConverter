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

From = input("輸入來源檔案的副檔名 (e.g. jpg, gif, png, jfif)： ").strip()
Mode = input("模式選擇。1 : 列出即將被轉換的檔案。2 : 與轉換後的檔案比較").strip()

LogArray=[]

match Mode:
    case '1':
        for File in Folder.rglob(f"*.{From}"):
            LogArray.append(str(File))

        log_file = Folder.parent / f"Log_Compare_{Mode}.txt"
        with open(log_file, 'w', encoding='utf-8') as log:
            for entry in LogArray:
                log.write(entry + '\n')
print(f"轉換記錄已儲存至 {log_file}")
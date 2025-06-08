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

LogArray=[]

Mode = input("模式選擇。1 : 列出即將被轉換的檔案。2 : 與轉換後的檔案比較").strip()

log_file = Folder.parent / f"Log_Compare_{Mode}.txt"

match Mode:
    case '1':
        From = input("輸入來源檔案的副檔名 (e.g. jpg, gif, png, jfif)： ").strip()

        for File in Folder.rglob(f"*.{From}"):
            LogArray.append(str(File))

        with open(log_file, 'w', encoding='utf-8') as log:
            for entry in LogArray:
                log.write(entry + '\n')
    case '2':
        To = input("請輸入要比對的檔案類型 (e.g. jpg, gif, png)：").strip()

        log_file_Load = Folder.parent / "Log_Compare_1.txt"
        #print(log_file_Load)

        MissingFiles=[]

        file_names=[]

        # 讀取 Log_Compare_1.txt 檔案內容
        with open(log_file_Load, 'r', encoding='utf-8') as log_load:
            file_names = [line.strip() for line in log_load.readlines()]

        # 檢查轉換後的檔案是否存在
        for File in file_names:
            #print(Path(File).stem)

            file_path = Path(File).with_suffix(f".{To}")  # 只比對檔名，不比對副檔名
            if not file_path.exists():
                MissingFiles.append(File)

        # 將缺少的檔案記錄到 log 檔案
        log_file = Folder.parent / "MissingFiles_Log.txt"
        with open(log_file, 'w', encoding='utf-8') as missing_log:
            for missing in MissingFiles:
                missing_log.write(missing + '\n')

        print(f"缺少的檔案已記錄至 {log_file}")





print(f"轉換記錄已儲存至 {log_file}")
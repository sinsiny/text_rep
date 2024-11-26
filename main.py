import os
import tkinter as tk
from tkinter import filedialog, messagebox

def replace_in_files(folder, old_str, new_str):
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            new_filename = filename.replace(old_str, new_str)
            os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, new_filename))
            
            new_filename_path = os.path.join(dirpath, new_filename)
            with open(new_filename_path, 'r', encoding='utf-8') as file:
                try:
                    content = file.read()
                    new_content = content.replace(old_str, new_str)
                    with open(new_filename_path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                except UnicodeDecodeError:
                    continue
        for dirname in dirnames: 
            new_dirname = dirname.replace(old_str, new_str)
            os.rename(os.path.join(dirpath, dirname), os.path.join(dirpath, new_dirname))

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)

def execute():
    folder = folder_entry.get()
    old_str = old_str_entry.get()
    new_str = new_str_entry.get()
    if folder and old_str and new_str:
        replace_in_files(folder, old_str, new_str)
        messagebox.showinfo("完了", "置き換えが完了しました！")
    else:
        messagebox.showwarning("警告", "すべてのフィールドを入力してください。")

root = tk.Tk()
root.title("text replace")

tk.Label(root, text="フォルダを選択:").grid(row=0, column=0, padx=5, pady=5)
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="参照", command=select_folder).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="置き換える文字列:").grid(row=1, column=0, padx=5, pady=5)
old_str_entry = tk.Entry(root, width=50)
old_str_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="新しい文字列:").grid(row=2, column=0, padx=5, pady=5)
new_str_entry = tk.Entry(root, width=50)
new_str_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="実行", command=execute).grid(row=3, columnspan=3, padx=5, pady=5)

root.mainloop()
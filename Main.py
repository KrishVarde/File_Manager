import os
import shutil
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def categorize_files():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Select Folder")
    if not folder:
        print("No folder selected.")
        return
    
    file_types = {}
    sizes = {}
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1][1:].lower()
            if ext:
                file_types.setdefault(ext, []).append(file_path)
                sizes[ext] = sizes.get(ext, 0) + os.path.getsize(file_path)
    
    for ext, files in file_types.items():
        ext_folder = os.path.join(folder, ext.upper())
        os.makedirs(ext_folder, exist_ok=True)
        for file in files:
            shutil.move(file, os.path.join(ext_folder, os.path.basename(file)))
    
    print("Files categorized successfully.")
    visualize_data(sizes)

def visualize_data(sizes):
    if not sizes:
        print("No data to visualize.")
        return
    
    labels = [ext.upper() for ext in sizes.keys()]
    sizes = [size / (1024 * 1024) for size in sizes.values()]  # Convert to MB
    
    plt.figure(figsize=(8, 6))
    plt.bar(labels, sizes, color='skyblue')
    plt.xlabel("File Categories")
    plt.ylabel("Size (MB)")
    plt.title("File Category Sizes")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    categorize_files()
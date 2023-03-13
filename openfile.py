import tkinter as tk
from tkinter import filedialog

def open_file():
    """Function to open a file dialog and return the path of the selected file."""
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path

#path = open_file()
#print(path.split('/')[-1])
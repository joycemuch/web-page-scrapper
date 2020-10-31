# web scrapper
import tkinter as tk
from tkinter.filedialog import asksaveasfile
import requests


def parse():
    try:
        url = ent.get()
        file = requests.get(url).text
        print("printing...............................................")
        x = asksaveasfile(mode="w", defaultextension=".txt")
        if x is None:
            return
        x.write(file)
    finally:
        print("url entered is wrong  or null")


root = tk.Tk()

root.title("web scrapper")
root.configure(bg='#3B2F2F')
root.iconbitmap('WebSite Scrapper/scrapper.ico')
root.geometry('1000x800')
root.attributes('-topmost', 1)

lbl = tk.Label(root, text="url  :", width=10, bg='#3B2F2F', fg='white', font=('calibre', 20, 'bold'))
ent = tk.Entry(root, width=100, borderwidth=1)
btn = tk.Button(root, width=10, text="search", command=parse, bg="grey", fg='black', font=('arial', 12, 'bold'))
b_lbl = tk.Label(root, font=('arial', 10), text='created by : joyce')

lbl.grid(row=1, column=4, pady=350, padx=20)
ent.grid(row=1, column=5, pady=150)
btn.grid(row=1, column=8, pady=350, padx=20)


if __name__ == '__main__':
    # parse()
    root.mainloop()

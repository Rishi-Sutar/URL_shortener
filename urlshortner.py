import pyperclip
import pyshorteners
from tkinter import *

root = Tk()

root.geometry("200x200")

root.title("URL Shortener")

root.configure(bg="grey")

url = StringVar()

url_address = StringVar()

def url_shortner():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)
    pyperclip.copy(url_short)


Label(root, text="URL SHORTENER").pack(pady=15)
Entry(root, textvariable=url).pack(pady=10)
Button(root, text="GENERATE & COPY URL", command=url_shortner).pack(pady=10)



root.mainloop()

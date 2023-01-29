#!/usr/bin/python3

from tkinter import *
import subprocess
import time
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw, ImageTk

REFRESH_RATE = 1000

PRIMARY_COLOR = "#a054f6"
SECONDARY_COLOR = "#d4cece"
BACKGROUND_COLOR = "#201e1e"


class Application(Tk):
    def __init__(self):
        super().__init__()
        self.init_widgets()

    def update(self):
        # Update every REFRESH_RATE ms
        dateText = datetime.now().strftime("%H:%M:%S")
        self.clockLabel.config(text=dateText)
        self.after(REFRESH_RATE, self.update)

    def init_widgets(self):
        # Logo canvas
        self.photo = ImageTk.PhotoImage(Image.open("img/logo.png"))
        self.logo = Canvas(self, width=323, height=112, bg=BACKGROUND_COLOR,
                           bd=0, highlightthickness=0, relief='ridge')
        self.logo.create_image(0, 0, anchor=NW, image=self.photo)
        self.logo.place(x=32, y=32)

        # Phone button
        self.photo2 = ImageTk.PhotoImage(Image.open("img/tel.png"))
        self.phone = Canvas(self, width=152, height=140, bg=BACKGROUND_COLOR,
                            bd=0, highlightthickness=0, relief='ridge')
        self.phoneImg = self.phone.create_image(
            0, 0, anchor=NW, image=self.photo2)
        self.phone.place(x=512, y=32)
        self.phone.isActive = False
        self.phone.bind('<Button-1>', self.onPhoneButtonClick)

        # Test button
        self.but = Button(self)
        self.but["text"] = "TEST"
        self.but["command"] = self.onTestButtonClick
        self.but.pack(side="bottom")

        # Quit button
        self.quit = Button(self)
        self.quit["text"] = "QUIT"
        self.quit["command"] = self.destroy
        self.quit.pack(side="bottom")

        # Clock init
        clockText = datetime.now().strftime("%H:%M:%S")
        self.clockLabel = Label(
            self, text=clockText, fg=PRIMARY_COLOR, bg=BACKGROUND_COLOR, font=("Courrier", 20))
        self.clockLabel.place(x=860, y=64)

        # Date init
        dateText = datetime.now().strftime("%d/%m/%Y")
        self.dateLabel = Label(self, text=dateText, fg=SECONDARY_COLOR,
                               bg=BACKGROUND_COLOR, font=("Courrier", 20))
        self.dateLabel.place(x=844, y=32)

    def scan(self):
        try:
            __import__(bluetooth)
        except ImportError:
            print("error")

        print("Scanning for bluetooth devices:")
        devices = bluetooth.discover_devices(
            lookup_names=True, lookup_class=True)
        number_of_devices = len(devices)
        print(number_of_devices, "devices found")
        for addr, name, device_class in devices:
            print("\n")
            print("Device:")
            print("Device Name: %s" % (name))
            print("Device MAC Address: %s" % (addr))
            print("Device Class: %s" % (device_class))
            print("\n")
        return

    def onTestButtonClick(self):
        test = subprocess.check_output(['whoami'])
        print(test)
        self.scan()

    def onPhoneButtonClick(self, e):
        global newimg
        if self.phone.isActive == True:
            newimg = ImageTk.PhotoImage(Image.open("img/tel.png"))
            self.phone.itemconfig(self.phoneImg, image=newimg)
            self.phone.isActive = False
        else:
            newimg = ImageTk.PhotoImage(Image.open("img/telactive.png"))
            self.phone.itemconfig(self.phoneImg, image=newimg)
            self.phone.isActive = True
        print(self.phone.isActive)


app = Application()
app.title("Black VitOS")
app.geometry("1024x600")
app.configure(bg=BACKGROUND_COLOR)
app.after(REFRESH_RATE, app.update)
app.mainloop()

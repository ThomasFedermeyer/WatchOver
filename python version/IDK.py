# Standard Library
import sys
import tkinter as tk
import time
from typing import Callable
from datetime import datetime
import numpy as np
import cv2
from PIL import ImageGrab, Image, ImageTk
import keyboard
from screeninfo import get_monitors
import pytesseract
from Character import Character


class Overlay:
    """
    Creates an overlay window using tkinter
    Uses the "-topmost" property to always stay on top of other Windows
    """

    def __init__(self,
                update_frequency_ms: int = 5_000, position: str = "+5+5",  LST: list = ((350, 200, 400, 500))):
        self.update_frequency_ms = update_frequency_ms
        self.root = tk.Tk()

        self.char1 = Character()
        

        # Set up Close Label
        # self.close_label = tk.Label(
        #     self.root,
        #     text=' X |',
        #     font=('Consolas', '14'),
        #     fg='green3',
        #     bg='grey19'
        # )
        # self.close_label.bind("<Button-1>", lambda _: sys.exit())
        # self.close_label.grid(row=0, column=0)

        # Set up Updating Text Label
        self.updating_text = tk.StringVar()
        self.updating_text_level = tk.Label(
            self.root,
            textvariable=self.updating_text,
            font=('Consolas', '14'),
            fg='green3',
            bg='grey19'
        )
        self.updating_text_level.grid(row=1, column=0)

        self.defaultImage = Image.open(r"C:\Users\tommy\Desktop\Personal projects\WatchOver\WatchOver\images\catgun.png")
        self.defaultImage2 = Image.open(r"C:\Users\tommy\Desktop\Personal projects\WatchOver\WatchOver\images\jimin.jpg")
        self.updating_Image = ImageTk.PhotoImage(self.defaultImage)
        self.updating_Image_level = tk.Label(
            self.root,
            image=self.updating_Image
        )
        self.updating_Image_level.grid(row=0, column=0)
        self.updating_Image_level.bind("<Button-1>", lambda _: sys.exit())


        # self.defaultImage2 = Image.open(r"C:\Users\tommy\Desktop\Personal projects\WatchOver\images\catgun.png")
        # self.updating_Image2 = ImageTk.PhotoImage(self.defaultImage)
        # self.updating_Image_level2 = tk.Label(
        #     self.root,
        #     image=self.updating_Image2
        # )
        # self.updating_Image_level2.grid(row=0, column=1)

        # Define Window Geometery
        self.root.overrideredirect(True)
        self.root.geometry(position)
        self.root.lift()
        self.root.wm_attributes("-topmost", True)

        self.lst1 = LST
        # self.lst2 = list((350, 621, 400, 921))
        # self.lst3 = list((400, 200, 450, 500))
        # self.lst4 = list((457, 255, 610, 665))
    # might make a lst3 that is you team ultimates

    # x_dif: 50
    # y_diff: 200
   
    def debugInfo(self, snapshot):
        img_np = np.array(snapshot)
        cv2.imshow("frame", img_np)
        for row in img_np:
            print("")
            for index in row:
                r = index[0]
                g = index[1]
                b = index[2]
                # print('\x1b[30;30;30m' + 'Success!' + '\x1b[0m')
                print('\x1b[' + str(int(r)) + ';' + str(int(g)) + ';' + str(int(b)) + 'm'  + '-' + '\x1b[0m', end=" ")



    def display(self, myList):
        screenShot = ImageGrab.grab(myList) #x, y, w, h
        return screenShot


    def update_Image(self) -> None:
        if keyboard.is_pressed('\t'):
            time.sleep(0.02)
            screenshot = self.display(self.lst1)
            self.updating_text.set(updateCharecter())
            self.updating_Image = ImageTk.PhotoImage(screenshot)
            self.updating_Image_level.configure(image = self.updating_Image)
            self.updating_Image_level.image = self.updating_Image
        elif keyboard.is_pressed('='):
            self.updating_Image = ImageTk.PhotoImage(self.defaultImage)
            self.updating_Image_level.configure(image = self.updating_Image)
            self.updating_Image_level.image = self.updating_Image
        elif keyboard.is_pressed('-'):
            self.updating_Image = ImageTk.PhotoImage(self.defaultImage2)
            self.updating_Image_level.configure(image = self.updating_Image)
            self.updating_Image_level.image = self.updating_Image

    def update_label(self) -> None:
        self.update_Image()        
        
        self.root.after(self.update_frequency_ms, self.update_label)


    def run(self) -> None:
        self.root.after(0, self.update_label)
        self.root.mainloop()

def example_callback():
    return str(datetime.now())




def get_monInfo():
    for m in get_monitors():
        if ((str(m)[str(m).index('name')+ 13:str(m).index('name')+ 21]) == 'DISPLAY4'):
            return True
    return False
    

def ImageToText(image):
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\Tesseract.exe'    
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    gray = cv2.bitwise_not(img_bin)
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.erode(gray, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)
    out_below = pytesseract.image_to_string(img)
    return out_below
    # print("OUTPUT:", out_below)

# https://overwatch.fandom.com/wiki/Ultimate_ability
# This is for charecter ultimate points
lstTime = list((125, 50, 300, 100)) # time
lstHealth = list((950, 200, 1100, 260)) # health
lstDamage = list((850, 200, 950, 260)) # Damage
def updateCharecter():
    Timephoto = ImageGrab.grab(lstTime)
    Healingphoto = ImageGrab.grab(lstHealth)
    DamagePhoto = ImageGrab.grab(lstDamage)
    Damage = ImageToText(DamagePhoto)
    Healing = ImageToText(Healingphoto)
    Time = ImageToText(Timephoto)
    if (len(Time) > 6):
        time.sleep(1)
        minuts = Time[6:Time.index(':', 6)]
        seconds = Time[Time.index(':', 6) + 1:Time.index(':', 6) + 3]
        print("minuts: " + Time[6:Time.index(':', 6)])
        print("seconds: " + Time[Time.index(':', 6) + 1:Time.index(':', 6) + 3])
        print("Damage: " + Damage)
        print("Healing: " + Healing)
        try:
            Damage = int(Damage)
        except:
            Damage = 0
        try:
            Healing = int(Healing)
        except:
            Healing = 0
        try:
            intsecomds = int(seconds)
        except:
            intsecomds = 0
        try:
            intminuts = int(minuts)
        except:
            intminuts = 0
        # the problem is that i need to check if the damage and or healing is >- 1000 beause then there is a comma, and that fucks with everything
        totalSeconds = intsecomds + (intminuts*60)
        totalUltPoints = (totalSeconds*5) + Damage + Healing
        print("ult percent should be about: " + str(totalUltPoints/2240))
        # return str(totalSeconds)
        return str(totalSeconds*5 + Damage)
    




def main():
    lst = list
    # sets the x,y,width, and height of the screencapture box 
    if get_monInfo() == True:
        print("POG")
        lst = list((457, 255, 610, 665))
    else:
        print("NOT POG ")
        lst = list((350, 200, 450, 500))
        


        # lst = list((850, 200, 1200, 500))
    overlay = Overlay(16, "+5+100", lst)
    overlay.run()

if __name__ == '__main__':
    main()
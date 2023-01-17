import numpy as np
import cv2
import keyboard
from mss import mss
from PIL import Image, ImageGrab, ImageTk
from screeninfo import get_monitors

from test import Overlay



def display():
    screenShot = ImageGrab.grab(lst) #x, y, w, h
    img_np = np.array(screenShot)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)

    

x_Start = 600
y_start = 600
lst = list((x_Start, y_start, x_Start+100, y_start+100))
def main():
    while True:
        if keyboard.is_pressed('w'):
            if (lst[1] >= 10):
                lst[1] -= 10
                lst[3] -= 10
                display()
        elif keyboard.is_pressed('a'):
            if (lst[0] >= 10):
                lst[0] -= 10
                lst[2] -= 10
                display()
        elif keyboard.is_pressed('s'):
            lst[1] += 10
            lst[3] += 10
            display()
        elif keyboard.is_pressed('d'):
            lst[0] += 10
            lst[2] += 10
            display()
            
        if keyboard.is_pressed('q'): 
            break
        else:
            t = tuple(lst)
            img = ImageGrab.grab(lst) #x, y, w, h
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
            cv2.imshow("", frame)
            if cv2.waitKey(1) & 0Xff == ord('q'):
                break
    
    cv2.destroyAllWindows()
            # screenShot = sct.grab(mon)
            # img = Image.frombytes( 'RGB', (screenShot.width, screenShot.height), screenShot.rgb,)
            # cv2.imshow('test', np.array(img)); cv2.waitKey(0)#; cv2.destroyAllWindows(); cv2.waitKey(1)

main()











"""

def resize_to_28x28(img):
    img_h, img_w = img.shape
    dim_size_max = max(img.shape)

    if dim_size_max == img_w:
        im_h = (26 * img_h) // img_w
        if im_h <= 0 or img_w <= 0:
            print("Invalid Image Dimention: ", im_h, img_w, img_h)
        tmp_img = cv2.resize(img, (26,im_h),0,0,cv2.INTER_NEAREST)
    else:
        im_w = (26 * img_w) // img_h
        if im_w <= 0 or img_h <= 0:
            print("Invalid Image Dimention: ", im_w, img_w, img_h)
        tmp_img = cv2.resize(img, (im_w, 26),0,0,cv2.INTER_NEAREST)

    out_img = np.zeros((28, 28), dtype=np.ubyte)

    nb_h, nb_w = out_img.shape
    na_h, na_w = tmp_img.shape
    y_min = (nb_w) // 2 - (na_w // 2)
    y_max = y_min + na_w
    x_min = (nb_h) // 2 - (na_h // 2)
    x_max = x_min + na_h

    out_img[x_min:x_max, y_min:y_max] = tmp_img

    return out_img

"""
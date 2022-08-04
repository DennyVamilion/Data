import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
# Das aktuelle script

#stop capture
def frame_Stop():
    root.destroy()
#opencv
def frame_Capture():
    try:
        cap = cv2.VideoCapture(0)
        succes,pimage = cap.read()
        counter = 0
        n = 0
        for i in os.listdir(r'C:\Users\Daniel\PycharmProjects\daten\Images'):
            n += 1
        n -= 1
        if (n < 0):
            n += 1
        else:
            counter += n

        while success:
            cv2.imwrite("Images/frame%d.jpg" % counter, image)
            success, image = cap.read()
            print("Image: ", counter)
            counter += 1

    except KeyboardInterrupt:
        print("Programm end")
        print("U have: ", counter, "images")
        raise SystemExit

root = Tk()
root.geometry('700x700')

#Label
label_w = tk.Label(text='Click the button to capture every frame: ')
label_w.pack

#Button Start
btn1 = tk.Button(text='Start Capture', width=15, height=5, command=frame_Capture)
btn1.pack()

#Button Stop
btn2 = tk.Button(text='Stop Capture', width=15, height=5, command=frame_Stop)
btn2.pack()

#video cam
L1 = Label(root)
L1.pack()
cap= cv2.VideoCapture(0)

def show_frames():
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   imgtk = ImageTk.PhotoImage(image = img)
   L1.imgtk = imgtk
   L1.configure(image=imgtk)
   L1.after(20, show_frames)

#Label pictures
n = 0
for i in os.listdir(r'C:\Users\Daniel\PycharmProjects\daten\Images'):
    n += 1

label_an = tk.Label(text='U have {} frames Captured'.format(n))
label_an.pack

# Positions
    #Buttons
btn1.place(x=150, y=530)
btn2.place(x=400, y=530)

    #Labels
label_w.place(x=85, y=510)
L1.place(x=27, y=27)
label_an.place(x=50, y=50)
#label1.pack(padx=10, pady=10)

show_frames()
root.mainloop()
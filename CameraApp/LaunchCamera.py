import tkinter as tk
import cv2
from PIL import Image, ImageTk

window = tk.Tk()

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

rval, frame = cap.read()
print(frame.shape)
cap.release()

window.geometry("1920x1080")
window.minsize(960, 540)
img = ImageTk.PhotoImage(image=Image.fromarray(frame))
label = tk.Label(image=img)
label.pack(expand=True)

window.mainloop()
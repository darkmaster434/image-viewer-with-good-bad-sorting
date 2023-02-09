import tkinter as tk
import os
import shutil
from PIL import Image, ImageTk
from win32api import GetSystemMetrics

screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)
main_window_x = screen_width-150
main_window_y = screen_height-150
image_resize_precentage = 45  # %
img_width = int((image_resize_precentage/100)*main_window_y)
img_height = int((image_resize_precentage/100)*main_window_x)
file_path = 'C:/Users/Corrupted/Desktop/New folder'  # folder directory
# file_path = 'C:/Users/Corrupted/Desktop/test'  # folder directory
good_path = 'C:/Users/Corrupted/Desktop/GOOD'  # good path
bad_path = 'C:/Users/Corrupted/Desktop/BAD'  # bad path

l = os.listdir(file_path)
print(len(l))


class MyGUI():
    global c
    global ima, f
    c = 0

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(str(main_window_x)+"x"+str(main_window_y))
        self.label = tk.Label(self.root, text=l[c], font=('Arial', 20))
        self.label.pack(padx=5, pady=5)
        # self.image = Image.open(file_path+'/'+str(l[c])+'.jpg')

        # self.image = self.image.resize(
        #     (img_width, img_height), Image.LANCZOS)
        # self.photo = ImageTk.PhotoImage(self.image)
        # self.canvas = tk.Canvas(
        #     self.root, width=img_width, height=img_height)
        # self.canvas.pack()
        # self.canvas.create_image(10, 10, anchor=tk.NW, image=self.photo)
        global ima
        t = Image.open(file_path+'/'+l[c])
        t = t.resize((img_width, img_height), Image.LANCZOS)
        ima = ImageTk.PhotoImage(t)
        self.photo_label = tk.Label(self.root, image=ima)
        self.photo_label.pack(padx=5, pady=5)

        button_frame = tk.Frame(self.root)

        self.next_button = tk.Button(
            button_frame, text='Next', command=self.Next_val)
        self.back_button = tk.Button(
            button_frame, text='back', command=self.Prev_val)

        self.good_button = tk.Button(
            button_frame, text='Good', command=self.Move_good)

        self.bad_button = tk.Button(
            button_frame, text='Bad', command=self.Move_bad)

        self.delete_button = tk.Button(
            button_frame, text='Delete', command=self.Delete_file, background='red2', foreground='yellow2')

        self.switch_button = tk.Button(
            button_frame, text='Switch Previous File', command=self.Switch_file)

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)

        self.back_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.good_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.bad_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.switch_button.grid(row=0, column=3, sticky=tk.W+tk.E)
        self.delete_button.grid(row=0, column=4, sticky=tk.W+tk.E)
        self.next_button.grid(row=0, column=5, sticky=tk.W+tk.E)

        button_frame.pack(fill='x')

        self.des = tk.Label(self.root, text='Welcome', background='coral')
        self.des.pack(padx=5, pady=5)
        self.root.mainloop()

    def Next_val(self):
        global f
        f = 0
        global c, ima
        c = c+1
        self.label.config(text=l[c])
        t = Image.open(file_path+'/'+l[c])
        t = t.resize((img_width, img_height), Image.LANCZOS)
        ima = ImageTk.PhotoImage(t)
        self.photo_label.config(image=ima)

    def Prev_val(self):
        global f
        f = 0
        global c, ima
        c = c-1
        self.label.config(text=l[c])
        t = Image.open(file_path+'/'+l[c])
        t = t.resize((img_width, img_height), Image.LANCZOS)
        ima = ImageTk.PhotoImage(t)
        self.photo_label.config(image=ima)

    def Move_good(self):
        global f
        f = 1
        shutil.move(file_path+'/'+l[c], good_path+'/'+l[c])
        self.dec('To Good '+l[c])
        self.Next_val()

    def Move_bad(self):
        global f
        f = 2
        shutil.move(file_path+'/'+l[c], bad_path+'/'+l[c])
        self.dec('To Bad '+l[c])
        self.Next_val()

    def Delete_file(self):
        global f
        f = 0
        os.remove(file_path+'/'+l[c])
        self.dec('Delete '+l[c])
        self.Next_val()

    def Switch_file(self):
        if f == 0:
            self.dec('Cant do anything '+l[c])
        elif f == 1:
            shutil.move(
                good_path+'/'+l[c-1], bad_path+'/'+l[c-1])
            self.dec('To bad '+l[c-1])
        elif f == 2:
            dec += 'Bad to Good'
            shutil.move(
                bad_path+'/'+l[c-1], good_path+'/'+l[c-1])
            self.dec('To Good '+l[c-1])
    def dec(self,txt):
        self.des.config(text=txt)


MyGUI()

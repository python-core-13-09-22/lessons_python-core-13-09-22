# import random
# import time
# from multiprocessing import Pool
#
#
#
#
# def my_print(index):
#
#     print(f"start my_print_{index}")
#     seconds = random.randint(0, 3)
#     time.sleep(seconds)
#     print(f"end my_print_{index} sleep {seconds}s")
#     return  seconds
#
# if __name__ == '__main__':
#     time_start = time.time()
#     vals = [i for i in range(100)]
#     with Pool(15) as pool:
#         res = pool.map(my_print, vals)
#     time_end = time.time()
#     print(f"runs {time_end - time_start}s")
#     print(f"all time {sum(res)}")

# image_labels.py
#Import the required library
from tkinter import*
#Create an instance of tkinter frame
win= Tk()
#Set the geometry
win.geometry("750x280")
#Create an canvas object
canvas= Canvas(win, width= 100, height= 100)
#Load an image inside the canvas
smiley = PhotoImage(file='smile.gif', width=50, height=50)
#Create an image in the canvas object
image_item = canvas.create_image((50,50), image=smiley )
#Bind the Button Event to the Canvas Widget
canvas.tag_bind(image_item, '<Button-1>', lambda e: smiley.configure(width=45 if smiley.width() == 50 else 50,
                                                                     height=45 if smiley.height() == 50 else 50))
canvas.pack()
win.mainloop()
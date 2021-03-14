#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:31:33 2021

@author: p.moreauneidhardt
"""

from tkinter import * 



f=Tk()
f.title("PAC-Man")


#Création du fond de la fenêtre :

w,h=736,494
image = PhotoImage(file='fondpacman.png', master=f)
canvas = Canvas(f, width=w, height=h)
canvas.create_image((w//2, h//2), image=image)


#Création des hitbox (rectangle) :


canvas.create_rectangle(0,0,25,164, fill="blue", width=0)
canvas.create_rectangle(0,0,736,15, fill="blue", width=0)
canvas.create_rectangle(711,0,736,164, fill="blue", width=0)
canvas.create_rectangle(0,479,736,494, fill="blue", width=0)
canvas.create_rectangle(711,297,736,494, fill="blue", width=0)
canvas.create_rectangle(0,297,29,494, fill="blue", width=0)


canvas.pack()#toujours à la fin
f.mainloop()
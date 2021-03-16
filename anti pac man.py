#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#21*25
from tkinter import *

class jeu():
    def __init__(self):
        self.__x=50
        self.__y=150
        self.__cote=50
        self.__speed=10
        self.__f=Tk()
        self.__f.title("Puck-Man.pptx")
        self.__carte=Canvas(self.__f,height=300,width=300)

        self.__coordMurs=[]
        
        self.createMap()

        self.__pacman=self.__carte.create_rectangle(self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1,fill="yellow")
        
        self.__f.bind("<z>",self.__north)
        self.__f.bind("<q>",self.__west)
        self.__f.bind("<s>",self.__south)
        self.__f.bind("<d>",self.__east)
        
        self.__carte.pack()
        self.__f.mainloop()
    
    def createMap(self):
        f = open("map1.txt", "r")
        x,y=0,0
        for ligne in f:
            ligne=ligne[:-1].split(",")
            for chiffre in ligne:
                if chiffre=="0":
                    self.__carte.create_rectangle(x*self.__cote,y*self.__cote,(1+x)*self.__cote,(1+y)*self.__cote,fill="blue2")
                    self.__coordMurs.append((x*self.__cote,y*self.__cote))
                elif chiffre=="1":
                    self.__carte.create_rectangle(x*self.__cote,y*self.__cote,(1+x)*self.__cote,(1+y)*self.__cote,fill="deep sky blue")
                x+=1
            y+=1
            x=0
        print(self.__coordMurs)

    def __north(self,poop):
        yTmp=self.__y-self.__speed
        for i in self.__coordMurs:
            if yTmp-self.__cote>=i[1] and i[0]+self.__cote<self.__x and self.__x+self.__cote<i[0]:
                self.__y-=self.__speed
                self.__carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                break

    def __west(self,poop):
        self.__x-=self.__speed
        self.__carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)

    def __south(self,poop):
        self.__y+=self.__speed
        self.__carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)

    def __east(self,poop):
        self.__x+=self.__speed
        self.__carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)

main=jeu()
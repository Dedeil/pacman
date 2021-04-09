#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#21*25
from tkinter import *

class jeu():
    def __init__(self):
        self.__cote=45
        self.__x=9*self.__cote
        self.__y=7*self.__cote
        self.__w=19
        self.__h=21
        self.__vitesse=9
        self.__f=Tk()
        self.__f.title("Puck-Man.pptx")
        self.__carte=Canvas(self.__f,height=self.__cote*self.__h,width=self.__cote*self.__w)

        self.__coordMurs=[]
        self.__coordBonus=[]
        self.__bonus=[]
        
        self.creerCarte()

        self.__pacman=self.__carte.create_oval(self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1,fill="yellow")
        
        self.__f.bind("<z>",self.__nord)
        self.__f.bind("<q>",self.__ouest)
        self.__f.bind("<s>",self.__sud)
        self.__f.bind("<d>",self.__est)
        
        self.__carte.pack()
        self.__f.mainloop()
    
    def creerCarte(self):
        f = open("map2.txt", "r")
        x,y=0,0
        for ligne in f:
            ligne=ligne[:-1].split(",")
            for chiffre in ligne:
                if chiffre=="0":
                    self.__carte.create_rectangle(x*self.__cote,y*self.__cote,(1+x)*self.__cote,(1+y)*self.__cote,fill="blue2")
                elif chiffre=="1":
                    self.__carte.create_rectangle(x*self.__cote,y*self.__cote,(1+x)*self.__cote,(1+y)*self.__cote,fill="deep sky blue")
                    self.__coordMurs.append((x*self.__cote,y*self.__cote))
                x+=1
            y+=1
            x=0
        #print(self.__coordMurs)
        self.ajouterBonus()
    
    def ajouterBonus(self):
        f=open("map2_bonus.txt", "r")
        x,y=0,0
        for ligne in f:
            ligne=ligne[:-1].split(",")
            for chiffre in ligne:
                if chiffre=="1":
                    self.__bonus.append(self.__carte.create_oval(x*self.__cote+9,y*self.__cote+9,(1+x)*self.__cote-9,(1+y)*self.__cote-9,fill="white"))
                    self.__coordBonus.append(((x+.5)*self.__cote,(y+.5)*self.__cote))
                x+=1
            y+=1
            x=0
            #print(self.__coordBonus)

    def __nord(self,poop):
        yTmp=self.__y-self.__vitesse
        for i in self.__coordMurs:
            if i[0]<=self.__x and self.__x+self.__cote<=i[0]+self.__cote and i[1]<=yTmp<i[1]+self.__cote:
                self.__y-=self.__vitesse
                self.__carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                self.__supprBonus(i)
                break

    def __ouest(self,poop):
        xTmp=self.__x-self.__vitesse
        for i in self.__coordMurs:
            if xTmp<0:
                self.__x+=self.__cote*(self.__w-1)
                self.__carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                self.__supprBonus(i)
                break
            elif i[0]<=xTmp<i[0]+self.__cote and i[1]<=self.__y and self.__y+self.__cote<=i[1]+self.__cote:
                self.__x-=self.__vitesse
                self.__carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                break

    def __sud(self,poop):
        yTmp=self.__y+self.__vitesse
        for i in self.__coordMurs:
            if i[0]<=self.__x and self.__x+self.__cote<=i[0]+self.__cote and i[1]-self.__cote<=yTmp<=i[1]:
                self.__y+=self.__vitesse
                self.__carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                self.__supprBonus(i)
                break

    def __est(self,poop):
        xTmp=self.__x+self.__vitesse+self.__cote
        for i in self.__coordMurs:
            if i[0]<xTmp<=i[0]+self.__cote and i[1]<=self.__y and self.__y+self.__cote<=i[1]+self.__cote:
                self.__x+=self.__vitesse
                self.__carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                self.__supprBonus(i)
                break
            elif xTmp>self.__w*self.__cote:
                self.__x=0
                self.__carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                break

    def __supprBonus(self,i):
        for j in self.__coordBonus:
            if abs(i[0]+self.__cote*.5-j[0])<=9 and abs(i[1]+self.__cote*.5-j[1])<=9:
                indice=self.__coordBonus.index(j)
                self.__coordBonus.pop(indice)
                self.__carte.coords(self.__bonus[indice],0,0,0,0)
                self.__bonus.pop(indice)
                break
        
main=jeu()

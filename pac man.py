#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#21*25
from tkinter import *
from random import choice

class menu():
    def __init__(self):
        self.__w=722
        self.__h=541
        self.__image = PhotoImage(file='pacman.png', master=f)
        self.canvas = Canvas(f, width=self.__w, height=self.__h)
        self.canvas.create_image((self.__w//2, self.__h//2), image=self.__image)
        
        self.boutonJouer=Button(f, text="Jouer",command=self.__debut)
        self.boutonQuitter=Button(f, text="Quitter", command=f.destroy)
        self.windowJouer = self.canvas.create_window(350,320,window=self.boutonJouer)
        self.windowQuitter = self.canvas.create_window(350,370,window=self.boutonQuitter)

    def __debut(self):
        self.canvas.grid_forget()
        programme=jeu()
        
        
class jeu():
    def __init__(self):
        self.__vitesse=7
        self.__cote=self.__vitesse*5
        self.__x=9*self.__cote
        self.__y=7*self.__cote
        self.__coordFant=[[9*self.__cote,9*self.__cote],[8*self.__cote,9*self.__cote],[10*self.__cote,9*self.__cote]]
        self.__fantomes=[]
        self.__directionFant=["nord","est","ouest"]
        self.__w=19
        self.__h=21
        self.__score=0
        self.__strScore=StringVar()
        self.__strScore.set("Score = "+str(self.__score))
        
        self.carte=Canvas(f,height=self.__cote*self.__h,width=self.__cote*self.__w)
        self.labelScore=Label(f,textvariable=self.__strScore)
        
        self.__coordMurs=[]
        self.__coordBonus=[]
        self.__bonus=[]
        
        self.__creerCarte()

        self.__pacman=self.carte.create_oval(self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1,fill="yellow")
        self.__creerFant(self.__coordFant[0][0],self.__coordFant[0][1],"red")
        self.__creerFant(self.__coordFant[1][0],self.__coordFant[1][1],"blue")
        self.__creerFant(self.__coordFant[2][0],self.__coordFant[2][1],"pink")
        
        f.bind("<z>",self.nord)
        f.bind("<q>",self.ouest)
        f.bind("<s>",self.sud)
        f.bind("<d>",self.est)
        
        self.labelScore.grid(column=0,row=0)
        self.carte.grid(column=0,row=1)
    
    def __creerCarte(self):
        f = open("map2.txt", "r")
        x,y=0,0
        for ligne in f:
            ligne=ligne[:-1].split(",")
            for chiffre in ligne:
                if chiffre=="0":
                    self.carte.create_rectangle(x*self.__cote,y*self.__cote,(1+x)*self.__cote,(1+y)*self.__cote,fill="blue2")
                elif chiffre=="1":
                    self.carte.create_rectangle(x*self.__cote,y*self.__cote,(1+x)*self.__cote,(1+y)*self.__cote,fill="deep sky blue")
                    self.__coordMurs.append((x*self.__cote,y*self.__cote))
                x+=1
            y+=1
            x=0
        self.ajouterBonus()

    def __creerFant(self,x,y,col):
        self.__fantomes.append(self.carte.create_oval(x+1,y+1,x+self.__cote-1,y+self.__cote-1,fill=col))
        
    def ajouterBonus(self):
        f=open("map2_bonus.txt", "r")
        x,y=0,0
        for ligne in f:
            ligne=ligne[:-1].split(",")
            for chiffre in ligne:
                if chiffre=="1":
                    self.__bonus.append(self.carte.create_oval(x*self.__cote+9,y*self.__cote+9,(1+x)*self.__cote-9,(1+y)*self.__cote-9,fill="white"))
                    self.__coordBonus.append(((x+.5)*self.__cote,(y+.5)*self.__cote))
                x+=1
            y+=1
            x=0

    def nord(self,poop):
        yTmp=self.__y-self.__vitesse
        for i in self.__coordMurs:
            if i[0]<=self.__x and self.__x+self.__cote<=i[0]+self.__cote and i[1]<=yTmp<i[1]+self.__cote:
                self.__y-=self.__vitesse
                self.carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                self.__supprBonus(i)
                break
        self.__mvtFantome()

    def ouest(self,poop):
        xTmp=self.__x-self.__vitesse
        for i in self.__coordMurs:
            if xTmp<0:
                self.__x+=self.__cote*(self.__w-1)
                self.carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                break
            elif i[0]<=xTmp<i[0]+self.__cote and i[1]<=self.__y and self.__y+self.__cote<=i[1]+self.__cote:
                self.__x-=self.__vitesse
                self.carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                self.__supprBonus(i)
                break
        self.__mvtFantome()

    def sud(self,poop):
        yTmp=self.__y+self.__vitesse
        for i in self.__coordMurs:
            if i[0]<=self.__x and self.__x+self.__cote<=i[0]+self.__cote and i[1]-self.__cote<=yTmp<=i[1]:
                self.__y+=self.__vitesse
                self.carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                self.__supprBonus(i)
                break
        self.__mvtFantome()

    def est(self,poop):
        xTmp=self.__x+self.__vitesse+self.__cote
        for i in self.__coordMurs:
            if i[0]<xTmp<=i[0]+self.__cote and i[1]<=self.__y and self.__y+self.__cote<=i[1]+self.__cote:
                self.__x+=self.__vitesse
                self.carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                self.__supprBonus(i)
                break
            elif xTmp>self.__w*self.__cote:
                self.__x=0
                self.carte.coords(self.__pacman,self.__x+1,self.__y+1,self.__x+self.__cote-1,self.__y+self.__cote-1)
                break
        self.__mvtFantome()

    def __supprBonus(self,i):
        for j in self.__coordBonus:
            if abs(i[0]+self.__cote*.5-j[0])<=9 and abs(i[1]+self.__cote*.5-j[1])<=9:
                indice=self.__coordBonus.index(j)
                self.__coordBonus.pop(indice)
                self.carte.coords(self.__bonus[indice],0,0,0,0)
                self.__bonus.pop(indice)
                if len(self.__bonus)<=0:
                    self.__toutDesassigner()
                self.__score+=100
                self.__strScore.set("Score = "+str(self.__score))
                return ""
        
    def __mvtFantome(self):
        i=0
        for coord in self.__coordFant:
            if self.__directionFant[i]=="nord":
                self.__fantNord(coord[0],coord[1],i)
            elif self.__directionFant[i]=="sud":
                self.__fantSud(coord[0],coord[1],i)
            elif self.__directionFant[i]=="est":
                self.__fantEst(coord[0],coord[1],i)
            elif self.__directionFant[i]=="ouest":
                self.__fantOuest(coord[0],coord[1],i)
            i+=1

    def __fantEst(self,x,y,j):
        if self.__coordFant[j][0]==9*self.__cote and self.__coordFant[j][1]==9*self.__cote:
            self.__directionFant[j]="nord"
            return ""
        xTmp=x+self.__vitesse+self.__cote
        if self.__x<xTmp<=self.__x+self.__cote and self.__y<=y and y+self.__cote<=self.__y+self.__cote:
            self.__toutDesassigner()
        else:
            for i in self.__coordMurs:
                if i[0]<xTmp<=i[0]+self.__cote and i[1]<=y and y+self.__cote<=i[1]+self.__cote:
                    self.__coordFant[j][0]+=self.__vitesse
                    self.carte.coords(self.__fantomes[j],self.__coordFant[j][0]+1,y+1,self.__coordFant[j][0]+self.__cote-1,y+self.__cote-1)
                    return ""
        self.__directionFant[j]=choice(("sud","nord","ouest"))

    def __fantOuest(self,x,y,j):
        if self.__coordFant[j][0]==9*self.__cote and self.__coordFant[j][1]==9*self.__cote:
            self.__directionFant[j]="nord"
            return ""
        xTmp=x-self.__vitesse
        if self.__x<=xTmp<self.__x+self.__cote and self.__y<=y and y+self.__cote<=self.__y+self.__cote:
            self.__toutDesassigner()
        else:
            for i in self.__coordMurs:
                if i[0]<=xTmp<i[0]+self.__cote and i[1]<=y and y+self.__cote<=i[1]+self.__cote:
                    self.__coordFant[j][0]-=self.__vitesse
                    self.carte.coords(self.__fantomes[j],self.__coordFant[j][0]+1,y+1,self.__coordFant[j][0]+self.__cote-1,y+self.__cote-1)
                    return ""
        self.__directionFant[j]=choice(("sud","est","nord"))

    def __fantNord(self,x,y,j):
        yTmp=y-self.__vitesse
        if self.__x<=x and x+self.__cote<=self.__x+self.__cote and self.__y<=yTmp<self.__y+self.__cote:
            self.__toutDesassigner()
        else:
            for i in self.__coordMurs:
                if i[0]<=x and x+self.__cote<=i[0]+self.__cote and i[1]<=yTmp<i[1]+self.__cote:
                    self.__coordFant[j][1]-=self.__vitesse
                    self.carte.coords(self.__fantomes[j],x+1,self.__coordFant[j][1]+1,x+self.__cote-1,self.__coordFant[j][1]+self.__cote-1)
                    return ""
        if self.__coordFant[j][1]!=245:
            self.__directionFant[j]=choice(("sud","est","ouest"))
        else:
            self.__directionFant[j]=choice(("est","ouest"))

    def __fantSud(self,x,y,j):
        yTmp=y+self.__vitesse
        if self.__x<=x and x+self.__cote<=self.__x+self.__cote and self.__y-self.__cote<=yTmp<=self.__y:
            self.__toutDesassigner()
        else:
            for i in self.__coordMurs:
                if i[0]<=x and x+self.__cote<=i[0]+self.__cote and i[1]-self.__cote<=yTmp<=i[1]:
                    self.__coordFant[j][1]+=self.__vitesse
                    self.carte.coords(self.__fantomes[j],x+1,self.__coordFant[j][1]+1,x+self.__cote-1,self.__coordFant[j][1]+self.__cote-1)
                    return ""
        self.__directionFant[j]=choice(("nord","est","ouest"))

    def __toutDesassigner(self):
        f.unbind("<z>")
        f.unbind("<q>")
        f.unbind("<s>")
        f.unbind("<d>")
        
f=Tk()
f.title("aztvfey")

menuP=menu()
"""
programme=jeu()
        
f.bind("<z>",programme.nord)
f.bind("<q>",programme.ouest)
f.bind("<s>",programme.sud)
f.bind("<d>",programme.est)

#boutonDebut=Button(f,text="Demarrer",command=Process(target=programme.debut).start().join())

programme.labelScore.grid(column=0,row=0)
programme.carte.grid(column=0,row=1)
#boutonDebut.grid(column=0,row=2)
"""
menuP.canvas.grid(row=0,column=0)
f.mainloop()

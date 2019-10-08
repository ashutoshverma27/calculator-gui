from tkinter import *
import datetime

root=Tk()
frame=Frame(root,height=485,width=490,bg="red")

root.title("Calculator")

expression=""
expr=""

def press(num):
    global expression

   
    text.insert(END,str(num))
    
    

def result():
    global expression
    try:
        date=datetime.datetime.now()
        total=str(text.get(1.0,END))
        calculated=str(eval(total))
        text.insert(END,"\n{}{}\n\n\n".format("=",calculated))
        calhist=open("history.txt","a")
        calhist.write(str(date.day)+" "+str(date.strftime("%b")))
        calhist.write("\n"+total)
        calhist.write(calculated)
        calhist.write("\n")
        calhist.close()

    except ZeroDivisionError:
            text.delete(1.0,END)
            text.insert(1.0,"Can't Divide by Zero")
    except SyntaxError:
            text.delete(1.0,END)
            text.insert(1.0,"Syntax Error")
            
    except UnboundLocalError:
        allclear()
    
    
    


def read():
    x=open("history.txt","r")
    y=x.read()
    text.delete(1.0,END)
    text.insert(1.0,y)
    print(y)
 
    
    

def allclear():

    
    text.delete(1.0,END)
    
    



def clear():
    s=text.get(1.0,END)
    length=len(s)
    t=1.0 +(length-2)*.1
    text.delete(t,END)
    print(t)


a=Button(frame,text="1",activebackground="#008080",command=lambda:press(1),font=('Helvetica', '40'),bg="#43978d",relief=GROOVE,height=1,width=3,bd=0)
a.place(x=0,y=85)

b=Button(frame,text="2",activebackground="#008080",command=lambda:press(2),font=('Helvetica', '40'),bg="#43978d",relief=GROOVE,height=1,width=3,bd=0)
b.place(x=98,y=85)

c=Button(frame,text="3",activebackground="#008080",command=lambda:press(3),font=('Helvetica', '40'),bg="#43978d",bd=0,relief=GROOVE,height=1,width=3)
c.place(x=196,y=85)

l=Button(frame,text="+",command=lambda:press("+"),activebackground='lightgrey',font=('Helvetica', '40'),relief=GROOVE,height=1,width=3,bd=0)
l.place(x=294,y=85)

d=Button(frame,text="4",activebackground="#008080",command=lambda:press(4),font=('Helvetica', '40'),bg="#43978d",bd=0,relief=GROOVE,height=1,width=3)
d.place(x=0,y=185)

e=Button(frame,text="5",activebackground="#008080",command=lambda:press(5),font=('Helvetica', '40'),bg="#43978d",bd=0,relief=GROOVE,height=1,width=3)
e.place(x=98,y=185)

f=Button(frame,text="6",activebackground="#008080",command=lambda:press(6),font=('Helvetica', '40'),bg="#43978d",bd=0,relief=GROOVE,height=1,width=3)
f.place(x=196,y=185)

m=Button(frame,text="*",command=lambda:press("*"),activebackground='lightgrey',font=('Helvetica', '40'),relief=GROOVE,height=1,width=3,bd=0)
m.place(x=294,y=185)

g=Button(frame,text="7",activebackground="#008080",command=lambda:press(7),font=('Helvetica', '40'),bg="#43978d",bd=0,relief=GROOVE,height=1,width=3)
g.place(x=0,y=285)

h=Button(frame,text="8",activebackground="#008080",command=lambda:press(8),font=('Helvetica', '40'),bg="#43978d",bd=0,relief=GROOVE,height=1,width=3)
h.place(x=98,y=285)

i=Button(frame,text="9",activebackground="#008080",command=lambda:press(9),font=('Helvetica', '40'),bg="#43978d",bd=0,relief=GROOVE,height=1,width=3)
i.place(x=196,y=285)

n=Button(frame,text="/",command=lambda:press("/"),activebackground='lightgrey',font=('Helvetica', '40'),relief=GROOVE,height=1,width=3,bd=0)
n.place(x=294,y=285)

j=Button(frame,text="0",activebackground="#008080",command=lambda:press(0),font=('Helvetica', '40'),bg="#43978d",bd=0,relief=GROOVE,height=1,width=3)
j.place(x=98,y=385)

k=Button(frame,text=".",activebackground="#008080",command=lambda:press("."),font=('Helvetica', '40'),bg="#43978d",bd=0,relief=GROOVE,height=1,width=3)
k.place(x=0,y=385)

o=Button(frame,text="%",command=lambda:press("%"),activebackground='lightgrey',font=('Helvetica', '30'),relief=GROOVE,height=1,width=4,bd=0)
o.place(x=392,y=245)

p=Button(frame,text="-",command=lambda:press("-"),activebackground='lightgrey',font=('Helvetica 40'),relief=GROOVE,height=1,width=3,bd=0)
p.place(x=294,y=385)

q=Button(frame,text="=",activebackground="#008080",command=result,font=('Helvetica', '40'),bg="#43978d",bd=0,height=1,width=3)
q.place(x=196,y=385)




allclr=Button(frame,text="AC",command=allclear,activebackground='lightgrey',font=('Helvetica', '30'),relief=GROOVE,height=3,width=4,bd=0)
allclr.place(x=392,y=85)

backspace=Button(frame,text="C",command=clear,activebackground='lightgrey',font=('Helvetica', '30'),relief=GROOVE,height=3,width=4,bd=0)
backspace.place(x=392,y=320)

text=Text(frame,font=('Helvetica', '20'),bg="#f0f5f5zz")
text.place(x=0,y=0,height=85,width=500)



frame.grid(row=0,column=0,sticky="news")
menu=Menu(root)
menu.add_command(label="History",command=read)
frame.tkraise()



root.config(menu=menu)
root.mainloop()

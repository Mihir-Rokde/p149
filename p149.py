from tkinter import*
import random
root=Tk()
root.configure(background="yellow")
root.title("Random words")
root.geometry("500x500")

label=Label(root)
def GenerateRandomWord():
    alpha_list=["A",'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    r1=random.randint(1,26)
    r2=random.randint(1,26)
    r3=random.randint(1,26)
    r4=random.randint(1,26)
    r5=random.randint(1,26)
    
    ra1=alpha_list[r1]
    ra2=alpha_list[r2]
    ra3=alpha_list[r3]
    ra4=alpha_list[r4]
    ra5=alpha_list[r5]
    
    label["text"]=ra1+ra2+ra3+ra4+ra5
btn=Button(root,text="generate random word",command=GenerateRandomWord)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
label.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
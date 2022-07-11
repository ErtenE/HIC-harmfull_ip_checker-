from tkinter import *
import datetime

def check_status():
    file=open("usom.txt","r")
    cont=file.read()
    file.close()
    ip=entry1.get()
    log_date=datetime.datetime.now()
    if str(ip) in cont:
        file=open("log.txt", "a")
        atention= str(ip)+" --> Harmful\nDate:"+str(log_date)+"\n"
        file.write(atention)
        file.close()
        v.set("IP is Harmful")
    else:
        file=open("log.txt", "a"),
        atention=str(ip)+" --> Not Harmful\nDate:"+str(log_date)+"\n"
        file.write(atention)
        file.close()
        v.set("IP is not Harmful")



#Tkinter GUI base
top= Tk()
top.title("USOM IP CHECKER")
label1=Label(top, text="Enter the IP:")
label1.place(x=50,y=180)
label1.pack()
entry1=Entry(top)
entry1.place(x=50,y=190)
entry1.pack()
v=StringVar()
entry2=Entry(top,textvariable=v)
entry2.place(x=50,y=200)
entry2.pack()
B=Button(top, text="Check  Status", command=check_status)
B.place(x=50,y=100)
B.pack()
top.mainloop()



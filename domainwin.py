from tkinter import *
from tkinter.messagebox import *



txt="""The purpose of network scanning is to manage, maintain, and secure the system using data found by the scanner.\nNetwork scanning is used to recognize available network services, discover and recognize any filtering systems in place,\nlook at what operating systems are in use, and to protect the network from attacks.It can also be used to determine the \noverall health of the network.."""
def st():
    result.insert(1.0,txt)
    
def quitApp():
    d=askyesno("Want To Quit","Are You Sure You Want to Quit")
    if d:
        win1.destroy()
def portwin():
    win1.destroy()
    import portwin
def urlwin():
    win1.destroy()
    import urlwin
def task1():
    win1.destroy()
    import files



  
def t1():
    task(1)
def t2():
    task(2)
    
def task(v):
    try:
        from pprint import pprint
        import virustotal3.core
        from tkinter import messagebox
        from virustotal_python import Virustotal
        domain = url.get()
        if domain=="":
             messagebox.showinfo("showinfo", " Domain Name can't be empty")
        else:
             # v2 example
            vtotal = Virustotal(API_KEY="ee23a655a602e049a292cb5d4cdfdc3b609de970ae3e1255b16ac086b2082a33")
            # v2 example
            resp = vtotal.request("domain/report", params={"domain": domain})

            #print(resp.response_code)
            #pprint(resp.json())
            k=resp.json()
            s=resp.json()
            # detailed infomation about the domain
            result.delete(1.0,END)
            if v==1:
                result.insert(1.0,s["whois"])
            else:
                result.insert(1.0,k['detected_urls'])
    except:
        messagebox.showinfo("showinfo", " Enter valid domain name")

clr="White"
clr1="Black"
win1=Tk() 
win1.title("Domain Scanner")
win1.wm_iconbitmap("form.ico")
win1.geometry("800x500+200+100")  #WxH+x+y
win1.config(bg=clr1)
#frames

frame1=Frame(win1,bg="red",height=50,padx=70,pady=10)
frame1.pack(side=TOP,fill="both")
frame2=Frame(win1,bg="red",height=250)
frame2.pack(side=TOP,fill="both")
frame4=Frame(win1,bg="red",height=100,padx=250)
frame4.pack(side=TOP,fill="both")

frame3=Frame(win1,bg=clr1,height=200)
frame3.pack(side=BOTTOM,fill="both")

scroll=Scrollbar(frame3)
scroll.pack(side=RIGHT,fill=Y)


b2=Button(frame1,text="Port Scanning",bg=clr,width=16,pady=5,font='Serif 10',command=portwin)
b2.pack(side=LEFT,pady=10)
b3=Button(frame1,text="URL Scanning",bg=clr,width=16,pady=5,font='Serif 10',command=urlwin)
b3.pack(side=LEFT,pady=10)
b4=Button(frame1,text="Files",bg=clr,width=16,pady=5,font='Serif 10',command=task1)
b4.pack(side=LEFT,pady=10)
b4=Button(frame1,text="Quit",bg=clr,width=8,pady=5,padx=5,font='Serif 10',command=quitApp)
b4.pack(side=LEFT,pady=10)
Label(frame2,text="Domain Scanning ",bg="red",fg="yellow", font="Georgia 18").pack(pady=5)
Label(frame2,text="Enter Domain",bg="red",fg="yellow",font="Arial 14",pady=10).pack()
url=Entry(frame2,font="Serif 14",width=30)
url.pack(pady=10)
b5=Button(frame4,text="whois",bg=clr,width=16,pady=5,font='Serif 10',command=t1)
b5.pack(pady=10,side=LEFT)
b6=Button(frame4,text="Scan",bg=clr,width=16,pady=5,font='Serif 10',command=t2)
b6.pack(pady=10,side=LEFT)


result=Text(frame3,bg=clr1,fg=clr,font='Serif 10',yscrollcommand=scroll.set,width=120,padx=10,pady=10)
result.pack(fill=Y)

scroll.config(command=result.yview)
st()

win1.mainloop()

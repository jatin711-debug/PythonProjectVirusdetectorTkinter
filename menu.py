from tkinter import *
from tkinter.messagebox import *


txt=""" This project consists of scanning of virus in the following:

1: Domain :-When referring to an Internet address or name, a domain or domain name is the location of a website.\n For example, the domain name "google.com" points to the IP address "216.58.216.164".

::> Our project can detect if the domain is infected with virus and not,It can also tell about the details of domain

2: Port :- A port is a virtual point where network connections start and end. Ports are software-based and managed by a computer's operating system. Each port is associated with a specific process or service. Ports allow computers to easily differentiate between different kinds of traffic: emails go to a different port than webpages, for instance, even though both reach a computer over the same Internet connection.

::> Project can ensure if a dangerous port is open or not

3: Url :- URL stands for Uniform Resource Locator. A URL is nothing more than the address of a given unique resource on the Web. In theory, each valid URL points to a unique resource. Such resources can be an HTML page, a CSS document, an image, etc. In practice, there are some exceptions, the most common being a URL pointing to a resource that no longer exists or that has moved. As the resource represented by the URL and the URL itself are handled by the Web server, it is up to the owner of the web server to carefully manage that resource and its associated URL.

::> Our project supports url scanning

4: files :- A file is an object on a computer that stores data, information, settings, or commands used with a computer program. In a GUI (graphical user interface), such as Microsoft Windows, files display as icons that relate to the program that opens the file. For example, all PDF icons appear the same and open in Adobe Acrobat or the reader associated with PDF files.

::> files scanning is supported
"""



def st():
    result.insert(1.0,txt)

def quitApp():
    d=askyesno("Want To Quit","Are You Sure You Want to Quit")
    if d:
        win.destroy()

def domainwin():
    win.destroy()
    import domainwin
def portwin():
    win.destroy()
    import portwin
def urlwin():
    win.destroy()
    import urlwin
def task():
    win.destroy()
    import files

clr="White"
clr1="black"
clr2="red"
win=Tk() 
win.title("Virus Scanner")
win.wm_iconbitmap("form.ico")
win.geometry("800x400+200+100")  #WxH+x+y
win.config(bg=clr1)
#frames

frame1=Frame(win,bg=clr,height=50,padx=70,pady=10)
frame1.pack(side=TOP,fill="both")
frame2=Frame(win,bg=clr,height=350)
frame2.pack(side=TOP,fill="both")


scroll=Scrollbar(frame2)
scroll.pack(side=RIGHT,fill=Y)


b1=Button(frame1,text="Domain Who is",bg=clr,width=16,pady=5,font='Serif 10',command=domainwin)
b1.pack(side=LEFT,pady=7)
b2=Button(frame1,text="Port Scanning",bg=clr,width=16,pady=5,font='Serif 10',command=portwin)
b2.pack(side=LEFT,pady=7)
b3=Button(frame1,text="URL Scanning",bg=clr,width=16,pady=5,font='Serif 10',command=urlwin)
b3.pack(side=LEFT,pady=7)
b4=Button(frame1,text="Files",bg=clr,width=16,pady=5,font='Serif 10',command=task)
b4.pack(side=LEFT,pady=7)
b5=Button(frame1,text="Quit",bg=clr,width=8,pady=5,font='Serif 10',command=quitApp)
b5.pack(side=LEFT,pady=7)
Label(frame2,text="Welcome",bg=clr,fg="purple",font="georgia 20").pack(pady=10)

result=Text(frame2,bg=clr1,fg=clr,font='Serif 10',yscrollcommand=scroll.set,width=120,padx=10,pady=10)
result.pack(fill=Y)

scroll.config(command=result.yview)
st()


win.mainloop()

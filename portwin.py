from tkinter import *
from tkinter.messagebox import *



txt="""The purpose of network scanning is to manage, maintain, and secure the system using data found by the scanner.\nNetwork scanning is used to recognize available network services, discover and recognize any filtering systems in place,\nlook at what operating systems are in use, and to protect the network from attacks.It can also be used to determine the \noverall health of the network.."""
def st():
    result.insert(1.0,txt)
def quitApp():
    d=askyesno("Want To Quit","Are You Sure You Want to Quit")
    if d:
        win3.destroy()
def domainwin():
    win3.destroy()
    import domainwin
def urlwin():
    win3.destroy()
    import urlwin
def files():
    win3.destroy()
    import files




    
def task():
    
        import socket
        import time
        from tkinter import messagebox
        
        
        # here we asking for the target website
        # or host
        target = url.get()
        # next line gives us the ip address
        # of the target
        try:
            if target=="":
                messagebox.showinfo("showinfo", " enter url")

            else:
                target_ip = socket.gethostbyname(target)
                print(target)
                print('Starting scan on host:', target_ip)

                # function for scanning ports
                
                def port_scan(port):
                        #print(target_ip,port)
                        try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.settimeout(10)
                                r=s.connect((target_ip, int(port)))
                                #time.sleep(10)
                                #print(port,"open")
                                return True
                        except:
                                #print(port,"closed")
                                return False

                list=[20,21,22,23,25,53,80,139,443,445,1433,1434,3306,3389]
                start = time.time()
                try:
                    beg= int(url1.get())
                    end= int(url2.get())
                    if beg>end:
                        messagebox.showinfo("showinfo", " beginning port shuld be less than end")
                except:
                    messagebox.showinfo("showinfo", " port Number should be integers")
                       
                # here we are scanning port 0 to 4
                s=""
                for port in range(beg,end+1):
                    #print(port)
                    p=int(port)
                    k=port_scan( port)
                    #print(k)
                    result.delete(1.0,END)
                    if k==True:
                        s=s+"\n"+"port "+str(port)+" : open"   
                        if port in list:
                           s= s+"\n"+ "!!!Dangerous port "+str(port)+" is " " open !!!"
                        
                    else:
                        s=s+"\n"+"port "+str(port)+" : close"

                end = time.time()
                
                #print(f'Time taken {end-start:.2f} seconds')
                
                result.insert(1.0,s)
                
        except:
            messagebox.showinfo("showinfo", " Url or Port not found")

clr="White"
clr1="Black"
win3=Tk() 
win3.title("Port Scanner")
win3.wm_iconbitmap("form.ico")
win3.geometry("800x500+200+100")  #WxH+x+y
win3.config(bg=clr1)
#frames

frame1=Frame(win3,bg="red",height=50,padx=70,pady=10)
frame1.pack(side=TOP,fill="both")
frame2=Frame(win3,bg="red",height=250)
frame2.pack(side=TOP,fill="both")
frame4=Frame(win3,bg="red",height=100,padx=325)
frame4.pack(side=TOP,fill="both")

frame3=Frame(win3,bg="red",height=200)
frame3.pack(side=BOTTOM,fill="both")

scroll=Scrollbar(frame3)
scroll.pack(side=RIGHT,fill=Y)

b1=Button(frame1,text="Domain Whois",bg=clr,width=16,pady=5,font='Serif 10',command=domainwin)
b1.pack(side=LEFT,pady=7)
b3=Button(frame1,text="URL Scanning",bg=clr,width=16,pady=5,font='Serif 10',command=urlwin)
b3.pack(side=LEFT,pady=7)
b4=Button(frame1,text="Files",bg=clr,width=16,pady=5,font='Serif 10',command=files)
b4.pack(side=LEFT,pady=7)
b5=Button(frame1,text="Quit",bg=clr,width=8,pady=5,font='Serif 10',command=quitApp)
b5.pack(side=LEFT,pady=7)
Label(frame2,text="Port Scanning ",bg="red",fg=clr1, font="Georgia 18").pack(pady=5)
Label(frame2,text="Enter URL",bg="red",fg=clr1,font="Arial 16").pack(pady=10)
url=Entry(frame2,font="Serif 14",width=30)
url.pack()
url1=Entry(frame4,font="Serif 14",width=3)
url1.pack(side=LEFT,pady=10)
url2=Entry(frame4,font="Serif 14",width=3)
url2.pack(side=LEFT,padx=30,pady=10)

b6=Button(frame3,text="Submit",bg=clr,width=16,pady=5,font='Serif 10',command=task)
b6.pack(pady=7)


result=Text(frame3,bg=clr1,fg=clr,font='Serif 10',yscrollcommand=scroll.set,width=120,padx=10,pady=10)
result.pack(pady=10,fill=Y)

scroll.config(command=result.yview)
st()

win3.mainloop()

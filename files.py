from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog

txt="""The purpose of network scanning is to manage, maintain, and secure the system using data found by the scanner.\nNetwork scanning is used to recognize available network services, discover and recognize any filtering systems in place,\nlook at what operating systems are in use, and to protect the network from attacks.It can also be used to determine the \noverall health of the network.."""
def st():
    result.insert(1.0,txt)

def quitApp():
    d=askyesno("Want To Quit","Are You Sure You Want to Quit")
    if d:
        win2.destroy()
def domainwin():
    win2.destroy()
    import domainwin
def portwin():
    win2.destroy()
    import portwin
def urlwin():
    win2.destroy()
    import urlwin

        

        
def files():
    result.delete(1.0,END)
    

    import os
    import time
    import json
    import virustotal3.core
    from tkinter import messagebox
    try:
        filename = filedialog.askopenfilename()# open to browse the file
        print(filename)
        #result.insert(INSERT,"SCAN STARTED")
        messagebox.showinfo("showinfo", "Scan Started")

        #API_KEY = os.environ['d6e8ddc0f68b12f65e414433c94e36bf26892c600e68727f13dbf68947242ad1']
        API_KEY='ee23a655a602e049a292cb5d4cdfdc3b609de970ae3e1255b16ac086b2082a33'
        vt = virustotal3.core.Files('ee23a655a602e049a292cb5d4cdfdc3b609de970ae3e1255b16ac086b2082a33')

        response = vt.upload(filename)
        analysis_id = response['data']['id']
        s='\nAnalysis ID: {}'.format(analysis_id)
        
        

        #result.insert(INSERT,"\n Submitted for Scan")
        #print('Analysis ID: {}'.format(analysis_id))
        results = virustotal3.core.get_analysis(API_KEY, analysis_id)
        status = results['data']['attributes']['status']

        #print('Waiting for results...')
        #result.insert(INSERT,"\n Waiting for Results")

        while 'completed' not in status:
            results = virustotal3.core.get_analysis(API_KEY, analysis_id)
            status = results['data']['attributes']['status']
            print('Current status: {}'.format(status))
            time.sleep(10)
            #result.insert(INSERT,"\n queued")
        results = virustotal3.core.get_analysis(API_KEY, analysis_id)
        k=results['data']['attributes']['results']
        import pandas as pd 
        df=pd.DataFrame(k)
        df=df.transpose()
        df=df.reset_index()
        df.loc[:,['index','category']]

        df1=df.loc[:,['index','category']]
        r=[]
        s=""
        for x in range(len(df1) ):
            #print(df1.iloc[x,:])
            r.append([df1.iloc[x,0],df1.iloc[x,1]])
            s=s+"ANTIVIRUS : "+df1.iloc[x,0]+" DETECTION RESULT : "+df1.iloc[x,1]+"\n"

            #print(s)
        lb1.config(text="SCAN COMPLETED")

        result.insert(1.0,str(s))
    except:
        messagebox.showinfo("showinfo", "Select a file")
    
clr="White"
clr1="Black"
win2=Tk() 
win2.title("Scanner")
win2.wm_iconbitmap("form.ico")
win2.geometry("800x400+200+100")  #WxH+x+y
win2.config(bg=clr1)
#frames

frame1=Frame(win2,bg="red",height=50,padx=70,pady=10)
frame1.pack(side=TOP,fill="both")
frame2=Frame(win2,bg="red",height=350)
frame2.pack(side=TOP,fill="both")
frame3=Frame(win2,bg=clr1,height=100)
frame3.pack(side=BOTTOM,fill="both")

scroll=Scrollbar(frame3)
scroll.pack(side=RIGHT,fill=Y)


b1=Button(frame1,text="Domain Who is",bg=clr,width=16,pady=5,font='Serif 10',command=domainwin)
b1.pack(side=LEFT,pady=7)
b2=Button(frame1,text="Port Scanning",bg=clr,width=16,pady=5,font='Serif 10',command=portwin)
b2.pack(side=LEFT,pady=7)
b3=Button(frame1,text="URL Scanning",bg=clr,width=16,pady=5,font='Serif 10',command=urlwin)
b3.pack(side=LEFT,pady=7)
b4=Button(frame1,text="Quit",bg=clr,width=8,pady=5,font='Serif 10',command=quitApp)
b4.pack(side=LEFT,pady=7)

Label(frame2,text="File Scanning ",bg="red",fg="yellow", font="Georgio 18").pack(pady=5)

b6=Button(frame2,text="Scan",bg=clr,width=16,pady=5,font='Arial 12',command=files)
b6.pack(pady=7)
lb1=Label(frame2,text="Start Scan",bg="red",fg="yellow",font="Arial 14")
lb1.pack(pady=10)


result=Text(frame3,bg=clr1,fg=clr,font='Serif 10',yscrollcommand=scroll.set,width=120,padx=20,pady=20)
result.pack(pady=10,fill=Y)

scroll.config(command=result.yview)
st()




win2.mainloop()

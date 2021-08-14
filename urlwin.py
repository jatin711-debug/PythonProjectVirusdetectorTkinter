from tkinter import *
from tkinter.messagebox import *

txt="""UrlScan is a security tool that restricts the types of HTTP requests that Microsoft Internet Information Services (IIS)\n will process By blocking specific HTTP requests, the UrlScan security tool helps prevent potentially harmful requests \n from reaching the server. UrlScan is implemented as an ISAPI filter that screens and analyzes HTTP requests as IIS receives them."""

def quitApp():
    d=askyesno("Want To Quit","Are You Sure You Want to Quit")
    if d:
        win4.destroy()

def domainwin():
    win4.destroy()
    import domainwin
def portwin():
    win4.destroy()
    import portwin
def task1():
    win4.destroy()
    import files


def st():
    result.insert(1.0,txt)

def task():
    from virustotal_python import Virustotal
    from tkinter import messagebox

    # v2 example
    vtotal = Virustotal(API_KEY="ee23a655a602e049a292cb5d4cdfdc3b609de970ae3e1255b16ac086b2082a33")
    from pprint import pprint

    #domain = url1.get()
    #print("domain",domain)
    # v2 example
    #resp = vtotal.request("domain/report", params={"domain": domain})

    #print(resp.response_code)
    #pprint(resp.json())

    # v3 example
    # url scanner 
    #resp = vtotal.request(f"domains/{domain}")
    import requests
    website=url1.get()

    try:
        
        if website=="":
            messagebox.showinfo("showinfo", " Url box can't be empty")
        else:
            print("url",website)
            url = 'https://www.virustotal.com/vtapi/v2/url/scan'
            params = {'apikey': 'ee23a655a602e049a292cb5d4cdfdc3b609de970ae3e1255b16ac086b2082a33', 'url':website}
            response = requests.post(url, data=params)
            #print(response.json())
            import pandas as pd
            #print(response.json())
            s=response.json()
            #print(s.get("scan_id"))
            k=s.get("scan_id")
            import requests
            url = 'https://www.virustotal.com/vtapi/v2/url/report'
            params = {'apikey': 'ee23a655a602e049a292cb5d4cdfdc3b609de970ae3e1255b16ac086b2082a33', 'resource':k}
            response = requests.get(url, params=params)
            import pandas as pd
            #print(response.json())
            r=response.json()
            r
            df = pd.DataFrame(response.json())
            df = df.reset_index()

            df.rename(columns = {'index':'antivirus'}, inplace = True) 

            df =df[(df.antivirus !='Sophos') & (df.antivirus !='Netcraft') & (df.antivirus !='StopBadware') & (df.antivirus !='Lumu') & (df.antivirus !='NotMining') & (df.antivirus !='AutoShun') & (df.antivirus !='Cyan') & (df.antivirus !='0xSI_f33d')   ]
            df.loc[:,['antivirus','scans']]
            #pprint(resp.data)
            result.delete(1.0,END)
            result.insert(1.0,r["scans"])
            print(r['scans'])
            
    except:
        messagebox.showinfo("showinfo", " Domain Not found ")
clr="White"
clr1="Black"
win4=Tk() 
win4.title(" Url Scanner")
win4.wm_iconbitmap("form.ico")
win4.geometry("800x400+200+100")  #WxH+x+y
win4.config(bg=clr1)
#frames

frame1=Frame(win4,bg="red",height=50,padx=70,pady=10)
frame1.pack(side=TOP,fill="both")
frame2=Frame(win4,bg="red",height=350)
frame2.pack(side=TOP,fill="both")
frame3=Frame(win4,bg=clr1,height=100)
frame3.pack(side=BOTTOM,fill="both")

scroll=Scrollbar(frame3)
scroll.pack(side=RIGHT,fill=Y)

b1=Button(frame1,text="Domain Who is",bg=clr,width=16,pady=5,font='Serif 10',command=domainwin)
b1.pack(side=LEFT,pady=7)
b2=Button(frame1,text="Port Scanning",bg=clr,width=16,pady=5,font='Serif 10',command=portwin)
b2.pack(side=LEFT,pady=7)
b4=Button(frame1,text="Files",bg=clr,width=16,pady=5,font='Serif 10',command=task1)
b4.pack(side=LEFT,pady=7)
b5=Button(frame1,text="Quit",bg=clr,width=8,pady=5,font='Serif 10',command=quitApp)
b5.pack(side=LEFT,pady=7)


Label(frame2,text="URL Scanning ",bg="red",fg=clr1, font="Georgia 18").pack(pady=5)
Label(frame2,text="Enter URL",bg="red",fg=clr1,font="Arial 14").pack(pady=10)
url1=Entry(frame2,font="Arial 16",width=30)
url1.pack()
b5=Button(frame2,text="Submit",bg=clr,width=16,pady=5,font='Serif 10',command=task)
b5.pack(pady=7)


result=Text(frame3,bg=clr1,fg=clr,font='Serif 10',yscrollcommand=scroll.set,width=120,padx=10,pady=10)
result.pack(pady=10,fill=Y)

scroll.config(command=result.yview)
st()


win4.mainloop()

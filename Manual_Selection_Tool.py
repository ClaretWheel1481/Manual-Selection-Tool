import tkinter as tk
import re
import urllib.request
import random
import webbrowser


#捕获API 403修复(添加User-Agent)
UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31",
    "Mozilla/5.0 (Linux; HarmonyOS; HMSCore 6.4.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.0.5.301 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604"
]

root=tk.Tk()
root.title('Manual Selection Tool')
root.geometry('425x190+750+430')
root.resizable(width=False,height=False)


#单击"Version"后打开浏览器跳转至Github项目页
def openurl(event):
    webbrowser.open("https://github.com/CrystalEggs/Manual-Selection-Tool-Python-Version",
                    new = 0)

link = tk.Label(root,
                text='Version: 0.9.2',
                height=2,
                font=("Simsum",9,'underline','bold'),
                fg="royalblue",
                cursor='hand2')
link.place(x=0,y=166)
link.bind("<Button-1>",openurl)

w=tk.Label(root,
           text='当前美元汇率：',
           height=1,
           font=("Microsoft YaHei",12))
w.place(x=10,y=10)

gx=tk.Label(root,
            text='(启动时更新)',
            height=1,
            fg='red',
            font=("Simsum",10,'bold'))
gx.place(x=165,y=16)

a=tk.Label(root,
           text='余额充值折扣数：',
           height=2,
           font=("Microsoft YaHei",12))
a.place(x=10,y=42)

b=tk.Label(root,
           text='Buff售出价格($)：',
           height=2,
           font=("Microsoft YaHei",12))
b.place(x=10,y=88)

c=tk.Label(root,
           text='Steam购入价格($)：',
           height=1,
           font=("Microsoft YaHei",12))
c.place(x=10,y=142)

d=tk.Label(root,
           text='100$预估税后利润($)',
           height=1,
           font=("Microsoft YaHei",12))
d.place(x=265,y=10)

d=tk.Label(root,
           text='预估利润率',
           height=1,
           font=("Microsoft YaHei",12))
d.place(x=300,y=71)

#汇率API抓取并转换
request=urllib.request.Request('http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXUSDCNY&column=Price')
request.add_header('User-Agent',
                   random.choice(UAS))
response=urllib.request.urlopen(request)
USDCNY=response.read()
USDCNY=USDCNY.decode('utf-8')
USDCNY=re.sub("\D","",USDCNY)
exchangerate=USDCNY
exchangerate=float(exchangerate) / 10000

hl=tk.Text(root,
           width=6,
           height=1,
           state='normal',
           cursor='exchange')
hl.insert('insert',exchangerate)
hl.configure(state='disable',
             bg="silver")
hl.place(x=120,y=18)

zk=tk.Entry(root,
            width=10)
zk.focus_set()
zk.place(x=142,y=59)

buff=tk.Entry(root,
              width=10)
buff.place(x=145,y=104)

steam=tk.Entry(root,
               width=10)
steam.place(x=160,y=149)

yj=tk.Text(root,
           width=10,
           height=2,
           cursor='heart')
yj.configure(state='disable',
             bg="silver")
yj.place(x=305,y=40)

lr=tk.Text(root,
           width=10,
           height=2,
           cursor='heart')
lr.configure(state='disable',
             bg="silver")
lr.place(x=305,y=100)

#汇率计算
def caculate():
    global huilv
    global zkshu
    global profit
    global container
    global profitmargin
    global wybuffprice
    global zhekou
    global steamprice

    zhekou=float(zk.get())
    wybuffprice=float(buff.get())
    steamprice=float(steam.get())
    huilv=int(exchangerate) * 100
    
    zkshu=huilv * zhekou
    huilv=huilv / steamprice * wybuffprice - zkshu
    profit=huilv - huilv * 0.035
    container=round(profit / zkshu * 100,2)
    profit=round(profit,1)
    profitmargin=["{:.2%}".format(container/100)]

#Textbox样式修改
def changes1():
    yj.configure(state='normal')
    lr.configure(state='normal')
    yj.delete(1.0,'end')
    lr.delete(1.0,'end')
    yj.insert('insert',profit)
    if container > 0:
        lr.configure(fg='red')
    elif container <= 0:
        lr.configure(fg='green')
    lr.insert('insert',profitmargin)
    yj.configure(state='disable')
    lr.configure(state='disable')

button=tk.Button(root,text="计算",
                 command=lambda:[caculate(),changes1()],
                 relief="groove",
                 cursor='hand2')
button.configure(height=2,
                 width=10,
                 font=("Simsum",10))
button.place(x=302,y=140)


root.mainloop()


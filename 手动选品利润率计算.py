import tkinter as tk
import re
import urllib.request
import random

#捕获API 403修复(添加User-Agent)
UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4826.60 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31"
]

root=tk.Tk()
root.title('手动选品利润率计算器 v0.9 ')
root.geometry('500x200+700+430')
root.resizable(width=False,height=False)

#下方仍在寻找可国内外正常且快速使用的IP查询的API

#较快的:http://ip.42.pl/raw
#       https://checkip.amazonaws.com/

hostname = urllib.request.Request('http://ip.42.pl/raw')
response0=urllib.request.urlopen(hostname)
IP=response0.read()
ipp=tk.Label(root,
             text=IP,
             height=2,
             font=("微软雅黑",9,'italic'))
ipp.place(x=400,y=170)

baseip=tk.Label(root,
           text='您的IP地址：',
           height=2,
           font=("微软雅黑",9,'italic'))
baseip.place(x=326,y=170)

w=tk.Label(root,
           text='当前美元汇率：',
           height=2,
           font=("黑体",12))
w.place(x=10,y=9)

gx=tk.Label(root,
            text='(每次启动更新)',
            height=1,
            fg='red')
gx.place(x=175,y=16)

a=tk.Label(root,
           text='输入余额充值的折扣数',
           height=2,
           font=("黑体",12))
a.place(x=10,y=50)

b=tk.Label(root,
           text='输入Buff售出价格 ($)',
           height=2,
           font=("黑体",12))
b.place(x=10,y=100)

c=tk.Label(root,
           text='输入Steam购入价格($)',
           height=2,
           font=("黑体",12))
c.place(x=10,y=150)

d=tk.Label(root,
           text='100$预估税后利润($)',
           height=1,
           font=("黑体",12))
d.place(x=310,y=12)

d=tk.Label(root,
           text='预估利润率',
           height=1,
           font=("黑体",12))
d.place(x=345,y=73)

#汇率API抓取并转换
request=urllib.request.Request('http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXUSDCNY&column=Price')
request.add_header('User-Agent',
                   random.choice(UAS))
response=urllib.request.urlopen(request)
USDCNY=response.read()
USDCNY=USDCNY.decode('utf-8')
USDCNY=re.sub("\D","",USDCNY)
FINAL=USDCNY
FINAL=float(FINAL) / 10000

hl=tk.Text(root,
           width=6,
           height=1,
           state='normal',
           cursor='exchange')
hl.insert('insert',FINAL)
hl.configure(state='disable')
hl.place(x=120,y=20)

zk=tk.Entry(root,
            width=10)
zk.focus_set()
zk.place(x=180,y=60)

buff=tk.Entry(root,
              width=10)
buff.place(x=180,y=110)

steam=tk.Entry(root,
               width=10)
steam.place(x=180,y=160)

yj=tk.Text(root,
           width=10,
           height=2,
           cursor='heart')
yj.configure(state='disable')
yj.place(x=350,y=40)

lr=tk.Text(root,
           width=10,
           height=2,
           cursor='heart')
lr.configure(state='disable')
lr.place(x=350,y=100)

#字符串转换成浮点型
def convert1():
    global wybuff
    global zhekou
    global steamd

    zhekou=float(zk.get())
    wybuff=float(buff.get())
    steamd=float(steam.get())

#汇率计算
def caculate():
    global PP
    global zkshu
    global FF
    global summ
    global others
    global FIN
    global FIE
    global BIE

    PP=int(FINAL) * 100
    zkshu=PP * zhekou
    FF=PP / steamd
    FF=FF * wybuff
    FF=FF - zkshu
    others= FF * 0.035
    summ=FF - others
    FIN=summ / zkshu
    FIE=FIN * 100
    FIE=round(FIE,2)
    summ=round(summ,2)
    BIE=["{:.2%}".format(FIE/100)]

#Textbox样式修改
def changes1():
    yj.configure(state='normal')
    lr.configure(state='normal')
    yj.delete(1.0,'end')
    lr.delete(1.0,'end')
    yj.insert('insert',summ)
    if FIE > 0:
        lr.configure(fg='red')
    elif FIE <= 0:
        lr.configure(fg='green')
    lr.insert('insert',BIE)
    yj.configure(state='disable')
    lr.configure(state='disable')

button=tk.Button(root,text="计算",
                 command=lambda:[convert1(),caculate(),changes1()],
                 relief="groove")
button.configure(height=2,
                 width=12,
                 font=("宋体",11))
button.place(x=335,y=140)


root.mainloop()


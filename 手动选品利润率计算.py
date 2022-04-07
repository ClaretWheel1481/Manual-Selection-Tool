import tkinter as tk
import re
import urllib.request
import random
import os

my_headers = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29",
]

root=tk.Tk()
root.title('手动选品利润率计算器 v0.6 ')
root.geometry('500x200+680+350')
root.resizable(width=False,height=False)


w=tk.Label(root,text='当前美元汇率',height=2,font="微软雅黑")
w.place(x=10,y=5)
gx=tk.Label(root,text='(联网实时更新)',height=1,fg='red')
gx.place(x=175,y=17)
a=tk.Label(root,text='输入余额充值的折扣数',height=2,font="微软雅黑")
a.place(x=10,y=50)
b=tk.Label(root,text='输入Buff售出价格 ($)',height=2,font="微软雅黑")
b.place(x=10,y=100)
c=tk.Label(root,text='输入Steam购入价格($)',height=2,font="微软雅黑")
c.place(x=10,y=150)
d=tk.Label(root,text='100$预计税后利润($)',height=1,font="微软雅黑")
d.place(x=310,y=1)
d=tk.Label(root,text='预计利润率(%)',height=1,font="微软雅黑")
d.place(x=340,y=60)

request=urllib.request.Request('http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXUSDCNY&column=Price')
request.add_header('User-Agent',random.choice(my_headers))
response=urllib.request.urlopen(request)
USDCNY=response.read()
USDCNY=USDCNY.decode('utf-8')
USDCNY=re.sub("\D","",USDCNY)
FINAL=USDCNY
FINAL=float(FINAL) / 10000

hl=tk.Text(root,width=6,height=1,state='normal',cursor='circle')
hl.insert('insert',FINAL)
hl.configure(state='disable')
hl.place(x=120,y=21)
zk=tk.Text(root,width=10,height=2)
zk.place(x=180,y=60)
buff=tk.Text(root,width=10,height=2)
buff.place(x=180,y=110)
steam=tk.Text(root,width=10,height=2)
steam.place(x=180,y=160)
yj=tk.Text(root,width=10,height=2)
yj.configure(state='disable')
yj.place(x=350,y=30)
lr=tk.Text(root,width=10,height=2)
lr.configure(state='disable')
lr.place(x=350,y=90)

def onClick1():

    global zhekou

    zhekou=zk.get(1.0,"end")
    zhekou=str.strip(zhekou)
    zhekou=float(zhekou)
    
def onClick2():

    global wybuff

    wybuff=buff.get(1.0,"end")
    wybuff=str.strip(wybuff)
    wybuff=float(wybuff)
    
def onClick3():

    global steamd

    steamd=steam.get(1.0,"end")
    steamd=str.strip(steamd)
    steamd=float(steamd)
    
def onClick4():
    global PP
    global zkshu
    global FF
    global summ
    global others
    global FIN
    global FIE

    PP=int(FINAL) * 100
    zkshu=PP * zhekou
    FF=PP / steamd
    FF=FF * wybuff
    FF=FF - zkshu
    others= FF * 0.035
    summ=FF - others
    FIN=summ / zkshu
    FIE=FIN * 100
    FIE=round(FIE,3)
    summ=round(summ,2)

def onClick5():
    yj.configure(state='normal')
    lr.configure(state='normal')
    yj.delete(1.0,'end')
    lr.delete(1.0,'end')
    yj.insert('insert',summ)
    if FIE > 0:
        lr.configure(fg='red')
    elif FIE<=0:
        lr.configure(fg='green')
    lr.insert('insert',FIE)
    yj.configure(state='disable')
    lr.configure(state='disable')

button=tk.Button(root,text="计算",command=lambda:[onClick1(),onClick2(),onClick3(),onClick4(),onClick5()])
button.place(x=370,y=160)

root.mainloop()



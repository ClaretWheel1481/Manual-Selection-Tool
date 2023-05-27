import tkinter as tk
import webbrowser
import json
from tkinter import messagebox
from urllib.request import urlopen

root=tk.Tk()
root.title('Steam搬砖手动选品利润计算工具')
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d'%(420,190,(screenwidth-420)/2,(screenheight-190)/2))
root.resizable(width=False,height=False)
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
root.withdraw()

if messagebox.askyesno('警告','该应用所计算的任何数据并非100%精准，造成任何财产损失请自行承，请确认是否继续使用？') == True:
#汇率API抓取并转换
#API备用：
# https://api.it120.cc/gooking/forex/rate?fromCode=CNY&toCode=USD
# https://api.exchangerate-api.com/v4/latest/USD
    response=urlopen("https://api.exchangerate-api.com/v4/latest/USD")
    exchangerate=json.loads(response.read())['rates']['CNY']

#单击"Version"打开浏览器至Github项目页
    def openurl(event):
        webbrowser.open("https://github.com/ClaretWheel1481/Manual-Selection-Tool",new = 0)

    link = tk.Label(root,
                    text='Version: 0.9.9',
                    height=2,
                    font=("Simsum",9,'underline','bold'),
                    fg="royalblue",
                    cursor='hand1')
    link.place(x=0,y=165)
    link.bind("<Button-1>",openurl)

    w=tk.Label(root,
               text='当前美元汇率：',
               height=1,
               font=("Microsoft YaHei",12))
    w.place(x=10,y=8)

    gx=tk.Label(root,
                text='(启动即更新)',
                height=1,
                fg='red',
                font=("Simsum",10,'bold'))
    gx.place(x=165,y=14)

    a=tk.Label(root,
               text='余额充值折扣：',
               height=2,
               font=("Microsoft YaHei",12))
    a.place(x=10,y=40)

    b=tk.Label(root,
               text='Buff售出价格：',
               height=2,
               font=("Microsoft YaHei",12))
    b.place(x=10,y=86)

    c=tk.Label(root,
               text='Steam购入价格：',
               height=1,
               font=("Microsoft YaHei",12))
    c.place(x=10,y=140)

    d=tk.Label(root,
               text='100$税后利润($)',
               height=1,
               font=("Microsoft YaHei",12))
    d.place(x=280,y=8)

    d=tk.Label(root,
               text='利润率',
               height=1,
               font=("Microsoft YaHei",12))
    d.place(x=315,y=69)
    
    wn=tk.Label(root,
               text='7折 输入“0.7”',
               height=1,
               fg='blue',
               font=("Microsoft YaHei",9))
    wn.place(x=14,y=75)

    hl=tk.Text(root,
               width=6,
               height=1,
               state='normal',
               cursor='exchange')
    hl.insert('insert',exchangerate)
    hl.configure(state='disable',
                 bg="silver")
    hl.place(x=120,y=16)

    zk=tk.Entry(root,
                width=10)
    zk.focus_set()
    zk.place(x=129,y=56)

    buff=tk.Entry(root,
                  width=10)
    buff.place(x=129,y=102)

    steam=tk.Entry(root,
                   width=10)
    steam.place(x=135,y=147)

    yj=tk.Text(root,
               width=10,
               height=2)
    yj.configure(state='disable',
                 bg="silver")
    yj.place(x=305,y=38)

    lr=tk.Text(root,
               width=10,
               height=2)
    lr.configure(state='disable',
                 bg="silver")
    lr.place(x=305,y=98)
    
    root.deiconify()
    
#汇率计算
    def caculate():
        global EXCRate
        global zkshu
        global profit
        global container
        global profitmargin
        global wybuffprice
        global DisCounts
        global steamprice

        DisCounts=float(zk.get())
        wybuffprice=float(buff.get())
        steamprice=float(steam.get())
        EXCRate=int(exchangerate) * 100
        
        zkshu=EXCRate * DisCounts
        EXCRate=EXCRate / (steamprice / EXCRate) * (wybuffprice/EXCRate) - zkshu
        profit=EXCRate - EXCRate * 0.035
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
    
else:
    root.destroy()
    root.quit()



import tkinter as tk

root=tk.Tk()
root.title('Helix Excusive')
root.geometry('200x200')
"""
var = tk.StringVar()
l = tk.Label(root, textvariable=var,bg='red',font=('Arial',12), width=15, height=2)
l.pack()
hit_flag = False

def hit_me():
    global hit_flag
    if hit_flag ==False:
        hit_flag = True
        var.set('hit sucess')
    else:
        hit_flag =  False
        var.set('hit close')

b = tk.Button(root, text='Start Crawler', width=15, height=2, command=hit_me)
b.pack()

"""
"""
e = tk.Entry(root,show='*')
e.pack()

t = tk.Text(root,height=2)
t.pack()



def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert('end',var)

b1 = tk.Button(root,text="insert point",width=15,height=2,command=insert_point)
b1.pack()

b2 = tk.Button(root,text="insert end",command=insert_end)
b2.pack()

t = tk.Text(root,height=2)
t.pack()
"""

var1 = tk.StringVar()    #创建变量
l =tk.Label(root,bg='yellow',width=4,textvariable=var1)
l.pack()



var2 = tk.StringVar()
var2.set((11,22,33,44)) #为变量设置值

#创建Listbox

lb = tk.Listbox(root, listvariable=var2)  #将var2的值赋给Listbox
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end', item)  #从最后一个位置开始加入值

lb.insert(1, 'first')       #在第一个位置加入'first'字符
lb.insert(2, 'second')      #在第二个位置加入'second'字符
lb.delete(2)                #删除第二个位置的字符
lb.pack()

def print_selection():
    value = lb.get(lb.curselection())   #获取当前选中的文本
    var1.set(value)     #为label设置值
b1 = tk.Button(root, text='print selection', width=15,height=2, command=print_selection)
b1.pack()

root.mainloop()


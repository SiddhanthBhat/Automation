from tkinter import *
from datetime import datetime
import xlrd
import csv

root = Tk()
time1 = ''
n=int(0)
auth=0
fields = []
Emprows = [] 
fields2 = []
items = [] 
bill =[]
tempbillitem=""
tempbillQty=""
tempprice=""
displaynum = StringVar()
displayTime = StringVar()
displayDate = StringVar()
displayID = StringVar()
displayItem= StringVar()
displayQty= StringVar()
displayID.set("Enter Employee ID")
canvas = Canvas(root, width=1300, height=768)
canvas.grid(columnspan=9, rowspan=8)

# Data Import Employee
def emplist():
    filename = "C:/Users/siddh/Desktop/Project/employee.csv" #PATH OF EMPLOYEE LIST
    
    # initializing the titles and Emprows list
    global fields
    global Emprows

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        
        # extracting field names through first row
        fields = next(csvreader)
    
        # extracting each data row one by one
        for row in csvreader:
            Emprows.append(row)
# Data Import Menu
def menulist():
    filename = "C:/Users/siddh/Desktop/Project/menu.csv" #PATH OF MENU LIST
    
    # initializing the titles and Emprows list
    global fields2
    global items

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        
        # extracting field names through first row
        fields2 = next(csvreader)
    
        # extracting each data row one by one
        for row in csvreader:
            items.append(row)  
# Code
def timeset():
    now=datetime.now()
    t_string = now.strftime("%H:%M:%S")
    displayTime.set(t_string)
    d_string = now.strftime("%d/%m/%Y")
    displayDate.set(d_string)

def num(x):
    global n
    n= (n * 10) + x
    displaynum.set(n)


def delete():
    global n
    n=0
    displaynum.set("")


def yes():
   global auth
   global displayItem
   global n
   global tempbillitem
   global tempbillQty
   global tempprice
   global Emprows
   global items
   n=str(n)
   emplist()
   menulist()
   print(n)
   if (auth==0):
        i=0
        while i<len(Emprows):
            if n == Emprows[i][0]:
                displayItem.set("Welcome, Enter Order")
                displayID.set(Emprows[i][1])
                timeset()
                n=0
                displaynum.set("")
                auth=1
                break  
            i +=1
   if(auth==1):                 #Input Item Index
        i=0
        displayQty.set("")
        while i<len(items):
           if n == items[i][0]:
                displayItem.set(items[i][1])
                tempbillitem = items[i][1]
                tempprice = items[i][2]
                n=0
                displaynum.set("")
                auth = 2
                return 
           i +=1
   if(auth==2):                 #Input Quantity
       displayQty.set(n)
       tempbillQty=n
       bill.append(tempbillitem)
       bill.append(tempbillQty)
       bill.append(tempprice)
       total = int(tempbillQty) * int(tempprice)
       bill.append(total)
       auth = 1
       n=0
       return


def output():
    global bill
    txtBillName.insert(1,"Item")
    txtBillQty.insert(1,"Qty.")
    txtBill1.insert(1,"Price")
    txtBilltotal.insert(1,"Total")
    i=0
    y=2
    while i < len(bill):
        txtBillName.insert(y,bill[i])
        txtBillQty.insert(y,bill[i+1])
        txtBill1.insert(y,bill[i+2])
        txtBilltotal.insert(y,bill[i+3])
        i=i+4
        y+=1
    total=0
    i=0
    while i<len(bill):
        total=total +int(bill[i+3])
        i+=4
    txtBillName.insert(y+2,"Grand Total")
    txtBilltotal.insert(y+2,total)


def exit(code):
    global auth, fields,Emprows,fields2,items,bill,tempbillitem,tempbillQty,tempprice,n
    if code==1:
        n=int(0)
        auth=0
        fields = []
        Emprows = [] 
        fields2 = []
        items = [] 
        bill =[]
        tempbillitem=""
        tempbillQty=""
        tempprice=""
        displaynum.set("")
        displayTime.set("")
        displayDate.set("")
        displayID.set("Enter Employee ID")
        displayItem.set("")
        displayQty.set("")
        txtBilltotal.delete(0,END)
        txtBill1.delete(0,END)
        txtBillQty.delete(0,END)
        txtBillName.delete(0,END)
    else:
        n=int(0)
        auth =1
        fields = []
        Emprows = [] 
        fields2 = []
        items = [] 
        bill =[]
        txtBilltotal.delete(0,END)
        txtBill1.delete(0,END)
        txtBillQty.delete(0,END)
        txtBillName.delete(0,END)
        tempbillitem=""
        tempbillQty=""
        tempprice=""
        displaynum.set("")
        displayTime.set("")
        displayDate.set("")
        displayItem.set("Input New Order")
        displayQty.set("")
        timeset()
 

# Numbers
btnMenu = Button(root, text='Menu',fg='white', width=5, bg='black', command=lambda:test(), font = 1)
btnMenu.grid(column=0, row=0,sticky='nesw')
btn0 = Button(root, text='0',fg='white', width=5, bg='black', command=lambda:num(0), font = 1)
btn0.grid(column=1, row=5,sticky='nesw')
btn1 = Button(root, text='1',fg='white', width=5, bg='black', command=lambda:num(1), font = 1)
btn1.grid(column=0, row=4,sticky='nesw')
btn2 = Button(root, text='2',fg='white', width=5, bg='black', command=lambda:num(2), font = 1)
btn2.grid(column=1, row=4,sticky='nesw')
btn3 = Button(root, text='3',fg='white', width=5, bg='black', command=lambda:num(3), font = 1)
btn3.grid(column=2, row=4,sticky='nesw')
btn4 = Button(root, text='4',fg='white', width=5, bg='black', command=lambda:num(4), font = 1)
btn4.grid(column=0, row=3,sticky='nesw')
btn5 = Button(root, text='5',fg='white', width=5, bg='black', command=lambda:num(5), font = 1)
btn5.grid(column=1, row=3,sticky='nesw')
btn6 = Button(root, text='6',fg='white', width=5, bg='black', command=lambda:num(6), font = 1)
btn6.grid(column=2, row=3,sticky='nesw')
btn7= Button(root, text='7',fg='white', width=5, bg='black', command=lambda:num(7), font = 1)
btn7.grid(column=0, row=2,sticky='nesw')
btn8 = Button(root, text='8',fg='white', width=5, bg='black', command=lambda:num(8), font = 1)
btn8.grid(column=1, row=2,sticky='nesw')
btn9 = Button(root, text='9',fg='white', width=5, bg='black', command=lambda:num(9), font = 1)
btn9.grid(column=2, row=2,sticky='nesw')
btnYes = Button(root, text='Yes',fg='white', width=5, bg='black', command=lambda:yes(), font = 1)
btnYes.grid(column=0, row=5,sticky='nesw')
btnDel = Button(root, text='Del.',fg='white', width=5, bg='black', command=lambda:delete(), font = 1)
btnDel.grid(column=2, row=5,sticky='nesw')
btnExit = Button(root, text='Exit',fg='white', width=5, bg='black', command=lambda:exit(1), font = 1)
btnExit.grid(column=0, row=7,sticky='nesw')
btnCan = Button(root, text='Cancel/New',fg='white', width=5, bg='black', command=lambda:exit(0), font = 1)
btnCan.grid(column=1, row=7,sticky='nesw')
btnPrint = Button(root, text='Print Bill',fg='white', bg='black', command=lambda:output(), font = 1)
btnPrint.grid(column=2, row=7, columnspan=3,sticky='nesw')

# ViewBox
inputTxt = Label(root, textvariable=displayItem, fg='black', bg='gray', font=("Arial", 15))
inputTxt.grid(column=1, row=0,sticky='nesw',columnspan=8)
inputQty = Label(root, textvariable=displayQty, fg='black', bg='yellow', font=("Arial", 15))
inputQty.grid(column=8, row=0,sticky='nesw')
inputNum = Label(root, textvariable=displaynum, fg='black', bg='gray', font=("Arial", 15))
inputNum.grid(column=0, row=1,sticky='nesw',columnspan=3)
txtUser = Label(root, textvariable=displayID, fg='black', bg='gray', font=("Arial", 15))
txtUser.grid(column=0, row=6,sticky='nesw',columnspan=9)
txtBillName = Listbox(root, fg='black', bg='blue', font=("Arial", 15))
txtBillName.grid(column=3, row=1,sticky='nesw',columnspan=3,rowspan=5)
txtBillQty = Listbox(root, fg='black', bg='green', font=("Arial", 15))
txtBillQty.grid(column=6, row=1,sticky='nesw',columnspan=1,rowspan=5)
txtBill1 = Listbox(root, fg='black', bg='white', font=("Arial", 15))
txtBill1.grid(column=7, row=1,sticky='nesw',columnspan=1,rowspan=5)
txtBilltotal =Listbox(root, fg='black', bg='gray', font=("Arial", 15))
txtBilltotal.grid(column=8, row=1,sticky='nesw',columnspan=1,rowspan=5)
clock = Label(root, textvariable=displayTime, fg='black', bg='white', font=("Arial", 15))
clock.grid(column=7, row=7,sticky='nesw',columnspan=2)
date = Label(root, textvariable=displayDate, fg='black', bg='gray', font=("Arial", 15))
date.grid(column=5, row=7,sticky='nesw',columnspan=2)


root.mainloop()

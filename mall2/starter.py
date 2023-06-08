import re
from tkinter import messagebox

def ppp(data):
    f = re.split("\*|\n", data)
    if f[-1]=="":
        f.pop()
    return f

def write(data):
    f = open("check.txt","w")
    for i in range(0,len(data),4):
        reg = f"{data[i]}*{data[i+1]}*{data[i+2]}*{data[i+3]}\n"
        f.write(reg)
    f.close()

def rewrite():
    f = open("check.txt","r")
    f3 = f.read()
    f.close()
    f3 = ppp(f3)
    a = ""
    for i in range(3,len(f3),4):
        a += f"{f3[i]}\t{f3[i-2]}\t{f3[i-1]}<br>------------------------------------------<br>"
    return a

def check(item,quantity):
    f = open("check.txt","r")
    f3 = f.read()
    f.close()
    f3 = ppp(f3)
    isthere = False
    for i in range(0,len(f3),4):
        if f3[i]==item:
            isthere = True
            qb = int(f3[i+2])
            qa = int(quantity)
            qb += qa
            f3[i+2]=qb
            write(f3)
            break
    if isthere == False:
        f = open("inventory.txt","r")
        global f2
        f2 = f.read()
        f.close()
        f2 = ppp(f2)
        for i in range(0,len(f2),3):
            if f2[i]==item:
                name = f2[i+2]
                price = f2[i+1]
                break
        f = open("check.txt","a")
        reg = f"{item}*{price}*{quantity}*{name}\n"
        f.write(reg)
        f.close()

def remove(item,quantity):
    f = open("check.txt","r")
    f3 = f.read()
    f.close()
    f3 = ppp(f3)
    for i in range(0,len(f3),4):
        if f3[i]==item:
            qb = int(f3[i+2])
            qa = int(quantity)
            qb -= qa
            f3[i+2]=qb
            write(f3)
            break

def calculate():
    f = open("check.txt","r")
    f3 = f.read()
    f.close()
    f3 = ppp(f3)
    a = 0
    for i in range(1,len(f3),4):
        a += float(f3[i])*int(f3[i+1])
    a += 0.09*a
    a = str(a)
    a2 = a.split(".")
    z = int(a2[0])
    h = ""
    count = 0
    while z > 0:
        rem = z % 10
        z //= 10
        h += str(rem)
        count += 1
        if count==3 and z > 10:
            h += ","
            count = 0
        print(h)
    h = h[::-1]
    a = h + "." + a2[1]
    messagebox.showinfo(title="SEE YOU LATER!",message=f"TOTAL:\t{a}")
    
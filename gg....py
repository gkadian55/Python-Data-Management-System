import pickle
print("                             ****************EMPERORS CYBER CAFE WELCOMES YOU****************        ")
print("                                               CYBER CAFE MANAGEMENT SYSTEM            ")
def write():
    f=open("ccmd.dat","wb")
    record=[]
    while True:
        sno=int(input("ID : "))
        name=input("Name : ")
        age=int(input("Age : "))
        ad=input("E-Mail : ")
        charge=int(input("Charges : "))
        data=[sno,name,age,ad,charge]
        record.append(data)
        ch=input("Do You Want To Enter More Data(Y/N) : ")
        if ch in 'Nn':
            break
    pickle.dump(record,f)
    print("Details Added..")
    f.close()

def read():
    print("Customer Details Are..")
    f=open("ccmd.dat","rb")
    try:
        while True:
            s=pickle.load(f)

            for i in s:
                print(i)
    except Exception:
        f.close()

def append():
    f=open("ccmd.dat","rb+")
    print("Add Details..")
    rec=pickle.load(f)
    while True:
        sno=int(input("ID : "))
        name=input("Name : ")
        age=int(input("Age : "))
        ad=input("E-Mail : ")
        charge=int(input("Charges : "))
        data=[sno,name,age,ad,charge]
        rec.append(data)
        ch=input("Do You Want To Enter More Data(Y/N) : ")
        if ch in 'Nn':
            break
    f.seek(0)
    pickle.dump(rec,f)
    print("Details Added..")
    f.close()

def search():
    f=open("ccmd.dat","rb")
    r=int(input("Enter ID To Search For Details : "))
    found=0
    try:
        while True:
            s=pickle.load(f)
            for i in s:
                if i[0]==r:
                    print(i)
                    found=1
                    break
    except Exception:
        f.close()
    if found==0:
        print("Sorry Details Not Found..")



def update():
    f=open("ccmd.dat","rb+")

    r=int(input("Enter ID To Search For Details : "))
    f.seek(0)
    try:
        while True:
            rpos=f.tell()
            s=pickle.load(f)
            for i in s:
                if i[0]==r:
                    i[4]=int(input("Update Charges : "))
                    f.seek(rpos)
                    pickle.dump(s,f)
                    break
    except Exception:
        f.close()


def delete():
    f=open("ccmd.dat","rb")
    s=pickle.load(f)
    f.close()

    r=int(input("Enter ID Whose Detail You Want To Delete : "))
    f=open("ccmd.dat","wb")
    reclst=[]
    for i in s:
        if i[0]==r:
            continue
        reclst.append(i)
    pickle.dump(reclst,f)
    f.close()





def mainmenu():
    print("----------------------------------------------")
    print("1. Insert Customer Details..")
    print("2. View Customer Details..")
    print("3. Add On Customer Details..")
    print("4. Search Customer Details..")
    print("5. Update Customer Details..")
    print("6. Delete Customer Details..")
    print("7. Quit..")
    print("----------------------------------------------")
while True:
    mainmenu()
    ch=int(input("Enter Your Choice(1-7) : "))
    if ch==1:
        write()
    elif ch==2:
        read()
    elif ch==3:
        append()
    elif ch==4:
        search()
    elif ch==5:
        update()
    elif ch==6:
        delete()
    elif ch==7:
        break


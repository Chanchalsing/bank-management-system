print("_"*40)
print("        BANK MANAGEMENT SYSTEM      ")
print("_"*40)
l1=['accountno.','name','address','phone','govtid','acctype','amount']
l2=[]
mydic={}

def new():
    global mydic
    a=int(input("Enter the account number : "))
    b=input("Enter the Name ")
    c=input("Enter the Address ")
    d=int(input("Enter the phone number "))
    e=input("Enter the Govt. Id ")
    f=input("Enter the Acc. Type ")
    g=int(input("Enter the amount "))
    l2.append(a)
    l2.append(b)
    l2.append(c)
    l2.append(d)
    l2.append(e)
    l2.append(f)
    l2.append(g)
    key_pair= zip(l1,l2)
    mydic=dict(key_pair)
    print("Account Created ")

def Ex():
    global mydic
    def check():
        print(mydic['amount'])

    def withdraw():
        wit=int(input("Enter amount to withdraw: "))

        mi=mydic['amount']-wit
        mydic['amount']=mi
        print("-"*40)
        print("Withdraw Successful ")
        print("Available Balance :",mi)
        print("-"*40)

    def Deposit():
        dep=int(input("Enter amount to Deposit: "))
        am=mydic['amount']+dep
        mydic['amount']=am
        print("-"*40)
        print(" Deposit Successful ")
        print("Available Balance :",am)
        print("-"*40)
        
    acc=int(input("Enter your account number : "))
    if acc in mydic.values() :
        print("Record Found")
        print("1. Check Balance ")
        print("2. Withdraw ")
        print("3. Deposit ")
        ch=int(input("Enter the choice : "))
        if ch==1:
            check()
        elif ch==2:
            withdraw()
        elif ch==3:
            Deposit()
        else:
            print("Wrong Choice ")
      
    else:
        print("Record Not found")
    




while(True):
    print("1. New Customer ")
    print("2. Existing Customer ")
    print("3. Exit ")
    choice=int(input("Enter choice "))
    if choice==1:
        new()
    elif choice==2:
        Ex()
    elif choice==3:
        break
    else:
        print("wrong input")
    
    
import threading

def evenlist(x):
    sum=0
    for i in range(len(x)):
        if x[i]%2==0:
            sum=sum+x[i]
    print("The addition of all even elements from input list: ",sum)

def oddlist(x):
    sum=0
    for i in range(len(x)):
        if x[i]%2!=0:
            sum=sum+x[i]
    print("The addition of all odd elements from input list: ",sum)

def main():
    no=int(input("Enter number of elements is the List: "))
    nlist=[]
    for i in range(no):
        a=int(input("Enter a number: "))
        nlist.append(a)
    thread1=threading.Thread(target=evenlist,args=(nlist,))
    thread2=threading.Thread(target=oddlist,args=(nlist,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("exit from main")

if __name__=="__main__":
    main()

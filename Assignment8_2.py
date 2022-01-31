import threading

def evenfactor(x):

    sum=0
    for i in range(1,x):
        if x%i==0:
            if i%2==0:
                sum=sum+i
    print("Sum of even factors is ",sum)

def oddfactor(y):

    sum=0
    for i in range(1,y):
        if y%i==0:
            if i%2!=0:
                sum=sum+i
    print("Sum of odd factors is ",sum)

def main():
    No=int(input("Enter a number: "))
    thread1=threading.Thread(target=evenfactor,args=(No,))
    thread2=threading.Thread(target=oddfactor,args=(No,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("exit from main")

if __name__=="__main__":
    main()

import threading

def even(x):
    for i in range(x):
        if i%2==0:
            print(i)

def odd(x):
    for i in range(x):
        if i%2!=0:
            print(i)

def main():
    x=20
    thread1=threading.Thread(target=even,args=(20,))
    thread2=threading.Thread(target=odd,args=(20,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

if __name__=="__main__":
    main()

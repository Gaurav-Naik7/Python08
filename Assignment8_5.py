import threading
No=50
def Counter(fun,lock):
    fun(lock)

def thread1(lock):
    lock.acquire()
    global No
    for i in range(1,No+1):
        print(i)
    lock.release()


def thread2(lock):
    lock.acquire()
    global No
    while (No>0):
        print(No)
        No=No-1
    lock.release()

def main():

    lock=threading.Lock()

    t1=threading.Thread(target=Counter,args=(thread1,lock,))
    t2=threading.Thread(target=Counter,args=(thread2,lock,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("exit from main")

if __name__=="__main__":
    main()

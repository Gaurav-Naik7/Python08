import threading

def small(input_str):

    sum=0
    for i in range(len(input_str)):
        if input_str[i].islower():
            sum=sum+1
    print("Number of small characters: ",sum)

def capital(input_str):

    sum=0
    for i in range(len(input_str)):
        if input_str[i].isupper():
            sum=sum+1
    print("Number of capital characters: ",sum)

def digit(input_str):

    sum=0
    for i in range(len(input_str)):
        if input_str[i].isdigit():
            sum=sum+1
    print("Number of digits: ",sum)

def main():
    str=input("Enter a string ")
    thread1=threading.Thread(target=small,args=(str,))
    thread2=threading.Thread(target=capital,args=(str,))
    thread3=threading.Thread(target=digit,args=(str,))
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()

    print("exit from main")

if __name__=="__main__":
    main()

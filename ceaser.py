s=input("enter text : ")
n=int(input("enter key : "))
def encrypt(s,n):
    res=""
    for i in s:
        if i.isupper():
            a=ord(i)-64+n
            k=a%26
            t=64+k
            if k==0:
                t=64+26

        elif i.islower:
            a=ord(i)-96+n
            k=a%26
            t=96+k
            if k==0:
                t=96+26
        c=chr(t)
        res=res+c
    return res
def decrypt(s,n):
    res=""
    n=n%26
    for i in s:
        if i.isupper():
            a=ord(i)-64-n
            if a<0:
                a=a+26
            t=64+a
            if a==0:
                t=64+26
        else:
            a=ord(i)-96-n
            if a<0:
                a=a+26
            t=96+a
            if a==0:
                t=96+26
        c=chr(t)
        res=res+c
    print("decrpted text = ",res)
z=(encrypt(s,n))
print("encrpted text = ",z)
decrypt(z,n)

    
    

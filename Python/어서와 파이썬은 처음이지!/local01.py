# 실행결과 예측
def sub(mylist):
    mylist = [1,2,3,4] # 원본 전역 변수 mylist와는 별개의 리스트 생성
    print("함수 내부에서의 mlist:",mylist)
    return

mylist = [10, 20, 30, 40]
sub(mylist)
print("함수 외부에서의 mylist:",mylist)
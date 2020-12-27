print("start!")

while True:
    try:
        print("try 구문이 실행되었습니다.")
        break
        print("try 구문의 break 키워드 뒤")
    except:
        print("except 구문이 실행되었습니다.")
    finally:
        print("finally 구문 실행")
    print("while 반복문의 마지막 줄")
    
print("finish")
# 함수 선언
def write_text_file(filename, text):
    # try except
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close() # 무조건 실행

# 함수 호출
write_text_file("text.txt","안녕하세요!")
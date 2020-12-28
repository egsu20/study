class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("##### 오류 정보 #####")
        print("message :", self.message)
        print("value :",self.value)

try:
    raise CustomException("이유없음", 276)
except CustomException as e:
    e.print()
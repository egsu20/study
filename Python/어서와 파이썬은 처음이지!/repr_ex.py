class Book:
    def __init__(self, title, isbn):
        self.__title = title
        self.__isbn = isbn

    # 객체의 정보를 한 줄의 문자열로 만들어서 반환
    def __repr__(self):
        return "ISBN : " + self.__isbn +"; Title : "+self.__title

book = Book("The Python Tutorial", "0123456")
print(book)

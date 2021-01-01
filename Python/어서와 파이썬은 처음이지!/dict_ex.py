# 공백 딕셔너리
d = {}

# 딕셔너리의 항목 접근
contacts = {
    "kim" : "01012345678",
    "park" : "0101234567",
    "lee" : "01012356645"
}
print(contacts["park"])
print(contacts.get("park"))

# 키가 없을 때 디폴트값
print(contacts.get("choi","010114"))

# 항목 추가
contacts["choi"] = "010567891232"
print(contacts)

# 항목 삭제
contacts.pop("kim")
print(contacts)

del contacts["choi"]
print(contacts)

# 항목 순회
scores = {"korean" : 80, "math" : 90, "english":80}
for item in scores.items(): # items()를 생략하면 키만 출력됨
    print(item)

# 딕셔너리 함축
triples = {x:x*x*x for x in range(6)}
print(triples)

# 정렬
dic = {"bags" : 1 , "books":5, "bottles" : 4, "coins":7, "cups":2,"pens":3}
print(dic)
print(list(dic)) # 딕셔너리를 리스트로 변경

print(list(sorted(dic)))
print(sorted(dic.values()))

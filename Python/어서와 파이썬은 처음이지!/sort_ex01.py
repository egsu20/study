print(sorted([4,2,3,5,1]))

# 리스트의 메소드 sort()
list_a = [4,2,3,1,6,7]
list_a.sort()
print(list_a)

students = [
    ('hong', 3.8, 20160302),
    ('kim', 4.1, 20160303),
    ('choi', 3.2, 20160301)
]

# key 매개변수 사용
# student[2]는 학번을 뜻함. 학번을 기준으로 정렬
# student 요소를 받아 student[2] 반환
print(sorted(students, key=lambda student:student[2]))

# reverse 매개변수로 오름차순, 내림차순 정렬
print(sorted(students, key=lambda student:student[2], reverse=True))

# 정렬의 안정성 : 키 값이 동일하다면 정렬 후에도
#                 원래의 순서가 유지되는 것을 보장
# ex
data = [(1, 100), (1,200), (4, 300), (3, 400), (1, 500)]
# 첫번째 요소를 기준으로 정렬
print(sorted(data, key=lambda item:item[0]))

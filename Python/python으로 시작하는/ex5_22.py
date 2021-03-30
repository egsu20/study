student = {'현준':1234, '민지':2345}

print('현준' in student)
print('현준' not in student)

print(student.get('민지'))
print(student.get('민자'))

print(student.keys())
print(student.values())
print(student.items())

print()
newstd={'승민':3456, '유진':4567}
print('원본 :', student)
student.update(newstd)
print('업데이트 :', student)


person = {'name':'준혁', 'age':21, 'height':172.5}
print('이름:{0[name]}, 나이:{0[age]}, 키:{0[height]}'.format(person))

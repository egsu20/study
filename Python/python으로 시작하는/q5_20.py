age = {'동혁':21, '민지':19, '준혁':23}

print('동혁의 나이 :', age['동혁']) # age.get('동혁;)
age['민지'] += 1
print(age.get('민지'))
print()

student = {'GilDong':2345, 'SunSin':1234, 'SeJong':3456}
for name in student.keys(): # .keys() 생략가
    print(name, ':',student[name])
print()

for name, num in student.items():
    print(name, ':',student[name])

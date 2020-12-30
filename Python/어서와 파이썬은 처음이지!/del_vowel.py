s = input("문자열을 입력하시오 : ")
vowels = "aeiouAEIOU"
result = ""

for char in s:
    if char not in vowels:
        result += char

print(result)

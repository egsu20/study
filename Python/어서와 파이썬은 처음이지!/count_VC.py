string = input("문자열 입력 : ")
word = string.lower()

vowels = 0
consonants = 0

if word.isalpha() and len(word) > 0:
    for char in word:
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print("모음의 개수 :", vowels)
print("자음의 개수 :", consonants)

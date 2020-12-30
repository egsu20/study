s = input("문자열 입력 : ")
word = s.lower()

if len(word) > 0 and word.isalpha:
    for i in range(len(word)):
        if word[i] in 'aeiou':
            print(i)

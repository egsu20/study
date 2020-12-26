dictionary ={
    "name":"7D mango",
    "type":"dang",
    "ingredient":["mango", "sugar", "meta","chija"],
    "origin":"fili"
}

string = input("접근하고자 하는 키:")

if string in dictionary:
    print(dictionary[string])
else:
    print("not in key")

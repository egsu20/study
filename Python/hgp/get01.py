dictionary ={
    "name":"7D mango",
    "type":"dang",
    "ingredient":["mango", "sugar", "meta","chija"],
    "origin":"fili"
} 

value = dictionary.get("not in key")
print(value)

if value == None:
    print("is none")
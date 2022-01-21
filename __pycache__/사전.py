# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3]) 
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(5)) #5에 값이 없을때  get이용하면 none , 대괄호 이용하면 오류
# print(cabinet.get(5,"사용 가능"))

# print(3 in cabinet) #TRUE
# print(5 in cabinet) #False

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새손님
print(cabinet)
cabinet["c-20"]= "조세호"
cabinet["A-3"]= "김종국"
print(cabinet)

#간 손님
del cabinet["A-3"]
print (cabinet)

#key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목용탕 종료
cabinet.clear()
print(cabinet)
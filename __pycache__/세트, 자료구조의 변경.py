# 집합(set)
# 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# #교집합 
# print(java & python)
# print(java.intersection(python))

# # 합집합 (둘중 아무거나 하나)
# print( java | python)
# print(java.union(python))

# #차집합 ( java만 가능)
# print(java-python)
# print(java.difference(python))

# #python 할 줄 아는 사람 늘어남
# python.add("김태호")
# print(python)

# #java를 잊음
# java.remove("김태호")
# print(java)
#//////////////////////////////////////////////////////////////////////////
#자료구조의 변겅
#커피숍

# menu ={"커피", "우유", "주스"}
# print(menu, type(menu))

# menu= list(menu)
# print(menu, type(menu))

#////////////////////////////////////////////////////////////
#QUIZ

# from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(lst)
# shuffle(lst)
# print(lst)
# chicken = (sample(lst,1))
# print(chicken)
# lst.remove(chicken)
# print(lst)
# # coffe = (sample(lst,3))

# from random import*
# users = range(1,21)
# # print(type(users))
# users = list(users)

# print(users)
# shuffle(users)

# winners = sample(users, 4)

# print("--당첨자 발표")
# print(" 치킨 당첨자: {0}".format(winners[0]))
# print(" 커피 당첨자: {0}".format(winners[1:]))
# print(" --축하합니다.--")

#///////////////////////////////////////////
from random import*
users = range(1,20)
# print(type(users))
users = list(users)
users.append("현지")
print(users)
shuffle(users)

winners = sample(users, 1)

print("--당첨자 발표")
print(" 고기 당첨자: {0}".format(winners[0]))
print(" --축하합니다.--")
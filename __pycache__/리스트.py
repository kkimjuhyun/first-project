# 순서를 가진 객체

# 지하철 칸별로 10명 20명 30명

# subway = [10,20,30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# print(subway.index("조세호")) #조세호 위치 찾기 index

# subway.append("하하") #맨뒤에 하하 추가 append
# print(subway)

# subway.insert(1,"정형돈") #1번 자리에 정형돈 추가 insert
# print(subway)

# print(subway.pop()) #맨뒤 한명을 꺼냄
# print(subway)

# # print(subway.pop()) #맨뒤 한명을 꺼냄
# # print(subway)

# # print(subway.pop()) #맨뒤 한명을 꺼냄
# # print(subway)

# #같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

#정렬도 가능
num_list= [5,4,3,2,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
num_list = [ 5,2,4,3,1]
mix_lsit = ["조세호", 20 , True]
print(mix_lsit)

num_list.extend(mix_lsit)
print(num_list)
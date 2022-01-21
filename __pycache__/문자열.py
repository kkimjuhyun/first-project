# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """ #줄바꿈
# 나는 소년이고 
# 파이썬은 쉬워요
# """

# print(sentence3)
#//////////////////////////////////////////////////////////////////////////////

# jumin = "991011-1234567"

# print("성별 :" + jumin[7])
# print("연: " + jumin[0:2]) #0~2직전 까지 즉 0,1번째에 있는 값
# print("월: "+ jumin[2:4])
# print("일: "+ jumin[4:6])

# print("생년월일: "+ jumin[0:6]) # [0:6]=[:6]
# print("뒤 7자리:"+ jumin[7:15]) #[7:] 7부터 끝까지
# print("뒤 7자리 (뒤에부터): "  + jumin[-7:]) #맨 뒤에부터 7번째 까지
#//////////////////////////////////////////////////////////////////////////////

#문자열 처리함수

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper()) #0번째 값이 대문자이면 t  소문자이면 f
# print(len(python)) #길이
# print(python.replace("Python", "JAVA"))

# index = python.index("n") #python 변수에  n이라는 글자가 몇번째 있는지 확인후 index  함수에 저장
# print(index)
# index = python.index("n", index + 1) #다음 위치에 있는 n
# print(index)

# print(python.find("JAVA")) #find에서 없을 때는  -1반환
# # print(python.index("JAVA")) #index에서 없을 때는 error 뒤에 더이상 실행x

# print(python.count("n"))
#//////////////////////////////////////////////////////////////////////////////

#문자열 포맷

# print("a" + "b")
# print("a","b") 

#방법 1
# print("나는 %d살입니다." %20) #정수
# print("나는 %s를 좋아합니다." %"python") #문자열
# print("Apple 은  %c로 시작해요 " %"A") #문자
# print("나는 %s살입니다." %20) # %s는 다가능
# print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))

#방법 2
# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간")) #중괄호 안에 숫자에 따라 순서 바뀔 수 있다.

#방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age=20,color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age=20))

#방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.") #쓰면 변수에 저장된 값을 가져다 사용가능

#/////////////////////////////////////////////////////////////////////////////

#탈출문자

# print("백문이 불여일견 \n백견이 불여일타")  \n: 줄바꿈
# print('저는 "나도코딩" 입니다.')   #문장속 큰따옴표 사용방법
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.") # \" \: 문장 내에서 따옴표

#\\ : 문장 내에서 \있을때
# # print("C:\\Users\\kimju\\Desktop\\PYTHONWORKSPACE>")

# # \r: 커서를 맨 앞으로 이동
# print("Red Apple\rpine")

# # \b: 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")

# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# site = "http://naver.com"
# step1=  site[7:]
# step2= step1[:-4]
# step3= step2[0:3]

# password= step3+ str(len(step2)) + str(step2.count("e")) +"!"

# print(password)


url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")] # my_str에 .이 어디있는 지 확인후 그 앞에 까지 
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0} 의 비밀번호는 {1} 입니다.".format(url, password)).
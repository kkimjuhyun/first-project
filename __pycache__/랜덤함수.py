from random import*

# print(random()) #0.0~1.0미만의 값 생성
# print(random() *10) #0.0~10.0 미만의 임의의 값 생성

# print(int(random()*10)) #정수형
# print(int(random() *10 +1))
# print(int(random()* 45)+1) 

# print(randrange(1,46)) #1~46미만의 임의의 값 생성

# print(randint(1, 45)) #1~45값



from random import *
x= randint( 4,28 )
print (x)
print( "오프라인 스터디 모임 날짜는 매월 "+ str(x) + "일로 선정되었습니다.") 
# print("Python", "Java",  sep=" , ", end= "?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python,", "Java", file=sys.stdout) #표준출력
# print("Python,", "Java", file=sys.stderr)

#시험성적
# scores = {"수학":0, "영어":50, "코딩":100} #dictionary key value
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #8칸 확보한 후 왼쪽정렬, 4칸 확보한 후 오른쪽 정렬

#은행 대기순번표
#001,002,,,,
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) #3크기를 확보한 후 값이 없는 공간에는 0으로 채움

# answer = input("아무 값이나 입력하세요 :")
# print("입력하신 값은 "+ answer + "입니다.")

# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(10000000000))
# # 3자리 마다 콤마를 찍어주기, +-부호 붙이기
# print("{0:+,}".format(10000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고. 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^로 채우기
# print("{0:^<+30,}".format(100000000000))
# # 소수점 출력
# print("{0:.2f}".format(5/3))

#////////////////////////////////////////////////////////////////////////////////////////////////////////
#파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") #파일이름, 목적 write, utf8 정의 한글정보 위함
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") #a는 덮어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #줄별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()
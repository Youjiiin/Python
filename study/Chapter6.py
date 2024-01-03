# 조건문
weather = "미세먼지"

if weather == "비": # 대입 연산자(=)가 아닌 비교 연산자(==) 사용
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("그냥 나가세요")


weather = input("오늘 날씨는 어때요? ")
print(weather)

temp = int(input("오늘 기온은 어때요? ")) # 입력값을 정수형으로 형변환

if 30 <= temp: # 30도 이상이면
    print("너무 더워요. 외출을 자제하세요.")
elif 10 <= temp and temp < 30: # 10도 이상 30도 미만이면
    print("활동하기 좋은 날씨예요.")
elif 0 <= temp and temp < 10: # 0도 이상 10도 미만이면
    print("외투를 챙기세요.")
else: # 그 외의 모든 경우(0도 미만이면)
    print("너무 추워요. 나가지 마세요.")


# 반복문
# for
for waiting_no in [1, 2, 3, 4, 5]:
    print("대기번호 : {0}".format(waiting_no)) # {0} 위치에 waiting_no의 값이 들어감

for waiting_no in range(5): # ← 0부터 5 직전까지(0~4)
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6, 2): # ← 1부터 6 직전까지(1~5)에서 2씩 간격 주기
    print("대기번호 : {0}".format(waiting_no))

students = [1, 2, 3, 4, 5]
print(students)

# 한 줄 for 문으로 각 항목에 100 더하기
students = [i + 100 for i in students]
print(students)

# while
customer = "토르" # 손님 닉네임
index = 5 # 초깃값, 부르는 횟수 최대 5번

while index >= 1: # 부르는 횟수가 1 이상일 때만 실행
    print("{} 님, 커피가 준비됐습니다.".format(customer))
    index -= 1 # 횟수 1회 차감
    print("{}번 남았어요.".format(index))
    if index == 0: # 5번 모두 불렀다면
        print("커피를 폐기 처분합니다.")

absent = [2, 5] # 결석한 학생 출석번호 
no_book = [7] # 책을 가져오지 않은 학생 출석번호
for student in range(1, 11): # 출석번호 1~10번
    if student in absent: # 결석한 학생이면
        continue # 다음 학생으로 넘어가기
    elif student in no_book: # 책을 가져오지 않으면 바로 수업 종료
        print("오늘 수업은 여기까지. {0}번 학생은 교무실로 따라와요.".format(student))
        break # 반복문 탈출
    print("{0}번 학생, 책을 읽어 보세요.".format(student))

###################################3

from random import *

cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if time <= 15 :
        print("[0] {0}번째 손님 (소요시간: {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i, time))

print("총 탑승객 : {0}명".format(cnt))
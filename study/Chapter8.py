import sys
# 구분자
print("파이썬", "자바")
print("파이썬", "자바", sep=",") # 값을 쉼표로 구분

print("파이썬", "자바", sep=", ", end="? ")
print("무엇이 더 재미있을까요?")

print("파이썬", "자바", file=sys.stdout)
print("파이썬", "자바", file=sys.stderr)

scores = {"수학": 0, "영어": 50, "코딩": 100}

# ljust / rjust 정렬
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# zfill() : 빈칸 0으로 채우기
for num in range(1, 21): # 1~20의 숫자
    print("대기번호 : " + str(num).zfill(3))

print("{0}".format(500))
# 빈칸으로 두기, 오른쪽 정렬, 공간 10칸 확보
print("{0: >10}".format(500))

print("{0: >+10}".format(500))
print("{0: >+10}".format(-500)) # 음수일 때
print("{0:_<10}".format(500)) # 빈칸을 _로 채우기, 왼쪽 정렬, 공간 10칸 확보

print("{0:,}".format(100000000000)) # 3자리마다 쉼표 찍기
print("{0:+,}".format(100000000000)) # + 기호 붙이기, 3자리마다 쉼표 찍기
print("{0:+,}".format(-100000000000)) # 음수일 때, 3자리마다 쉼표 찍기

# 빈칸을 ^로 채우기, 왼쪽 정렬, + 기호 붙이기, 공간 30칸 확보, 3자리마다 쉼표 찍기
print("{0:^<+30,}".format(100000000000))

print("{0}".format(5 / 3))
print("{0:f}".format(5 / 3))
print("{0:.2f}".format(5 / 3))

# 파일 열고 닫기
# score.txt 파일을 쓰기 모드로 열기
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file) # score.txt 파일에 내용 쓰기
print("영어 : 50", file=score_file) # score.txt 파일에 내용 쓰기
score_file.close() # score.txt 파일 닫기

# score.txt 파일에 이어 쓰기 모드로 열기
score_file = open("score.txt", "a", encoding="utf8")
# # write() 함수는 줄 바꿈이 없으므로 \n 추가
score_file.write("과학 : 80\n")
score_file.write("코딩 : 100\n")
score_file.close()

# score.txt 파일을 읽기 모드로 열기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # 파일 전체 읽어 오기
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 한 줄씩 읽어 오고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # end 값을 설정해 줄 바꿈 중복 수행 방지
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")

while True:
    line = score_file.readline()
    if not line: # 더 이상 읽어 올 내용이 없을 때
        break # 반복문 탈출
    print(line, end="") # 읽어 온 내용 출력
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")

lines = score_file.readlines() # 파일에서 모든 줄을 읽어 와 리스트 형태로 저장
for line in lines: # lines에 내용이 있을 때까지
    print(line, end="") # 읽어 온 내용 출력

score_file.close()

# pickle
import pickle # pickle 모듈 가져다 쓰기
 
profile_file = open("profile.pickle", "wb") # 바이너리 형태로 저장
profile_file = open("profile.pickle", "wb") # 바이너리 형태로 저장
profile = {"이름": "스누피", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 데이터를 파일에 저장
profile_file.close() # 파일 닫기

profile_file = open("profile.pickle", "rb") # 읽어 올 때도 바이너리 형태 명시
profile = pickle.load(profile_file) # 파일에 있는 정보를 불러와서 profile에 저장
 
print(profile)
profile_file.close()

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file: # 새로운 파일 생성
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
jNum = "123456-1234567"
print("성별: " + jNum[7])

# 슬라이싱
print("앞자리: " + jNum[0:6]) #시작인덱스:종료인덱스 직전까지
# 변수명[:종료 인덱스]: 처음부터 종료 인덱스 직전까지 슬라이싱
# 변수명[시작 인덱스:]: 시작 인덱스부터 끝까지 슬라이싱
# 변수명[:]: 처음부터 끝까지 슬라이싱
print("주민등록번호 뒷자리(뒤에서부터) : " + jNum[-7:])
# 음수 인덱스는 -14 -13 ... -2 -1 로 배정

# 문자열 처리하기
# lower() : 소문자 변환
# upper() : 대문자 변환

# islower() : 소문자인지 확인
print("abc".islower())
print("AbC".isupper())
# isupper() : 대문자인지 확인

# replace() : 문자열 바꾸기
print("abc".replace("a", ""))

# index() : 찾는 문자열의 인덱스 (없으면 오류)
# index(찾는 문자, 시작 인덱스, 종료 인덱스)
print("abcdefaa".index("b"))

# find() : 찾는 문자열의 인덱스 (없으면 -1) 
# find(찾는 문자, 시작 인덱스, 종료 인덱스)
print("abcadefa".find("d", 0, 3))

# count() : 문자열이 나온 횟수
print("aaaaaaabc".count("a"))

# 문자열의 길이
a = "abcc"
print(len(a))

# 문자열 포매팅 : 원하는 위치에 특정한 값 넣기
# %d %f %c %s
print("나는 %d살입니다." % 20)
print("나는 %s살입니다." % 20) # %s로도 정숫값 표현 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 값이 여럿일 때

#format() : print("문자열{인덱스}문자열{인덱스} ...".format(값1, 값2, ...))
print("나는 {}살입니다.".format(20))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

#f 문자열 사용하기 : print(f"문자열{변수명1}문자열{변수명2}...")
age = 21
color = "초록"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
print("123\n123")

# \' \"
print("\"123\"")

#\
print("C:\\User\\Python")

#\r : 맨 앞으로 이동 - 일부 환경에서 적용안됨
print("Red Apple\rPine")

# 앞글자 없애기 - 일부 환경에서 적용안됨
print("Redd\bApple")

# tab
print("Red\tApple")
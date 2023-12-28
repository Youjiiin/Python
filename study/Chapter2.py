# 변수 선언하기
# 따로 자료형은 작성하지 않고 값을 입력할 때 자료형에 맞게 입력해주면 된다.
age = 25
name = "유진"

# 숫자 자료형을 string과 이이서 print할때는 str로 형변환을 해줘야 한다.
print("이름: " + name + " 나이: " + str(age))
print(age)

# ,로 이어줄 수 있다. 대신, ','를 넣으면 띄어쓰기가 적용된다.
print("이름: ", name, " 나이: ", age)

# 형변환 (int -> float)
print(float(age))

# 형변환 시 타입 확인
print(type(3)) # 정수(int)
print(type("3")) # 문자열(str)
print(type(3.5)) # 실수(float)
print(type(str(3))) # 정수(int)를 문자열(str)로 형변환


# 연습문제
# station = "사당"
# station = "신도림"
station = "인천공항"

print(station + "행 열차가 들어오고 있습니다.")
from random import *

# 리스트
subway = [10, 20, 30]
print(subway)
print(subway.index(20))

# 리스트 요소 추가
subway.append(40)
print(subway)

# 특정 인덱스에 추가
subway.insert(1, 30)
print(subway)

# 리스트 요소 제거
subway.pop()
print(subway)

# 요소 개수 확인
print(subway.count(30))

# 전체 제거
subway.clear()
print(subway)

num = [2, 5, 3, 1, 4]

# 오름차순 정렬
num.sort()
print(num)

# 오름차순 정렬 - 새로운 리스트 생성
num_list = sorted(num)
print(num_list)

# 내림차순 정렬
num.sort(reverse=True)
print(num)

# 순서뒤집기
num.reverse()
print(num)

# 리스트 확장
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# 딕셔너리
cabinet = {3: "푸", 100: "피글렛"}

print(cabinet[3]) # key 3에 해당하는 value
print(cabinet.get(3)) # key 3에 해당하는 value
print(cabinet[100]) # key 100에 해당하는 value
print(cabinet.get(5, "사용 가능")) # key에 해당하는 값이 없으면 기본값을 사용하게 함 - get(key, default=None)

# key가 있는지 확인
print(3 in cabinet)
print(5 in cabinet)

# in 연산자 - 안에 글자가 포함되어있는지 
print("곰" in "곰돌이")
print("돌이"  in "곰돌이")
print("푸" in "곰돌이")

# value값 변경
print(cabinet)
cabinet[3] = "티거" # key에 해당하는 값이 있을 때 -> 값 변경
cabinet[20] = "이요르" # key에 해당하는 값이 없을 때 -> 값 추가
print(cabinet)

# 값 제거
del cabinet[3]
print(cabinet)

print(cabinet.keys()) # key만 출력
print(cabinet.values()) # value만 출력
print(cabinet.items()) # key, value 한 쌍으로 출력
cabinet.clear() # 값 전체 삭제
print(cabinet)

# 튜플 : 리스트 읽기 전용
menu = ("돈가스", "치즈돈가스")
print(menu[0])
print(menu[1])

name = "피글렛"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("피글렛", 20, "코딩")
print(name, age, hobby)

(departure, arrival) = ("김포", "제주")
print(departure, ">", arrival) # 김포 > 제주
(departure, arrival) = (arrival, departure)
print(departure, ">", arrival) # 제주 > 김포

# 세트 : 중복을 허용하지 않고, 데이터 순서도 보장하지 않는다.
my_set = {1, 2, 3, 3, 3}
print(my_set)

empty_set = set() # 빈 세트 생성하기

java = {"푸", "피글렛", "티거"} # 자바 개발자 세트
python = set(["푸", "이요르"]) # 파이썬 개발자 세트

# 교집합(자바와 파이썬을 모두 다룰 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합(자바 또는 파이썬을 다룰 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합(자바는 할 수 있지만 파이썬은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# 파이썬 개발자 추가(기존 개발자: 푸, 이요르)
python.add("피글렛")
print(python)

# 자바 개발자 삭제(기존 개발자: 푸, 피글렛, 티거)
java.remove("피글렛")
print(java)

# 타입 변환
menu = {"커피", "우유", "주스"}
print(menu)
print(type(menu))

menu = list(menu) # 리스트로 변환
print(menu, type(menu))

menu = tuple(menu) # 튜플로 변환
print(menu, type(menu))

menu = set(menu) # 세트로 변환
print(menu, type(menu))

####################################

p = range(1, 21)
person = list(p)
shuffle(person)
get = sample(person, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(get[0]))
print("커피 당첨자 : {}".format(get[1:]))
# print("치킨 당첨자 :", get[0])
# print("커피 당첨자 :", get[1:])
print("-- 축하합니다! --")

####################################

subject = ['자료구조', '알고리즘', '운영체제', '자료구조']
subject = set(subject)
print("신청한 과목은 다음과 같습니다.")
subject = list(subject)
print(subject)
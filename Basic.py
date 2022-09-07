
###################################
## 4-1.문자열                     ##
###################################

# 기본 개념 Skip 



###################################
## 4-2.슬라이싱                   ##
###################################

# jumin ='860217-1498280'
# print('성별'+jumin[7])  # 7번째 있는 위치 값을 가져 옴
# print('성별'+jumin[0:9])  # 0번째~9번째 까지 값을 가져 옴 

# print(jumin[2:4])
# print(jumin[:6])
# print(jumin[7:])
# print(jumin[-7:])



###################################
## 4-3.문자열 처리 함수           ##  
###################################

# 변수명.upper
# 변수명.lower
# len(변수명)
# 변수명.count("찾을문자")
# 변수명.isupper
# 변수명.islower
# 변수명.find("찾을문자")
# 변수명.replace("바꿀문자", "변경 후 문자")
# 변수명.index ("찾을문자") 그리고 print(index) 해줘야 함 
# 변수명.index ("찾을문자", index + 1 ) 찾은거 그 뒷자리 



###################################
## 4-4.문자열 포멧                ##   
###################################

# # 방법 1. %d 정수(Integer) %s 문자(String)  %c 한문자(Character) 
# print("나는 %d살입니다." % 20)
# print("나는 %s살입니다." % "스무살")
# print("나는 %c살입니다." % "A")
# print("나는 %s살이고 %s에 삽니다." %("스무살", "서울"))  # 2개 이상 쓸 때는 괄호로 씌워줘야 함

# #방법 2. {}활용, 뒤에 .format(넣을 값)
# print("나는{}에 삽니다" .format("서울"))
# print("나는{0}살이고 {1}에 삽니다." .format("스무", "서울")) # 순서 바꿀꺼면 0,1 등 순서 앞에서 넣어야 함 
# print("나는{age}살이고 {city}에 삽니다." .format(age = "서른", city = "대구")) # 순서 바꿀꺼면 0,1 등 순서 앞에서 넣어야 함 

# #방법3 변수를 밖에서 선언하고, 안에서 f 넣고 {변수명} 괄호 사용  
# age = "사십"
# city = "대전"
# print(f"나는{age}살이고 {city}에 삽니다.") # 순서 바꿀꺼면 0,1 등 순서 앞에서 넣어야 함 



###################################
## 4-5.탈출 문자                  ##   
###################################

# \\ 문장내에서 역슬러쉬 1개 쓸 때 사용 
# \n 줄바꿈(next line)  
# \r 커서 맨앞으로 이동해서 남은거 작성   
# \b 백스페이스(한글자 삭제)
# \t 탭

# print("Red \\Apple")  #출력 결과 : Red \Apple 
# print("Red App\rle")  #출력 결과 : led App 
# print("Red App\ble")  #출력 결과 : Red Aple
# print("Red App\tle")  #출력 결과 : Red App le



###################################
## 5-1.리스트 []                 ##   
###################################

# # 특징 : []괄호 씀, 다양한자료형 사용가능, "리스트 확장 가능"  
# subway =["박주호", "이효선", "김다은"]
# print(subway.count("이효선"))  
# print(subway.index("이효선"))  
# print(subway.append("김민서"))  
# print(subway.insert(0, "댕댕이")) #위치 지정해서 append 
# print(subway)
# print(subway.pop())
# subway.sort() #정렬기능
## subway.clear() #리스트 전체 삭제

# subway2 = ["1호선", 7114, True]
# subway.extend(subway2) # 리스트 확장 가능(다른리스트 extend)
# print(subway)



###################################
## 5-3.튜플 () = ()              ## 사전과 순서 바꿈 
###################################

# # 특징 : 리스트와 다르게 내용 변경 및 추가가 불가. 단, 속도가 빠름. 변수 변경 없는곳에 주로 사용
# menu = ("오라클", "자바", "C언어")
# print(menu[0])

# (name, age, hobby) = ("jh", "20", "코딩") # 이런 형태로 변수를 선언할 수 있음
# print(name, age, hobby)



###################################
## 5-2.사전 {키:값}               ##   
###################################

# # 특징 : 고상한 중괄호에 키:값을 이용 함  키를 부를 땐 [키] 씌워서 씀 
# cabinet ={3:"삼번 키", 1:"일번 키"}

# # 출력하기
# print(cabinet[3])  # 값없으면 오류 후 중단 됨
# print(cabinet.get(3)) #값이 없어도 오류 안나고 계속 진행 됨

# # 키 없으면 하드코딩 텍스트 보여주기
# print(cabinet.get(1, "키가 없으면 이 텍스트 보여 줌(하드코딩 개념)"))

# #사전 안에 키값 있는지 확인하기
# print( 3 in cabinet) # 있으면 True 없으면 Flase

# # 키 추가하기 
# cabinet["c-20"] = "세번째 키" # 키 추가하기
# cabinet["d-20"] = "네번째 키" 

# # 키 지우기 
# del cabinet["c-20"]

# # 키만 출력하기 
# print(cabinet.keys())

# # 값만 출력하기 
# print(cabinet.values())

# # 모두(키,값) 출력하기 
# print(cabinet.items())

# # 클리어하기 
# cabinet.clear() 



###################################
## 5-4.세트 {set}                ##
###################################

# # 특징 : 중복 안됨. 순서 없음 

# my_set = {1,2,3,4,5,5,5,5} #중복값 프린트 시 안보임 
# print(my_set)

# java = {"유재석", "김태호", "정준하"}
# python = set(["유재석", "박명수"]) #위랑 똑같이 이렇게도 정의 할 수 있음 

# # 교집합 출력하기 
# print(java & python)
# print(java.intersection(python)) # 위에랑 똑같은 형태인데 명령어만 다름

# # 합집합 출력하기
# print(java | python)
# print(java.union(python)) # 위에랑 똑같은 형태인데 명령어만 다름

# # 차집합 출력하기
# print(java - python)
# print(java.difference(python)) # 위에랑 똑같은 형태인데 명령어만 다름

# # 추가하기 
# python.add("김태호")

# # 삭제하기
# java.remove("김태호")



###################################
## 5-5.자료구조의 변경            ##
###################################

# 설명 : 리스트 = 튜플 = 세트  3개 유형이 서로 바꿀 수 있음 
# menu = ["커피", "우유", "주스"]

# menu = list(menu) #리스트로 바꾸기 
# menu = set(menu) #세트로 바꾸기 
# menu = tuple(menu) #튜플로 바꾸기 

# print(menu, type(menu)) #바뀐거 확인 



###################################
## 6-1.if                        ##
###################################

# weather = input("오늘 날씨는 어때요?")
# if weather =='비' or '눈': 
#  print("우산을 챙기세요")
# elif weather =='미세먼지' : 
#     print("마스크를 챙기세요")
# else : 
#     print("준비물 필요 없어요")

# temperture = int(input("온도는 몇도인가요?"))
# if temperture > 35 : 
#     print("밖에 나가지 마세요")
# elif temperture <= 35 and temperture >= 30 : 
#     print("밖이 더워요")
# elif temperture < 30 and temperture > 12 : 
#     print("외출하기 좋은 날씨에요")
# elif temperture <= 12  : 
#     print("추워요 외투를 챙기세요")
# elif temperture == -10 or temperture == 40 : 
#     print("위험한 날씨에요")
# else : print("온도를 다시 입력해주세요")



###################################
## 6-2.for 변수명 in [] :        ##
###################################

# for wait_no in [0,1,2,3,4,5] : 
#     print("대기번호{0}" .format(wait_no))

# for wait_no in range(5) :  # 0, 1, 2, 3, 4
#     print("대기번호{0}" .format(wait_no))

# for wait_no in range(1, 6) :  # 1부터 6 미만까지 보여줘라
#     print("대기번호{0}" .format(wait_no))

# starbucks = ["고객1", "고객2", "고객3", "고객4"]
# for customer in starbucks :  
#     print("{}의 커피가 나왔습니다." .format(customer))



###################################
## 6-5.한줄 for i in    변수명    ##     3/27 12:49~ 
###################################

#출석번호가 1 2 3 4, 앞에 100을 붙기기로 함 -> 101, 102, 103~

#숫자 더 붙이기
# student =[1,2, 3, 4, 5]
# print(student)
# student = [i+100 for i in student]
# print(student)

# #이름을 길이로 변환
# students = ["Iron amn", "Thor", "I am Groot"]
# students = [len(i) for i in students]
# print(students)

# #학생이름 대문자로 변환
# students = ["Iron amn", "Thor", "I am Groot"]
# students = [i.upper() for i in students]  #upper괄호 공백
# print(students)



###################################
## 6-3.while 조건 :              ##
###################################

# CUSTOMER ="JH"
# index = 5 
# while index >= 1 :
#     print("{0}손님, 커피가 나왔습니다. {1}번 남았어요" .format(CUSTOMER, index))
#     index -=1
#     if index == 0 : 
#         print("커피는 폐기처분 되었습니다.")
        
# CUSTOMER = "JH"
# Index  = 0
# while True  : 
#     print("{0}손님, 커피가 나왔습니다. Index {1} " .format(CUSTOMER, Index))
#     Index += 1 

# Customer = "jh"
# person = "Unknown"
# while person != Customer :  # 이 조건(이름이 틀림)을 만족할때까지 계속 반복 함
#     print("{0}손님, 커피가 나왔습니다." .format(Customer))
#     person = input("이름이 어떻게 되세요?")



###################################
## 6-4.Continue 와 Break         ##     3/27 12:36~ 
###################################

# 특징 : continue 조건 안맞아도 다음으로 넘어 감, break 실행 후 중단시킴 

# absent = [2, 5] # 결석
# no_book =[7]
# for student in range(1, 11) :   #1,2,3,4,5,6,7,8,10
#     if student in absent :
#         continue
#     elif student in no_book : 
#         print ("오늘 수업 여기까지. {0}은 교무실로 따라와" .format(student))
#         break
#     print("{0}, 책을 읽어봐" .format(student))
    
    

###################################
## 7-1.함수                      ##     3/27 12:57~ 
###################################

# 개념설명 : 믹서기와 같다. 입력값(과일)을 가지고 어떤일을 수행한 다음 결과물(주스)을 내놓는다 
# 사용목적 : 똑같은 내용을 반복해서 사용되는걸 한 뭉치로 묶어서 편하게 쓰기 위함

# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행할 문장2>
#     ...
#     return 결과값 
  
# 함수 이름 뒤 괄호 안의 매개변수(과일)는 이 함수에 입력으로 전달되는 값을 받는 변수이다. 
# 이렇게 함수를 정의한 다음 if, while, for문 등과 마찬가지로 함수에서 수행할 문장을 입력한다.

# 매개변수(parameter)와 인수(arguments)는 혼용해서 사용되는 헷갈리는 용어이므로 잘 기억하기. 
# 매개변수는 함수에 입력으로 전달된 값을 받는 변수를 의미하고 
# 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.

# def add(a, b):  # a, b는 매개변수
#     return a+b
# print(add(3, 4))  # 3, 4는 인수

# 입력값이 없는 함수 (결과값은 있음)
# def say() : 
#         return 'hi'    
# a = say() # 결괏값을 받을 변수 = 함수이름()
# print(a)


# def open_account():
#         print("새로운 계좌가 생성되었습니다")
# open_account() #이게 있어야 함수가 호출되어서 실행 됨



###################################
## 7-2.전달값과 반환값            ## 
###################################

# def deposit (balance, money) : #입금
#         print("입금이 완료. 잔액은 {0}입니다." .format(balance + money))
#         return balance+money

# balance = 0 #처음 잔액 
# balance = deposit(balance, 3000)
# print(balance)


# def withdraw  (balance, money):
#         if balance >= money : 
#                 print ("출금이 완료되었습니다. 잔액{0}" .format(balance-money))
#                 return balance-money
#         else : 
#                 print("잔액이 부족합니다. 남은잔액{0}" .format(balance))
#                 return balance

# balance = 0 #처음 잔액
# balance = deposit(balance, 3000)
# balance = withdraw(balance, 1000)


# def withdraw_night(balance, money): #저녁에 출금 수수료 포함
#         commission =100 
#         return commission, balance-money-commission  #여러개 값을 한번에 반환가능 

# balance = 0 #처음 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 1000)
# commision, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은{1}원입니다." .format(commision, balance))



###################################
## 7-3.기본값                    ## 
###################################

# 하드코딩 개념으로 기본 값이 들어가도록 하는 것. 

# def profile(name, age=17, main_lang="Python"):
#         print("이름: {0}  \t나이: {1} \t주사용언어 {2}"  \
#                 .format(name, age,main_lang))
              
# profile("jh", 20, "Python")
# profile("dk", 23, "자바")
# profile("유재석")
# profile("김태호", 34)



###################################
## 7-4.키워드값                   ## 
###################################

# 함수에서 전달받는 매개변수를 호출 시 지정해서 호출하면 순서가 바뀌어도 호출할 수 있음 

# def profile(name, age, main_lang):
#         print(name, age, main_lang)
        
# profile(main_lang="Java", name="유재석", age = 30)



###################################
## 7-5.가변인자                   ## 
###################################

# # *매개변수  <- 가변인자 형태로 이렇게 해서 여러개 변수를 받을 수 있음

# def profile(name, age, *main_lang):
#         print("이름: {0}  \t나이: {1} \t주사용언어 {2}".format(name, age, main_lang))

# profile("유재석", 20, "자바", "파이썬", "C", "C#", "GoLang")
# profile("김태호", 25, "자바", "파이썬", )



###################################
## 7-6.지역변수와 전역변수         ## 
###################################

# 전역변수(Global Variable) : 함수를 포함하여 스크립트 전체에서 접근할 수 있는 변수. 전역 변수에 접근할 수 있는 범위를 전역 범위(global scope)라고 한다. (※사용 : def 윗줄에 씀) 
# 프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다. 왜냐하면 함수는 독립적으로 존재하는 것이 좋기 때문이다. 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다
# 지역변수(Local Variable) : 변수를 만든 함수 안에서만 접근할 수 있는 변수이다. 함수 바깥에서는 접근 할 수 없다. (※사용 : def 구역 안에서 씀. 지금까지 배운 것.)

# gun = 10 
# def checkpoint (soilders): 
#         global gun # 전역공간에 있는 gun 사용
#         gun = gun -soilders
#         print("[함수내] 남은 총 {0}" .format(gun) )
        
# print("천체 총: {0}" .format(gun))
# checkpoint(2)
# print("남은 총: {0}" .format(gun))

# gun = 10 
# def checkpoint_return (gun, soilders): 
#         gun = gun -soilders
#         print("[함수내] 남은 총 {0}" .format(gun) )
#         return gun-soilders
        
# print("천체 총: {0}" .format(gun))
# gun = checkpoint_return(gun, 2)
# print("남은 총: {0}" .format(gun))



###################################
## 7-7.퀴즈 #6                   ## 
###################################

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오 
#  * 표준체중 : 각 개인의 키에 적당한 체중
 
#  (성별에 따른 공식)
#  남자 : 키(m) x 키(m) x 22
#  여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값  : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시 

# (출력예제) 키 175cm 남자의 표준 체중은 67.38 입니다. 

# def std_weight(height, gender):
#         if gender == "남자":
#                 print("키{0}m {1}의 표준 체중은{2} 입니다." \
#                         .format(height, gender,  height * height * 22 ))
#                 return height * height * 22
#         elif gender =="여자":
#                 print("키{0} {1}의 표준 체중은{2} 입니다." \
#                         .format(height, gender,  height * height * 22 ))
#                 return height * height * 21

# height = 170 
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키{0} {1}의 표준 체중은{2}kg 입니다." .format(height, gender, weight ))



###################################
## 8-1.표준 입출력                ## 
###################################

##설명 :sep 쓰면 중간에 분리. end 쓰면 맨 끝에 달아달라. 

# print("Python", "Java", "JavaScript", sep=" vs ") #출력 Python vs Java vs JavaScript

# print("Python", "Java", sep=" , ", end="?") 
# print("무엇이 더 재밌을까요?") #출력 Python , Java?무엇이 더 재밌을까요?

## stdout은 표준출력 stderr은 표준에러처리
# import sys 
# print("Python", "java", file =sys.stdout)
# print("Python", "java", file =sys.stderr)

##정렬해서 보여주기 (subject는 표준 명령어인 듯.)
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, scores in scores.items():   #사전 명령어  
#         print(subject.ljust(8), str(scores).rjust(4), sep=":") #ljust(8) 왼쪽 8칸 공간 확보 후 정렬해라. 

# # 은행 대기순번표 001, 002, 003, ... 
# for num in range(1, 21):
#         print("대기번호 : " + str(num).zfill(3))  #zill 3만큼 공간확보 후 0채워라

# #표준입력 (사용자 문자열을 받을땐 항상 String 형태로만 저장함 중요!)
# answer = input("아무값이나 입력하세요 : ")  #숫자를 넣어도 int가 아니라 Str로 입력 됨 
# print("입력한 값은 "+answer+"입니다.") 
# print(type(answer))



###################################
## 8-2.다양한 출력 포멧           ## 
###################################

# # 빈 자리는 빈 공간으로 두고, 오른족 정렬을 하되, 총 10자리 공간을 확보 
# print("{0: >10}" .format(500)) #출력        500 

# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}" .format(500)) #출력       +500 
# print("{0: >+10}" .format(-500)) #출력      -500 

# #왼쪽정렬하고, 빈칸으로 _로 채움
# print("{0:_>+10}" .format(500)) #출력 ______-500
# print("{0:_<+10}" .format(500)) #출력 +500______

# #큰숫자 들어오면 3자리마다 콤마 찍어주기 
# print("{0:,}" .format(1000000000000)) #출력 1,000,000,000,000
# print("{0:+,}" .format(1000000000000)) #출력 +1,000,000,000,000
# print("{0:+,}" .format(-1000000000000)) #출력 -1,000,000,000,000

# #3자리마다 콤마 직어주고, 부호 찍고, 자릿수 확보하기. 빈자리는 ^로 채워주기
# print("{0:^<+30,}" .format(1000000000000)) #+1,000,000,000,000^^^^^^^^^^^^

# #소수점 출력 
# print("{0:f}" .format(5/3)) #1.666667
# print("{0:.2f}" .format(5/3)) #1.67  (소수점 2번째 자리까지만 표시하기)



###################################
## 8-3.파일 입출력                ## 
###################################

# #file만들기
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# #append 하기 
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()

# #읽기 
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

#한줄씩 읽기 
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #한줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end="") #한줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end="") #한줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end="") #한줄 읽고 커서는 다음줄로 이동
# score_file.close()

# #list에 저장해서 한줄씩 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line)
# score_file.close()



###################################
## 8-4.pickle                    ## 
###################################

# 데이터를 파일로 저장하는 것 

# #파일 저장하기 (pickle.dump(입력값(변수),파일변수))
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["골프", "축구", "코딩"]}
# print(profile) #단순 확인목적 출력
# pickle.dump(profile, profile_file) #profile정보를 file에 저장하기
# profile_file.close()

# #데이터 가져오기
# import pickle
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #파일에 있는 정보를 profile에 불러오기
# print(profile) #단순 확인목적
# profile_file.close()



###################################
## 8-5.with                      ## 
###################################

#pickle 처럼 Close()를 해줄 필요 없음 

#pickle 파일 읽기
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# #일반 텍스트 쓰기
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 학습중입니다.")
    
#일반 텍스트 불러오기    
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())



###################################
## 8-6.Quiz                      ## 
###################################

# Quiz) 당신의 회사에서 매주 1회 작성해야 하는 보고서가 있다. 
# 보고서는 항상 아래와 같은 현태로 출력되어야 한다. 

# -X 주차 주간보고 - 
# 부서 : 
# 이름 :
# 업무 요약 : 
    
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오. 

# 조건 : 파일명을 '1주차.txt'.... 와같이 만듭니다. 



###################################
## 9-1.클래스                    ## 
###################################



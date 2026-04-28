kor_score = int(input("국어점수를 입력하세요."))
eng_score = int(input("영어점수를 입력하세요."))
math_score = int(input("수학점수를 입력하세요."))

score_list = [kor_score, eng_score, math_score]

average = sum(score_list) / len(score_list)

if average >= 90 :
    result = "A"
elif average >=80 :
    result = "B"
elif average >=70 : 
    result = "C"
elif average >=60 :
    result = "D"
else :
    result = "F"

print(f"당신의 평균 점수는 {average:.2f}으로 {result} 학점입니다.")
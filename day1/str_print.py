name = "전은지"
mbti = "ISTP"
blood_Type = "B"

# 안녕하세요. 전은지입니다. 제 MBTI는 ISTP이고요. 혈액형은 B형입니다.
print("안녕하세요. " + name + "입니다. " +"제 MBTI는 " + mbti + "이고요. " + "혈액형은 " + blood_Type + "입니다.")
print("안녕하세요. %s입니다. 제 MBTI는 %s이고요. 혈액형은 %s입니다." % (name, mbti, blood_Type))
print("안녕하세요. {}입니다. 제 MBTI는 {}이고요. 혈액형은 {}입니다." .format(name, mbti, blood_Type))
print("안녕하세요. {2}입니다. 제 MBTI는 {1}이고요. 혈액형은 {0}입니다." .format(blood_Type, mbti, name))

# 최신방식
print(f"안녕하세요. {name[:-2]+"**"}입니다. 제 MBTI는 {mbti}이고요. 혈액형은 {blood_Type}입니다.")

fam_list = ["전은지", "장원영", "츄", "수지", "박보검", "이채영"]

favorite = {
    "food" : [{
        "name": "빵"
        "bestThing": ["식빵", "카스테라", "버터떡"] 
    },    "과자", "고기", "술"],
    "activity" : ["여행", "낮잠", "노래"],
    "animal" : ["고양이"]
}

#튜플 수정해보기()

#세트 생성{11,2,33,3,3,3,3}

#print("food" in favorite.keys())
print("여행" in favorite.get("activity",[]))
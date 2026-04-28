logined_id_list = [
    "wjdd1s",
    "leeyun0528-cyber",
    "d0hiru",
    "Bul1etBear",
    "Kimmyoungsung",
    "wjdd1s",
    "leeyun0528-cyber",
    "d0hiru",
    "Bul1etBear",
    "Kimmyoungsung",
    "wjdd1s",
    "Bul1etBear",
    "Kimmyoungsung",
    "wjdd1s",
    "leeyun0528-cyber",
    "d0hiru",
    "Bul1etBear",
]

user_set1 = set(logined_id_list) #    "wjdd1s" "leeyun0528-cyber","d0hiru","Bul1etBear","Kimmyoungsung"
print(user_set1)

user_set2 = {"Bul1etBear", "Kimmyoungsung", "dumpling0531", "Lyxx-cloud", "yeon506"}

print(user_set1)
print(user_set2)

print(user_set1.intersection(user_set2))
#print(user_set1.intersection_update(user_set2))

print(user_set1.union(user_set2))#합집합

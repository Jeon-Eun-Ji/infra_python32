#서버 "리스트"
server_list = ["WEB-01", "DB-01", "APP-01"]

#타입 확인
type(server_list)

#"리스트" 내 요소를 인덱싱하여 출력
print(server_list[0])
print(server_list[1])
print(server_list[2])
print(server_list[2] == server_list[-1])

#추가
server_list.append("PROXY-01")
print(server_list)
#삭제
server_list.remove("DB-01")
print(server_list)

#리스트 연장
server_list.extend(["WEB-02", "DB-02", "APP-02"])

# insert(인덱스, 값) - 원하는 위치에 삽입
server_list.insert(2, "일번째 서버 넣기")

print(server_list)

#전체 길이 확인
print(f"서버 리스트에는 총 {len(server_list)}개의 요소가 있습니다.")
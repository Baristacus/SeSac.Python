# 리스트
a = [1, 2, 3, 4, 5, 6]
print(a[4])  # 해당 index값 출력
print(len(a))  # 리스트의 총 길이 구하기
print(a[1:3])  # 시작은 포함. 끝은 -1

a.append(7)  # 리스트 마지막에 넣기
print(a)

a.insert(0, 0)  # 원하는 index위치에 넣기
print(a)

a.remove(7)
print(a)

fruits = ["사과", "바나나", "딸기"]
print(fruits)

members = [2, "Seokin", "3"]
print(members)

# ----------------------------------------------------

# 튜플: 변경 불가한 리스트를 생성 - 이뮤터블(Immutable)
b = (1, 2, 3, 4, 5)

print(b[1:3])
print(b[1:])
print(b[:3])


# ----------------------------------------------------

# 딕셔너리: key, value
c = {
    "name": "Seokin",
    "age": 10,
    "city": "Seoul",
}

print(c)
print(c["name"])
print(c["age"])
print(c["city"])


c["email"] = "email@e.com"  # 새로운 key, value 추가
print(c)


del c["email"]  # key, value 삭제
print(c)

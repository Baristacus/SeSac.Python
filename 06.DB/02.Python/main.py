import db_crud as db


def main():
    # 테이블 생성
    db.create_table()

    # 데이터 삽입
    db.insert_data("Alice", 25)
    db.insert_data("Bob", 30)
    db.insert_data("Charlie", 35)
    db.insert_data("David", 20)

    # 데이터 조회
    print("----- 데이터 삽입 후 데이터 조회 -----")
    users = db.fetch_users()
    for user in users:
        print(user)
    print("----- 데이터 삽입 후 데이터 조회 끝 -----")

    # 데이터 수정
    db.update_user("Alice", 35)
    db.update_user("Bob", 40)
    db.update_user("Charlie", 45)

    # 데이터 조회
    print("----- 데이터 수정 후 데이터 조회 -----")
    users = db.fetch_users()
    for user in users:
        print(user)
    print("----- 데이터 수정 후 데이터 조회 끝 -----")

    # 데이터 삭제
    db.delete_user("Alice")

    # 데이터 조회
    print("----- 데이터 삭제 후 데이터 조회 -----")
    users = db.fetch_users()
    for user in users:
        print(user)
    print("----- 데이터 삭제 후 데이터 조회 끝 -----")


if __name__ == "__main__":
    main()

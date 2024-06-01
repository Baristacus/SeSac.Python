# 일상 생활에서의 개념과 논리를 코딩으로 옮겨놓고자 하는 개념


class Person:
    # 프로퍼티를 정의
    name = ""
    age = 0
    status1 = "playing"

    def __init__(self, name, age):  # 초기화 함수(선택사항)
        self.name = name
        self.age = age

    # 메소드(함수) = 행위를 지정
    def speak(self):
        print(f"안녕 {self.name}")

    def walk(self):
        print(f"간다 {self.name}")
        self.status1 = "walk"

    def think(self):
        print(f"생각한다 {self.name}")
        self.status1 = "think"

    def status2(self):
        print(f"현재상태: {self.status1}")


# 사람(person) 이라는 객체를 만들고, 사람이 할 수 있는 행위를 정의
# 객체의 함수는 첫번째 인자가 self 이어야 함
#   나중에 필요할때 객체 자신의 속성 등 필요한 부분에 접근하기 위해서.

alice = Person("Alice", 10)
# alice.name = "Alice"
bob = Person("Bob", 20)
# bob.name = "Bob"
# print(type(alice))

alice.speak()
bob.walk()

alice.think()
alice.status2()

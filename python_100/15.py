# 공백을 두고 입력된 정수 2개 줄 바꿔 출력하기
a, b = input().split()
a = int(a)
b = int(b)
print(a)
print(b)

# # map 함수 이용해서 정수 입력 받고 나누기
a, b = map(int, input().split()) # .split() == 공백을 두고 나눈다.
print(a)
print(b)
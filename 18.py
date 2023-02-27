# 시간 입력받아 그대로 출력하기
h, m = input().split(':') # split(':')는 :(콜론) 기호를 기준으로 자른다.
print(h, m, sep=':') # sep(erator)는 분류기호로서 :(콜론) 기호를 사이에 두고 값을 출력한다.
print(type(h)) #< class 'str'>
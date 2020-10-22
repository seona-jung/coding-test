n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 각 데이터의 두 번째 원소를 기준으로 설정
# def setting(data):
#     return data[1]
# array.sort(key=setting)

array = sorted(array, key=lambda student : student[1])

for student in array:
    print(student[0], end= ' ')


# 평균 구하기 (출처: https://programmers.co.kr/learn/courses/30/lessons/12944?language=python3)
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 제한사항
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

def solution(arr):
    answer = sum(arr) / len(arr)
    return answer

# average를 구하기 위해 일반적인 방식으로 전체의 합/원소의 개수로 구하였다.
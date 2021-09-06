#약수의 합 (출처: https://programmers.co.kr/learn/courses/30/lessons/12928)
#정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

#제한 사항
#n은 0 이상 3000이하인 정수입니다.
#입출력 예1
#12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

#입출력 예2
#5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.

 def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0: answer += i
    return answer
 

#range 값에 여러 숫자를 대입해 보았는데, 우선 range(1, n) 으로 실행했다.
#그런데 오류값이 나왔다. 왜일까? 그래서 n+1을 넣었는데 문제 없이 실행됐다.
#자기 자신을 약수로 갖게 하기 위해서일 것이다.
#12의 약수는 12도 포함되므로 range 범위를 n으로 실행할 경우 오류가 나온다.

#좋아요를 가장 많이 받은 다른 사람의 풀이를 가져와서 실행해 보았다.

def sumDivisor(num):
# num / 2 의 수들만 검사하면 성능 약 2배 향상잼
return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
 

#한 줄 짜리 코드로 실행이 가능하므로 효율적이다.
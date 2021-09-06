#수박수박수박수박수박수? (출처: https://programmers.co.kr/learn/courses/30/lessons/12922)
#길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

#제한 조건
#n은 길이 10,000이하인 자연수입니다.

def solution(n):
    answer = ''
    str_list = list('수박')

    for i in range(n):
        if i % 2 == 0 :
            answer += str(str_list[0])
        else: answer += str(str_list[1])
return answer
 

#str을 사용하라는 팁을 참고해서 풀어 보았다.

#그러나 더 직관적이고 쉬운 다른 사람의 풀이가 있어서 참고하였다.

def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)
# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));
 
#연산기호를 이용해서 몫, 나머지로 계산해 풀이하는 위의 방법이 더 좋을 것 같다.

 
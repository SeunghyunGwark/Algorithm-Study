# 가운데 글자 가져오기 (출처: https://programmers.co.kr/learn/courses/30/lessons/12903)
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

#제한사항
#s는 길이가 1 이상, 100이하인 스트링입니다.
def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer = s[int((len(s))/2 - 1):int(len(s)/2 + 1)]
    else:
        answer = s[int((len(s) - 1)/2)]
    return answer
 
#다른 풀이를 보니 위에 스트링이라고 명시를 했다는 것을 고려하여 str을 사용해도 될 것 같다!

def string_middle(str): 
    return str[(len(str)-1)//2:len(str)//2+1]
 
#위의 것은 다른 사람의 코드 중 가장 좋았던 것인데, 한 줄로 간단하게 표현할 수 있어서 좋은 코드인 것 같다. 
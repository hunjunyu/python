# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다
#       - { }



ss = set([1,2,2,4,6,9,5,7,7,8,9,2,3,111])
s={1,2,3,1,1,4,5,6,6,2}
s1={3,5,4,6,3,4}
s3 = set()
s3 = {1,2,3,555,6,2,6,6,55,22,1,555}
#print(s[0])
#set은 추출을 못한다
print(s&s1) #교집합
print(s1|s)#합집합
print(s-s1)#차집합
print(s1-s)
print(ss)
print(s3)
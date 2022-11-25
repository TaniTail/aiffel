
## 실습1 -전화번호 끝자리 가리기 ##

numbers = '010-12345-23456'

#def change_num(nums): #기본적으로 큰 함수의 토대를 잡아두고
#    return answer    #우리가 반환하고 싶은 값을 내는 함수라는 것을 생각. (앤서라는 로컬 변수를 만들것을 대강..)

##그리고 change_num 이라는 수 안에 한 줄씩 코드를 채워보자!

numbers[-5:]
numbers.replace(numbers[-5:], '#####')

def change_num(nums):
    answer = nums.replace(nums[-5:], '#####')
    return answer

change_num('0102836848484')


## 실습 2 -리스트 평탄화 ##


overlap = [[1, 2],3,[[4,5,6],7],8,9]

for element in overlap:
    print(element)
    
    #반복문은 range함수와 자주 쓰이지만 이렇게 컬렉션을 차례로 꺼낼 수 있다.
    
for i in range(len(overlap)):
    print(overlap[i])


a=[[[1,2],3],4,[5,6]]

def flatten(data):
    output = [ ] # 빈 리스트 만들어두기
    
    for element in data:
        if type(element) == list:
            output += flatten(element)
        else:
            output.append(element)
    return output


flatten(a)


## 실습 3 ##

x = 100.0

if x % 1 == 0 :
    print('정수입니다.')
    

##type(x%1)
##print(x%1) -> 정수와 실수 섞어서 연산하면 값은 실수가 나온다. 따라서 요렇게 하면 안됨



##만들 함수는 input 값이 둘다 정수라면 두 정수를 나눴을 때의 값을 구해주고,
##입력된 값이 정수가 아니라면 '정수만 계산 가능합니다'라고 출력하고 
##결과값은 None으로 출력하는 함수



def int_divider(x,y):
    
    if x % 1 ==0 and y % 1 == 0:
        
        answer = x / y
        
        #둘다 정수니까 리턴값에. 
    else:
        print('정수만 계산 가능합니다.')
        return None ################ 이부분 헷갈리는 듯!~
    
        
    return answer


int_divider(6,3)




def int_divider(x,y):
    
    if x % 1 ==0 and y % 1 == 0:
        
        answer = x / y
        
        #둘다 정수니까 리턴값에. 
    else:
        print('정수만 계산 가능합니다.')
        answer = None
    
        
    return answer


int_divider (10,3)

int_divider (-1,0.9)

int_divider (6.0,3)




print(int_divider (10,3))




## 아.... 리턴되는 값과 리턴되는 값의 '출력' 이 다른 부분!!
##결과값 표시는 가장 나중에 갖고 있는 갚, 즉 맨 마지막 리턴값!!!!



def mul(*values):
    output = 1
    for num in values:
        if num <= 10:
            output *= num
        else:
            pass
    return output


print(mul(3,4,5,6))







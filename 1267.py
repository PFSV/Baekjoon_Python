
'''
통화시간 // 청구되는 통화시간 


영식 요금제

0~29초: 몫 0, 10원
30~59초: 몫 1, 20원
60~89초: 몫 2, 30원

-> 청구금액 = 요금제 가격(통화시간//요금제 초+1)

시간 당 청구금액 산출 후 총합 비교, if로 비교
'''

#통화 시간 space로 구분 후 int 배정, 리스트로 묶기(변수가 몇 개인지 모름)

#통화시간마다 청구금액 출력해 총합에 더하기: 시간의 개수 정해졌으므로 for
#총 청구금액: 영식: y_sum, 민식: m_sum

n = int(input())

y_sum = 0
m_sum = 0

for i in list(map(int,input().split())):
    y_sum += 10*((i//30)+1)
    m_sum += 15*((i//60)+1)
    
if y_sum < m_sum:
    print("Y",y_sum)
elif y_sum > m_sum:
    print("M",m_sum)
else:
    print("Y M",y_sum)



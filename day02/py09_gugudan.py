# 구구단 프로그램
# 2 x 1 =2 ~ 9 x 9 = 81

for i in range(2, 10):
    # print(i)
    '''
    if i == 9:
        break
    '''
    for j in range(1, 10):
        if j == 9: ##'='은 값을 넣는거 '=='은 값을 비교 '='을 사용하면 문법상 맞지않아서 오류 출력
            break

        # print(i * j) - 값만 출력
        print(i, 'x', j, '=', i * j, end ='\t') #end = '\t' 터미널에서 옆으로 펼쳐지게 표시
    
    
    print()
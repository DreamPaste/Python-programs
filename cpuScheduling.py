
# FCFS 알고리즘을 구현한 함수입나다.
def FCFS(ready_que) :             # 선입선출 알고리즘 함수 선언
    print("### FCFS-염휘건 ###\n")  # 알고리즘 종류를 포함한 내용 출력

    i=1                            #반복횟수를 확인할 i 를 1로 설정
    
    print("실행 순서 :", end=" ")    # 실행 순서를 출력한다
    for key in ready_que.keys() :  #정렬한 딕셔너리의 키(프로세스 번호)를 반복문으로 추출한다.
        print("P%d"%(key), end="") #추출한 프로세스를 하나씩 출력한다
        if len(ready_que) != i : print( " -> ",end="") #마지막 반복문에는 화살표를 출력하지 않아 출력되는 프로세스 사이에만 화살표가 들어간다
        i+=1 #반복할때마다 i가 1씩 증가한다
    
    print() # 한줄을 띄운다
    i=0 ##프로세스 순서 인덱스
    ready_time = 0 ##대기 시간 
    run_time =0 ##총 실행 시간
    sum_ready_time =0# 대기 시간을 모두 더한 값
    for key, value in ready_que.items() : #반복문을 통해 readyque의 딕셔너리에서 프로세스 이름과 각 프로세스의 정보를 하나씩 접근한다.
       
        run_time += value[1]              #실행시간을 반복할때마다 누적한다
        if i == 0 :                       #처음 반복할때를 확인하는 조건문
            ready_time= 0                 ##첫번째 도착하는 프로세스는 대기 시간이 0
        else :                            #처음 반복 이후일때
            ready_time= run_time-value[1]-value[0] ##그 다음 프로세스부터의 대기 시간은 이전까지 실행한 시간의 합에서 도착 시간을 뺀 값이다.
        i+=1                              #반복할때마다 i값을 증가시킨다
        sum_ready_time+=ready_time        #반복할때마다 나온 대기시간을 누적하여 총 대기시간을 구한다.
        print("\n프로세스 P%d 대기시간 : %d"%(key,ready_time)) #프로세스 이름과 각 프로세스의 대기시간을 구한다.
    print("\n평균대기시간 : %f "%(sum_ready_time/len(ready_que))) #평균 대기시간을 구한다(총 대기시간에서 프로세스 개수를 나눈다)
    
    
#SJF 알고리즘을 구현한 함수입니다.
def SJF(ready_que) :                    #SJF 알고리즘 함수 선언
    
    print("### SJF-염휘건 ###\n")         #스케쥴링 종류와 이름 출력
    run_que = dict(sorted(ready_que.items(), key=lambda x : x[1][1]))  ##프로세스를 실행 시간 순으로 정렬한다.
    que =[] # que 리스트를 선언힌다.
    i=0 #반복순에서 사용할 i 지정
    for key,value in ready_que.items() : #ready_que에 첫 항목만 que 리스트에 담는다.(비선점 우선순위)
        if i==0 : #i가 0일때 (처음일때)
            que.append([key,value]) #que리스트에 프로세스 이름과 그 정보들을 입력한다.
            break #반복문을 나간다.
        i+=1 #반복할때마다 1씩 증가
    for key ,value in run_que.items() : #실행 시간 순으로 정렬된 딕셔너리에 순서대로 접근한다.
        if que[0][0] != key :             #que에 이미 담긴 프로세스를 제외하고 
            que.append([key,value])        #que 리스트에 추가한다.
        
    print("실행 순서 :", end=" ")    # 실행 순서를 출력한다
    for i, p in enumerate(que) :  #sjf으로 들어간 que에 처음부터 하나씩 접근한다.
        print("P%d"%p[0], end="") #추출한 프로세스를 하나씩 출력한다
        if len(que)-1 != i : print( " -> ",end="") #마지막 반복문에는 화살표를 출력하지 않아 출력되는 프로세스 사이에만 화살표가 들어간다
        
    print() # 한줄을 띄운다
    ready_time = 0 ##대기 시간 
    run_time =0 ##총 실행 시간
    sum_ready_time =0# 대기 시간을 모두 더한 값
    for i, p in enumerate(que): #반복문을 통해 que의 리스트에서 프로세스 이름과 각 프로세스의 정보를 하나씩 접근한다.
        
        run_time += p[1][1]              #실행시간을 반복할때마다 누적한다
        if i == 0 :                       #처음 반복할때를 확인하는 조건문
            ready_time= 0                 ##첫번째 도착하는 프로세스는 대기 시간이 0
        else :                            #처음 반복 이후일때
            ready_time= run_time-p[1][1]-p[1][0] ##그 다음 프로세스부터의 대기 시간은 이전까지 실행한 시간의 합에서 도착 시간을 뺀 값이다.
        
        sum_ready_time+=ready_time        #반복할때마다 나온 대기시간을 누적하여 총 대기시간을 구한다.
        print("\n프로세스 P%d 대기시간 : %d"%(p[0],ready_time)) #프로세스 이름과 각 프로세스의 대기시간을 구한다.
    print("\n평균대기시간 : %f "%(sum_ready_time/len(que))) #평균 대기시간을 구한다(총 대기시간에서 프로세스 개수를 나눈다)
    
    
#RR 알고리즘을 구현한 한수입니다.   
def RR(ready_que, timer) :      #라운드 로빈 알고리즘을 함수로 선언
    print("### RR-염휘건###\n")   #스케쥴링 종류와 이름 출력
    plist =[]                   #프로세스를 저장할 리스트 선언
    que =[]                     #슬라이스로 나눈 프로세스를 저장할 리스트 선언
    
    for key, value in ready_que.items() :    #readyque의 프로세스 이름과 정보를 순서대로 접근한다
        plist.append([key,value[1],0,False,value[0]]) #리스트에 프로세스 이름 ,실행시간 ,반복횟수, 큐에서 나갈 프로세스를 확인하는 bool 값,도착시간 을 저장
    
    i=0  #인덱스할 i값
    now=0 #프로세스가 처리된 시간
    remain=0 #프로세스가 시작한 시간
    while plist : #리스트 안의 항목이 없을때까지 반복
        
        if i == len(plist) : #큐가 한바퀴 돌때마다 
            temp =[] #temp 리스트 생성
            for p in plist : #리스트에서 프로세스 하나씩 검사해서
                if p[3] != True: #실행시간이 아직 남은 프로세스는
                    temp.append(p) #temp 리스트에 넣는다
            plist = temp #temp 리스트는 필요 없는 프로세스를 정리 후 plist로 만든다.
            
            i=0             #프로세스를 처음부터 검사할수 있도록 i를 0으로 초기화한다.
            
        if(plist[i][1] <= timer) : #타임 슬라이스보다 실행 시간이 적은 프로세스를 확인한다.
            remain = now  #프로세스 시작 시간을 저장
            now += plist[i][1] #프로세스가 남은 실행시간만큼 실행되고, 그 시간이 누적되어 now에 저장
            plist[i][2]+=1 #반복횟수가 증가한다.
            que.append([plist[i][0], remain, plist[i][2],plist[i][4]]) #프로세스 이름, 시작시간, 프로세스 등장 횟수 , 도착시간 저장
            plist[i][3] = True #실행\] 이제 남지 않았으므로 나가도록 표시해둔다.
            if len(plist) == 1: #모든 프로세스가 나가면 반복이 끝난다.
                break #반복 탈출
        else :              #실행 시간이 타임 슬라이스보다 많다면
            remain = now    #프로세스 시작 시간을 저장
            now += timer    #프로세스가 할당시간만큼 실행된다. 그 시간이 누적되어 now에 저장
            plist[i][1] -=timer #프로세스가 남은 실행시간이 할당된 시간만큼 준다.
            plist[i][2]+=1  #반복횟수가 증가한다.
            que.append([plist[i][0], remain, plist[i][2],plist[i][4]]) #프로세스에 이름, 시작시간, 프로세스 등장 횟수 , 도착시간 저장
            
        i+=1   #반복할때마다 i가 1씩 증가한다.
    
    i=1 #i를 1로 초기화
    
    print("실행 순서 :", end=" ")          #실행순서를 표시할 수 있도록 출력한다
    for index in que :          #que 리스트에서 순서대로 하나씩 접근한다.
        print("P%d"%(index[0]), end=" ")      #프로세스 이름을 출력한다
        if len(que) != i : print(" -> ",end="") #마지막 반복에는 화살표를 출력하지 않아 프로세스 사이에 화살표가 들어갈 수 있도록 한다.
        i+=1                             #반복마다 i값이 증가되도록 한다.
        
    print("\n") #두 줄을 건너뛴다    
    all_ready=0 # 총 대기시간을 구할 변수
    ready=0 #대기 시간을 넣을 변수
    for key in ready_que.keys() :  #프로세스를 순서대로 하나씩 접근한다
        for j in range(len(que)-1, 0, -1) : #que리스트 가장 뒤에 있는 항목들부터 순서대로 접근한다.
            if( key == que[j][0]) :  #각 프로세스마다 que 리스트에서 제일 뒤에 있는 값(큐에서 마지막으로 할당된 프로세스 슬라이스의 정보)
                ready = que[j][1]-que[j][3]-((que[j][2]-1) * timer) #대기 시간 : 프로세스가 시작한 시간-도착시간-(큐에 있는 프로세스 조각의 개수-1 * 각 프로세스 점유 시간)
                all_ready += ready # 총 대기시간에 값을 누적한다.
                print("프로세스 P%d 대기시간 : %d\n"%(key,ready)) #프로세스 이름과 대기 시간을 출력한다
                break #각 프로세스마다 하나씩만 출력하도록 항목을 찾으면 내부 반복문을 나간다.
    
    print("\n평균대기시간 : %f "%(all_ready/len(ready_que))) #평균대기시간은 프로세스의 전체 대기시간에서 프로세스 수를 나눈 값이다.
    
    
#우선순위 알고리즘을 구현한 함수입니다.
def Priority(ready_que) : # 우선순위 프로세스 알고리즘 함수 선언
    print("### 우선순위 스케쥴링-염휘건 ###\n")         #스케쥴링 종류와 이름 출력
    prior_que = dict(sorted(ready_que.items(), key=lambda x : x[1][2]))  ##프로세스를 우선 순위 순서로 정렬한다.
    que = [] #que 리스트 선언
    i=0 #반복순에서 사용할 i 지정
    for key,value in ready_que.items() : #ready_que에 첫 항목만 que 리스트에 담는다.(비선점 우선순위)
        if i==0 : #i가 0일때 (처음일때)
            que.append([key,value]) #que리스트에 프로세스 이름과 그 정보들을 입력한다.
            break #반복문을 나간다.
        i+=1 #반복할때마다 1씩 증가
    for key ,value in prior_que.items() : #우선 순위로 정렬된 딕셔너리에 순서대로 접근한다.
        if que[0][0] != key :             #que에 이미 담긴 프로세스를 제외하고 
            que.append([key,value])        #que 리스트에 추가한다.
        
    print("실행 순서 :", end=" ")    # 실행 순서를 출력한다
    for i, p in enumerate(que) :  #우선순위 스케줄링으로 들어간 que에 처음부터 하나씩 접근한다.
        print("P%d"%p[0], end="") #추출한 프로세스를 하나씩 출력한다
        if len(que)-1 != i : print( " -> ",end="") #마지막 반복문에는 화살표를 출력하지 않아 출력되는 프로세스 사이에만 화살표가 들어간다
        
    print() # 한줄을 띄운다
    ready_time = 0 ##대기 시간 
    run_time =0 ##총 실행 시간
    sum_ready_time =0# 대기 시간을 모두 더한 값
    for i, p in enumerate(que): #반복문을 통해 que의 리스트에서 프로세스 이름과 각 프로세스의 정보를 하나씩 접근한다.
        
        run_time += p[1][1]              #실행시간을 반복할때마다 누적한다
        if i == 0 :                       #처음 반복할때를 확인하는 조건문
            ready_time= 0                 ##첫번째 도착하는 프로세스는 대기 시간이 0
        else :                            #처음 반복 이후일때
            ready_time= run_time-p[1][1]-p[1][0] ##그 다음 프로세스부터의 대기 시간은 이전까지 실행한 시간의 합에서 도착 시간을 뺀 값이다.
        
        sum_ready_time+=ready_time        #반복할때마다 나온 대기시간을 누적하여 총 대기시간을 구한다.
        print("\n프로세스 P%d 대기시간 : %d"%(p[0],ready_time)) #프로세스 이름과 각 프로세스의 대기시간을 구한다.
    print("\n평균대기시간 : %f "%(sum_ready_time/len(que))) #평균 대기시간을 구한다(총 대기시간에서 프로세스 개수를 나눈다)
    
    
    
#메인 함수입니다.
if __name__ == '__main__' : #main함수 선언
    process_list = {} ##준비 큐를 딕셔너리(키와 벨류가 쌍으로 짜여진 형태)로 만든다.
    
    print("201968052 염휘건\n\n\n\n"); #학번 이름 출력
    print("입력 방식을 선택하세요\n정적입력 : 0 동적입력 : 1")# 입력 방식을 선택하도록 알려줌
    mod = int(input()) #정수룰 입력받음
    if mod == 0 : #mod가 0일때
        print("<<정적 입력 정보>>\n") #정적 입력 정보를 안내한다.
        type_list = ["도착시간","실행시간","우선순위"] #프로세스의 정보 설명을 리스트로 만든다
        process_list = {1: [0, 15, 3], 2: [5, 8, 4], 3: [8, 2, 1], 4: [10, 5, 2]} #정적 프로세스 데이터를 입력
        
        slice = 4 #프로세스 슬라이싱시간은 4초
        
        print("\n\n")#두 줄을 건너뛴다.
    elif mod == 1 :#mod가 1일때
        print(" 전체 프로세스 수와 타임 슬라이스 시간 입력") #입력할 항목을 알려줌
        count, slice = map(int, input().split())  #프로세스의 수와 라운드 로빈 알고리즘에서 사용할 타임 슬라이스 시간을 입력받아 각각의 변수에 넣는다
        print("--프로세스의 도착시간, 실행시간, 우선순위 입력") #입력할 항목을 알려줌
    
        for i in range(count) : ##프로세스 개수만큼 반복한다.
            print("프로세스 %d 입력 :"%(i+1)) # 입력받을 프로세스 이름과 함께 한줄씩 입력할수 있도록 돕는다
            process_list[i+1] = (list(map(int, input().split()))) ##각 프로세스의 도착시간, 실행시간, 우선순위를 리스트 형태로 입력받는다.
    else :                              #0과1입력을 제외하면
        print("입력이 잘못되었습니다!") # 0과 1을 제외한 입력은 오류처리
    print("\n프로세스 정보를 출력합니다.\n"); #프로세스 정보를 출력하도록 하는 안내문
    
    for key, value in process_list.items() : #프로세스 내용을 딕셔너리에서 하나씩 꺼내온다.
        
        print("프로세스 %d :"%key,end=" ") #각 프로세스 이름을 출력한다
        print("도착시간 : %d 실행 시간 : %d 우선 순위 : %d\n"%(value[0],value[1],value[2])) #각 프로세스 정보를 출력한다.
        
    print("타임 슬라이싱 시간 : %d\n\n"%slice) #라운드 로빈의 프로세스당 할당할 시간을 입력합니다.
    
    ready_que = dict(sorted(process_list.items(), key= lambda x : x[1][0]))  ##준비 큐에 있는 프로세스를 도착시간 순서로 정렬한다.
    FCFS(ready_que)         #FCFS 알고리즘 함수 실행
    print("\n")             #두줄을 띄운다
    SJF(ready_que)          #SJF 알고리즘 함수 실행
    print("\n")             #두 줄을 띄운다
    RR(ready_que, slice)    #RR 알고리즘 함수 실행
    print("\n")             # 두 줄을 띄운다
    Priority(ready_que)     # 우선순위 스케쥴링 함수 실행
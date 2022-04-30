
from locale import T_FMT_AMPM
from os import remove
import numpy as np

## 행 중 최대 길이보다 적은 행이 있다면 0을 추가하도록 만들기

row = []
matrix = []
ccount, rcount =0,0
newmat = []
def inputmatrix() :
    while True :
        row = list(map(int, input("%d번째 행을 입력하세요 : " % (len(matrix)+1)).split()))
        matrix.append(row)
        if matrix[-1] == [] :
            matrix.remove(matrix[-1])
            break;    
        
    rcount = len(matrix)
    ccount = max(list(map(len, matrix)))
    for row in matrix :
        if len(row) < ccount :
           while len(row) < ccount :
                row.append(0)
    
    return matrix, rcount, ccount
    

        
        
        
def typemat (matrix, rcount, ccount) :
    kindmat = ["정사각행렬", "영행렬", "단위행렬", "대각행렬", "삼각행렬"]
    zeromat = [[0 for i in range(ccount)]for i in range(rcount)]
    unitmat = [[1 if i==j else 0 for i in range(ccount)]for j in range(rcount)]
    if matrix == zeromat :
        print(kindmat[1])
    if rcount == ccount :
        print(kindmat[0])
        if unitmat == matrix :
            print (kindmat[2])
    
        a =b = 0
        k = 0
        for i  in range(rcount) :
            for j  in range(ccount) :
                if i == j :
                    pass
                elif (i>j) and (matrix[i][j] == 0) :
                    a += 1
                elif (i<j) and (matrix[i][j] == 0) :
                    b += 1
                
        k = int(rcount *(rcount-1)/2)
        if a == k: print("상" + kindmat[4])
        elif b == k : print("하" + kindmat[4])
        elif a + b== 2*k : print(kindmat[3])
    
    return zeromat, unitmat;




def moder(mode):
    if mode ==1 :  # 행렬로 해 찾기
        cons = [1,2,3,4]
        
    
    
    
    
    
    
        pass
    
    
    if mode ==2 :   #역함수 만들기
        pass

        
    






##REF 및 RREF 연산하기(가우스 소거법)
def gausmin (matrix, ccount, rcount) :
        
        newmat = matrix
        j= 0
        cul=[]
        for i  in range(rcount):
            rowcul = []
            
            if all(newmat[i][j]==0 for i in range(len(newmat[i]))): j+=1   #모든 열의 항목이 0이면 다음 열로 넘긴다.
            col = [newmat[i][j] for i in range(rcount)] # 같은 행인 원소들
            if col.count(1) == 1 and col.count(0) == rcount -1  :  j+=1    #원소들중 하나만 1이고 나머지가 0이면 다음 열로 넘긴다
            if j>ccount or i>rcount : 
                break #j가 전체 열보다 클 경우 연산하지 않는다
             
            
            if i ==rcount : pass
        
            elif all(0==x for x in newmat[i]) : # 한 행이 모두 0 이면 밑으로 내리기
                        tmp = newmat.pop(i)
                        newmat.append(tmp)
                        print("E",i+1,rcount+1)
                        rowcul = ["E",i,rcount]
                        cul.append(rowcul)
            elif newmat[i][j] ==0 :    #i행 1열이 0일경우 바로 밑에 행과 자리를 바꾼다
                     tmp = newmat[i]
                     newmat[i][j] = newmat[i+1]
                     newmat[i] = tmp
                     print("E",i+1,i+2)
                     rowcul = ["E", i, i+1]
                     cul.append(rowcul)
            if i == j :        #i와 j가 같을때 
                for p in range(rcount) :
                    if p==i : continue #rref연산이 되도록 한다
                    x = newmat[p][j] / newmat[i][j]
                    print("E%d%d(-%.3f/%.3f)"%(i+1,p+1,newmat[p][j], newmat[i][j]))
                    rowcul = ["E",i,p,":",-newmat[p][j],"/",newmat[i][j]]
                    cul.append(rowcul)
                    newmat[p] = [newmat[p][k]+(newmat[i][k]*(-x))for k in range(ccount)] 
                    print(np.array(newmat))
                
                if newmat[i][j] != 1 :   
                    print("E%d(-1/%d)" %(i+1,newmat[i][j]))#행의 1열이 1이 되도록 만든다
                    rowcul = ["E",i,":",-1,"/",newmat[i][j]]
                    cul.append(rowcul)
                    newmat[i] = [newmat[i][n]/newmat[i][j] for n in range(len(newmat[i]))]
                    print(np.array(newmat))
        
        return newmat, cul
        






def devarray (cul) :
    
    pass
    
    
    
    
    
    
def showmat(matrix) :
    for i  in matrix :
        print(i)
        
        
if __name__ == '__main__' :
    matrix, rcount, ccount = inputmatrix()
    print("입력된 행렬 :")
    zeromat,unitmat = typemat(matrix, ccount, rcount)
    print(np.array(matrix),"\n")
    
    newmat,cul = gausmin(matrix, ccount, rcount)
    print(cul)
    
    
    
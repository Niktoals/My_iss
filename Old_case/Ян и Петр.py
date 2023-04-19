import random
# In i Petr
def ran():
    answer=[]
    for i in range(100):
        f=random.randint(0, 1)
        if f==1:
            answer.append('1')
        if f==0:
            answer.append('0')
    return answer
def In():
    k=0
    answer=ran()
    for i in range(len(answer)//2):
        count=[]
        count.append(answer[:2:])
        k+=2
        if count[0].count('1')==2:
            break
        del answer[:2]
    return k
def Petr():
    k=0
    answer=ran()
    for i in range(len(answer)//2):
        count=[]
        count.append(answer[:2:])
        k+=1
        if count[0][0]=='0' and count[0][1]=='1':
            break
        del answer[0]
    return k
def days():
    count_In=[]
    summ_In=0
    for i in range(100):
        count_In.append(In())
    for i in count_In:
        summ_In+=i
    result_In=summ_In/100
    count_Petr=[]
    summ_Petr=0
    for i in range(100):
        count_Petr.append(Petr())
    for i in count_Petr:
        summ_Petr+=i
    result_Petr=summ_Petr/100
    return result_In, result_Petr
def main():
    razniza=[]
    summ=0
    for i in range(100):
        result_In, result_Petr=days()
        answer=str(result_In-result_Petr)
        indx=answer.index('.')
        if indx==1:
            razniza.append(answer[:4:])
        if indx==2:
            razniza.append(answer[:5:])
    for i in razniza:
        summ+=float(i)
    ans=summ/100
    ind=str(ans).index('.')
    ans=str(ans)
    if ind==1:
        pass
        print(ans[:4:])
    if ind==2:
        pass
        print(ans[:5:])
if __name__=='__main__':
    main()
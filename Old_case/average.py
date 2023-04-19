import random 

def dig(n_n, op_n, co_n):
    ls=[]
    for i in range(100):
        n=random.randint(2, n_n)
        days={}
        for n in range(1, n):
            oper=random.randint(1, op_n)
            cost=random.randint(1, co_n)
            days[n]=cost/oper # среднее от каждого дня
        print(days)
        ans=sum(days.values())/len(days) # средние от суммы всех средних
        ls.append((max(days.values())-ans)+(ans-min(days.values()))) #Добавление аплитуды
    print(sum(ls)/len(ls))
a=10
for i in range(10):
    dig(a, a, a)
    a*=10



 
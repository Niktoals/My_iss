rows=int(input())
seats=[]
for i in range(rows):
    start_seats=input().split('_')
    seats.append(start_seats)
n_groups=int(input())
groups=[]
for i in range(n_groups):
    group=input().split()
    groups.append(group)
for i in groups:
    free_seats=[]
    new_string=''
    if i[2]=='aisle':
        for f in seats:
            if i[1]=='left' and f[0][-1:-int(i[0])-1:-1].count('.')==int(i[0]):
                if i[0]==3:
                    seats[seats.index(f)][0]='XXX'
                else:
                    new_string=seats[seats.index(f)][0]
                    seats[seats.index(f)][0]=new_string[:3-int(i[0]):]+'X'*int(i[0])
                for h in range(int(i[0])):
                    free_seats.append(str(seats.index(f)+1)+chr(67-h))
                free_seats.reverse()
                print('Passengers can take seats:', *free_seats, end='\n')
                break
            if i[1]=='right' and f[1][:int(i[0]):].count('.')==int(i[0]):
                if i[0]==3:
                    seats[seats.index(f)][1]='XXX'
                else:
                    new_string=seats[seats.index(f)][1]
                    seats[seats.index(f)][1]='X'*int(i[0])+new_string[-1:int(i[0])-1:-1]
                for h in range(int(i[0])):
                    free_seats.append(str(seats.index(f)+1)+chr(67+h))
                print('Passengers can take seats:', *free_seats, end='\n')
                break           
    if i[2]=='window':
        for f in seats:
            if i[1]=='left' and f[0][:int(i[0]):].count('.')==int(i[0]):
                if i[0]==3:
                    seats[seats.index(f)][0]='XXX'
                else:
                    new_string=seats[seats.index(f)][0]
                    seats[seats.index(f)][0]='X'*int(i[0])+new_string[-1:int(i[0])-1:-1]
                for h in range(int(i[0])):
                    free_seats.append(str(seats.index(f)+1)+chr(65+h))
                
                print('Passengers can take seats:', *free_seats, end='\n')
                break
            if i[1]=='right' and f[1][-1:-int(i[0])-1:-1].count('.')==int(i[0]):
                new_string=seats[seats.index(f)][1]
                seats[seats.index(f)][1]=new_string[:0-int(i[0]):]+'X'*int(i[0])
                for h in range(int(i[0])):
                    free_seats.append(str(seats.index(f)+1)+chr(70-h))
                free_seats.reverse()
                print('Passengers can take seats:', *free_seats, end='\n')
                break            
    if len(free_seats)==0:
        print('Cannot fulfill passengers requirements', end='\n')
    else:
        for k in range(len(seats)):
            print(*(seats[k][0]+'_'+seats[k][1]), sep='', end='\n')
            seats[k][0]=seats[k][0].replace('X', '#')
            seats[k][1]=seats[k][1].replace('X', '#')

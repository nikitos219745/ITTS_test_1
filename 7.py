while True:
    v=int(input('Length of list(0-100):'))
    if v<0 or v>100:
        print('Incorrect number!')
        continue
    a=[v]
    for i in range(v):
        a.append(int(input(f'[{i}]:')))
    c=0
    for i in range(v):
        if a[i]>a[i+1] and i!=0:
            print(f'Index of less number:[{i}]')
            c+=1
    print(f'Times:{c}')
    print('Print 1 to close program or other button to rerun')
    k=input()
    if k == '1':
        break
    else:
        continue

num=9
print('num/2',(num-1)//2)
for i in range(num):
    if i <= ((num-1) // 2):
       print('前几层',i)
    else:
        print('后面几层',i,((num-1)-i))


win = open("中獎發票.txt").read().split()
myreceipt = open("我的發票.txt").read().split()

counter = 1
for i in myreceipt:
    if i in win:
        print(f'第{counter}張發票中獎了，中獎號碼{i}!')
    counter += 1
    

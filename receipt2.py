from unicodedata import numeric


win = open("中獎發票2.txt").read().split()
myreceipt = open("我的發票2.txt").read().split()

for i, code in enumerate(myreceipt):
    for j in win:
        if code[2:] == j[2:]:
            if code[1:] == j[1:]:
                if code == j:
                    print(f'第{i+1}張中10000，號碼為{code}')
                else:
                    print(f'第{i+1}張中200，號碼為{code}')
            else:
                print(f'第{i+1}張中200，號碼為{code}')
        

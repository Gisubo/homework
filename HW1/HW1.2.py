import sys
if len(sys.argv) == 1:
    arr=[]
    file = sys.stdin.readlines()
    for line in file:
        arr.append(line)
    len_arr = 17 if len(arr) >= 17 else len(arr)
    for i in range(len_arr,0,-1):
        sys.stdout.write(arr[-i])
else:
    for j in range(1,len(sys.argv)):
        arr = []
        file = open(sys.argv[j],'r',encoding='utf_8_sig')
        for line in file:
            arr.append(line)
        len_arr = 10 if len(arr) >10 else len(arr)
        for i in range(len_arr,0,-1):
            sys.stdout.write(arr[-i])


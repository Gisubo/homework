import sys
file = sys.stdin.readlines() if len(sys.argv)==1 else open(sys.argv[1],'r',encoding='utf_8_sig')
i = 1
for line in file:
    sys.stdout.write(str(i)+' '+line)
    i+=1

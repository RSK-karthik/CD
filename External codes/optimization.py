l=[]
lhs=[]
rhs=[]
while True:
    line=input()
    if line=='}':
        break
    else:
        l.append(line)
print(l)
if l[0][0]=='f':
    loop_param=l[0][4]
else:
    loop_param=l[0][6]
loop=l.pop(0)
for exp in l:
    left=exp[:exp.index('=')]
    right=exp[exp.index('=')+1:]
    # print(lhs,rhs)
    lhs.append(left)
    rhs.append(right)
for_yes=[]
for_no=[]
for i in range(len(lhs)):
    if (lhs[i]==loop_param) or (lhs[i] in rhs[i]):
        for_yes.append(l[i])
    else:
        for_no.append(l[i])
print(loop)
for i in for_yes:
    print(i)
print('}')
for i in for_no:
    print(i)
#follow

n=int(input())
c=input()
s=[]
for i in range(n):
    s.append(input())

first={}
for i in s:
    x=i[0]
    if not i[3].isupper():
        first[x] = i[3]

for i in s:
    y=i[0]
    if i[3].isupper():
        if i[3] in first:
            first[y] = first[i[3]]

follow = {}

follow[c] = "$"
for i in s:
    x=i
    for j in range(3,len(i)):
        if x[j].isupper() and j==len(i)-1:
            follow[x[j]] = "follow of " + x[0]
        if x[j].isupper():
            if j+1<len(i):
                if x[j+1].isupper():
                    follow[x[j]] = first[x[j+1]]
                else:
                    follow[x[j]] = x[j+1]
print("First: ",first)
print("Follow: ",follow)

#first

n=int(input())
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

print("First: ",first)

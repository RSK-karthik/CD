#LL(1)

first = {"S":["c","a"],"A":["a"],"B":["c"]}

follow = {"S":["$","a","c"],"A":["$","a","c"],"B":["d"]}

prod = ["S->A","S->Bd","A->a","B->c"]

LL={}
t = ["a","c","d"]
non_t = ["S","A","B"]

for i in non_t:
    x=i
    d={}
    for j in prod:
        y = j[3]
        if j[0]==x:
            
            if y in t:
                if y in d:
                    d[y].append(j)
                else:
                    d[y] = [j]
            elif y in non_t:
                z = first[y]
                for q in z:
                    if q in d:
                        d[q].append(j)
                    else:
                        d[q] = [j]
            else:
                z = follow[x]
                for q in z:
                    if q in d:
                        d[q].append(j)
                    else:
                        d[q] = [j]
    LL[x] = d

# Check for multiple entries
multiple_entries = False
for nonterminal, entries in LL.items():
    for symbol, productions in entries.items():
        if len(productions) > 1:
            print(f"Multiple entries found for {nonterminal} -> {symbol}:")
            for production in productions:
                print(production)
            multiple_entries = True

if not multiple_entries:
    print("No multiple entries found.")

print(LL)
#count letter
def findinlist(x,li_input):
    for i in range (len(li_input)):
        if x== li_input[i]:
            return i
        
def countletter (n):
    a=[]
    b=[]
    for i in n:
        if i not in a:
            a.append(1)
            b.append(1)
        else:
            x=findinlist(i,a)
            b[x]+=1
    for i in range (len(a)):
        print(a[i], " ", b[i])
    
countletter("asdfdsgsa")
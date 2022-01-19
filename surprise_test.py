def expanding(lst):
    lst1 = []
    try:
        for i in range(len(lst)):
            out = (lst[i+1])-lst[i]
            lst1.append(abs(out))
    except:
        lst1.append(lst[-1])
    if sorted(lst1)==lst1:
        return True
    else:
        return False

lst = list(map(int,input().split()))
print(expanding(lst))
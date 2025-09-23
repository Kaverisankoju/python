li = [1,2,3,20,30,90]
search_val = 3
low = 0
high = len(li)-1
while low < high:
    mid = (low + high)//2
    if li[mid] == search_val:
        print(mid)
        break
    elif li[mid] > search_val:
        high = mid - 1
    else:
            low = mid + 1
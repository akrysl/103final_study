def merge(left, right):
    print("\nleft:", left, "\nright:", right)
    result = []
    i, j = 0, 0
    while (len(result) < len (left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left):
            result.extend(right[j:])
        if j == len(right):
            result.extend(left[i:])
    print("result", result)
    return result

def mergesort(list):
    if (len(list) < 2):
        return list

    middle = len(list)//2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)

print ("Final:", mergesort([3,11,4,5,1,2,12,8,3,7,6,9,10]))

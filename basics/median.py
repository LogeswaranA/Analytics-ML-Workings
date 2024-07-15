def find_median(listvalue):
    sortedlist = sorted(listvalue)
    n = len(sortedlist)

    if n % 2 == 1:
        return sortedlist[n // 2]
    else:
        mid1 = sortedlist[n // 2 - 1]
        mid2 = sortedlist[n // 2]
        return (mid1 + mid2 )/ 2

numbers = [5,1,3,2,1,5,6]
print(find_median(numbers))

# // operator is integer division operator, which divides and will round the results to nearest integer value
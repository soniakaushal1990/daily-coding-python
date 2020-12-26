def max_partition_sum(array,k):
    left, right= max(array),sum(array)
    while left < right:
        mid = (left+right)//2
        if(can_partition(array,mid,k)):
            right=mid
        else:
            left=mid+1          

    return left

def can_partition(array,limit,k):
    total=0
    partitions=1

    for num in array:
        if total+num > limit:
            total=num
            partitions += 1
            if partitions > k:
                return False
        else:
            total+=num
    return True


print(max_partition_sum([5, 1, 2, 7, 3, 4],3))
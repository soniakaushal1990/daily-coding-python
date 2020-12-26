def min_jumps(arr,jumps=0):
    if not arr or len(arr) == 1:
        return jumps

    if arr[0] == 0:
        return float("inf")
    moves = [min_jumps(arr[i:],jumps+1) for i in range(1,min(arr[0]+1,len(arr)))]
    return min(moves)


print(min_jumps([6,2,4,0,5,1,1,4,2,9]))
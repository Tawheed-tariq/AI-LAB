def LinearSearch(arr, target):
    for i in arr:
        if i == target:
            return i;
    return -1;


def BinarySearch(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left + (right - left)//2
        if(arr[mid] == target):
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid - 1
    return -1



if __name__ == "__main__":
    arr = [0,1,2,3,4,5,6]
    print(LinearSearch(arr, 4))
    print(BinarySearch(arr, 3))
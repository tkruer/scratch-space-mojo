fn quick_sort(borrowed arr: ListLiteral) -> object:    
    let left = []
    let right = []
    
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

fn main():
    let _arr = [1, 2, 3, 4, 5]
    
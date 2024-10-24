'''define array, and get the unique elements from the array preserving their order'''

def unique_elements(arr):
    seen = set(arr)
    print(dir(seen))
    print("seen :", seen)
    res = []
    for num in arr:
        if num in seen:
            res.append(num)
            seen.remove(num)
    return res
arr = [0,1,1,1,1,99,22,99,'e',1,2,2,22]  #[0,1,2,22]
print(unique_elements(arr))
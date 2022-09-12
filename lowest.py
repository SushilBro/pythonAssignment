numbers = [3,5,1,62,8,20,62]
def nth_lowest(b, n='sushil'):
    try:
        nums = set(b)
        if n == 'sushil':
            return min(b)
        else:
            if not type(n) is int:
                print("Only integers are allowed in second parameter")
            elif (len(b) >= n):
                nums = sorted(nums)
            else:
                print("Inputed length is greater than actual length!!!")
        return nums[n-1]
    except:
        print("Something went wrong!!")
    
    

print(nth_lowest(numbers,3))
print(nth_lowest('mynameissushilgautamiamapythondeveloper', 12))
print(nth_lowest(numbers, 4))
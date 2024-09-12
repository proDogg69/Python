def binary_searchv2(list, target):
    if len(list) == 0:
        return False 
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] <target:
                # midpoint + 1:
                # the ':' is important here
                return binary_searchv2(list[midpoint + 1:], target)
            else:
                return binary_searchv2(list[:midpoint], target)
            
def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]
result = binary_searchv2(numbers, 12)
verify(result)

result = binary_searchv2(numbers, 6)
verify(result)



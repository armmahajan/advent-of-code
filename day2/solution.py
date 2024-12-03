import collections
def findSafeLevels():
    with open('input.txt', 'r') as file:
        count = 0
        oneAllowedCount = 0
        for line in file:
            arr = line.split()
            arr = [int(i) for i in arr]
            if checkSafeLevel(arr):
                count += 1
            else:
                for i in range(len(arr)):
                    if checkSafeLevel(arr[:i] + arr[i+1:]):
                        count += 1
                        break
            # if checkSafeLevelOneAllowed(arr):
            #     oneAllowedCount += 1
            # elif checkSafeLevel(arr[1:]):
            #     oneAllowedCount += 1
        print(f"None allowed count : {count}") 
        print(f"One allowed count : {oneAllowedCount}") 

def checkSafeLevel(arr):
    diffs = []
    l, r = 0, 1
    while r < len(arr):
        # Calculate diff and store it 
        diff = arr[r] - arr[l]
        diffs.append(diff)

        # Increment Pointers
        l += 1
        r += 1
    
    # Check if diffs are within range and all pos/neg
    for i in range(len(diffs)):
        abs_diff = abs(diffs[i])
        if abs_diff < 1 or abs_diff > 3:
            return False
        if diffs[i] * diffs[0] <= 0:
            return False
    return True

def checkSafeLevelOneAllowed(arr):
    # Check monotonic increasing
    inc = True
    allowed = 1
    stack = []
    for i in arr:
        if not stack:
            stack.append(i)
            continue
        
        if i - stack[-1] >= 1 and i - stack[-1] <= 3:
            stack.append(i)
        else:
            allowed -= 1
        
        if allowed < 0: 
            inc = False
            break
    
    # Check monotonic decreasing
    dec = True
    allowed = 1
    stack = []
    for i in arr:
        if not stack:
            stack.append(i)
            continue
        
        if i - stack[-1] <= -1 and i - stack[-1] >= -3:
            stack.append(i)
        else:
            allowed -= 1
        
        if allowed < 0: 
            dec = False
            break
    if not dec and not inc:
        print(arr)
    return dec or inc

findSafeLevels()
import re

def multiplyAll(file):
    # Extract all mul commands from the file
    muls = []
    for line in file:
        muls += re.findall(r'mul\(\d+,\d+\)', line)

    # Calculate mul command and add it to result
    results = 0 
    for mul in muls:
        nums = re.findall(r'\d+', mul)
        results += int(nums[0]) * int(nums[1])
    
    print(results)

def multiplyDos(file):
    # Extract all mul commands from the file
    muls = []
    for line in file:
        muls += re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)

    # Optionally calculate mul command if "do" flag is set
    results = 0
    do = True
    for command in muls:
        if command == 'don\'t()':
            do = False
        elif command == 'do()':
            do = True
        else:
            if do:
                nums = re.findall(r'\d+', command)
                results += int(nums[0]) * int(nums[1])
    
    print(results)

# Handle file
with open('input.txt', 'r') as file:
    multiplyAll(file)
    file.seek(0)
    multiplyDos(file)
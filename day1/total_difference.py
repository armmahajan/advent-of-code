import collections

def findDifference():
    with open('input.txt', 'r') as input:
        # Read input file into arrays
        list1 = []
        list2 = []
        for line in input:
            line = line.split()
            list1.append(int(line[0]))
            list2.append(int(line[1]))

        # Sort lists
        list1.sort()
        list2.sort()

        # Calculate difference
        total_diff = 0
        for i in range(len(list1)):
            total_diff += abs(list1[i] - list2[i])

        print(total_diff)

def findSimilarityScore():
    with open('input.txt', 'r') as input:
        # Read input file into arrays
        list1 = []
        list2 = []
        for line in input:
            line = line.split()
            list1.append(int(line[0]))
            list2.append(int(line[1]))

        # Generate counts of each number 
        list1_set = set(list1)
        list2_count = collections.Counter(list2)

        similarity_score = 0
        for num in list1_set:
            if num not in list2_count:
                continue
            
            similarity_score += num * list2_count[num]
        
        print(similarity_score)

findSimilarityScore()
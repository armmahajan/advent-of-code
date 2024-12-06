import collections
# Handle file
with open('input.txt', 'r') as file:
    prereqs = collections.defaultdict(list)
    required_for = collections.defaultdict(list)
    orderings = []
    passed_reqs = False
    for line in file:
        if line == '\n':
            passed_reqs = True
            continue
        if not passed_reqs:
            required, other = line.strip().split('|')
            prereqs[int(other)].append(int(required))
            required_for[int(required)].append(int(other))
        if passed_reqs:
            orderings.append([int(i) for i in line.strip().split(',')])

    valid_orderings = []
    invalid_orderings = []

    for ordering in orderings:
        printed = set()
        valid = True
        for page in reversed(ordering):
            for i in prereqs[page]:
                if i in printed:
                    valid = False
                    break
            printed.add(page)
        
        if valid:
            valid_orderings.append(ordering)
        else:
            invalid_orderings.append(ordering)
    
    total = sum([ordering[len(ordering)//2] for ordering in valid_orderings])
    print(total)

    '''
        DFS through each path, if an explored node doesnt have any page_set matches
        return []
        if it has all the matches return [matches_list]
    '''
    def dfs(node, order, page_set, curr_set):
        if not page_set:
            return order
        matches = []
        for i in required_for[node]:
            if i in page_set:
                order_copy = order.copy()
                order_copy.append(i)
                page_copy = page_set.copy()
                page_copy.remove(i)
                curr_set_copy = curr_set.copy()
                curr_set_copy.add(i)
                matches.append(dfs(i, order_copy, page_copy, curr_set_copy))
        for i in matches:
            if i:
                return i
        return []

    res = 0
    for ordering in invalid_orderings:
        start = -1
        page_set = set(ordering)
        # Find node that doesnt contain any of the others as a prereq
        for page in ordering:
            is_start = True
            for prereq in prereqs[page]:
                if prereq in page_set:
                    is_start = False
                    break
            
            if is_start:
                start = page
        page_set.remove(start) 
        corrected = dfs(start, [start], page_set, set([start]))
        res += corrected[len(corrected)//2]
    
    print(res)
    
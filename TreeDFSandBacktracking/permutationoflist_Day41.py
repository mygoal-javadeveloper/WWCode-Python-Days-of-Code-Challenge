# Write a program that uses recursion to generate all permutations of a list

def permutelst(lst, idx=0):
    # using tree DFS and backtracking.
    if idx >= len(lst):
        print('Final:', lst)
        return
    for x in range(idx, len(lst)):
        lst[idx], lst[x] = lst[x], lst[idx]
        permutelst(lst, idx+1)
        lst[idx], lst[x] = lst[x], lst[idx]



lst = list(input('Enter the elements of the list separated by space: \n').strip().split())
permutelst(lst)
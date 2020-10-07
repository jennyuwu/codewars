# link: https://www.codewars.com/kata/523f5d21c841566fde000009/python
# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]

# My answer
def array_diff(a, b):
    list_diff = []
    for item in a:
        if item not in b:
            list_diff.append(item)

    return list_diff


# Another answer variation
def array_diff(a, b):
    return [x for x in a if x not in b]

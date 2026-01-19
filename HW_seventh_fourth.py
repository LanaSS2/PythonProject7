#create an intersection of sets with multiples of 3 in first list, and the second list of numbers which are multiples of 5

def common_elements():
    set1 = {x for x in range(100) if x % 3 == 0}
    set2 = {x for x in range(100) if x % 5 == 0}
    intersection_set = set1.intersection(set2)
    return intersection_set  #return set1 & set2


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("ОК")
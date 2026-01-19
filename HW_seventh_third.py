#find the index of the second entry of the second string in the first string.

def second_index(text: str, some_str: str):
    first = text.find(some_str)
    if first == -1:
        return None

    second = text.find(some_str, first + len(some_str))
    return None if second == -1 else second


print(second_index("sims", "s"))# == 3, 'Test1'
print(second_index("find the river", "e"))# == 12, 'Test2'
print(second_index("hi", "h"))#  is None, 'Test3'
print(second_index("Hello, hello", "lo"))#  == 10, 'Test4'
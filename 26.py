#level intermediate


def sum_list(num_list: list[float]) -> float:
    """Returns the sum of all numbers in the list."""
    run_total = 0
    for num in num_list:
        run_total = run_total + num
    return run_total
    

def test_sum_list_empty():
    assert sum_list([]) == 0

def test_sum_list_nonempty():
    assert sum_list([1, 2, 3]) == 6

    #assert takes anything that evalutates to true or false / boolean 

def product_list(num_list: list[float]) -> float: 
    """adds together the sums of all the numbers in a list and returns a singular product"""
    total = 1
    for nums in num_list: 
        total = total * nums
    return total

def test_product_list(): 
    assert product_list([ 1, 2, 3, 4]) == 24 


def count_occurrences(items: list[str], target: str) -> int: 
    """given a list, it returns how many times the target string appears in the list"""
    total = 0 
    for item in items: 
        if item == target: 
            total = total + 1 
    return total

def test_count_occurences(): 
    assert count_occurrences([], "hello") == 0

def test_count_occurences2(): 
    assert count_occurrences(["hi", "bye", "hi"], "hi") == 2

def filter_by_prefix(words: list[str], prefix: str) -> list[str]: 
    """given a list of words it returns a new list that just has the words with a certain prefix"""
    total = []
    for word in words: 
        if word.startswith(prefix) == word: 
            total = [] + [word]
    return total 
    
def test_filter_by_prefix(): 
    assert filter_by_prefix(["undo", "undone", "preorder", "indent"], "un") == ["undo", "undone"]


     
        
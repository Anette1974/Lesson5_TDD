from sum_list_folder.src.sum_list import sum_list

def test_sum_list__empty_list():
    expected = 0
    actual =  sum_list ([])
    assert actual == expected

def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([2, -15]) == -13
    assert sum_list([-10, 20, 8, 0]) == 18
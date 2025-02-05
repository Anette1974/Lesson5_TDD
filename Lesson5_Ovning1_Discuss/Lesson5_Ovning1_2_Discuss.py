print("Övning 1, del 2")
#Det har smugit sig in kommentarer i stället för kod på några ställen.
# Skriv färdigt testfallen test_empty_list och test_number_list.
# Returnerar summan av alla tal i listan
def sum_list(list):
    return None

sum_list(list)

def test_empty_list():
    expected =  7
    actual = add (4, 3)
    assert actual == expected

#test_empty_list()


def test_number_list():
    assert sum_list([5]) == 5  # Testar en lista med ett element
    assert sum_list([1, 2, 3]) == 6  # Testar en lista med flera positiva tal
    assert sum_list([-1, -2, -3]) == -6  # Testar en lista med negativa tal
    assert sum_list([]) == 0  # Testar en tom lista

    print("Alla tester passerade!")

test_number_list()  # Kör testerna
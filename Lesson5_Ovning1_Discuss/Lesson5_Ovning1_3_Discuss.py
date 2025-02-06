#3a Diskutera följande kod. Räcker det med ett testfall för att testa funktionen?
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    return None

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

#3b Skriv färdigt funktionen count_vowels med hjälp av TDD-metoden, red → green → refactor.


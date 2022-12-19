from AverageWordLength import calculateAverage


# /////////////////////Test assignment example
def test_case_1():
    input = 'The quick brown fox jumps over the lazy dog'
    print('User input is:', input)
    assert calculateAverage(input) == 3.89, "Test_case_1 Should be 3.89"
    print('The average of word length is:', calculateAverage(input))
    print('-------------------------------')


# /////////////////////Test assignment example
def test_case_2():
    input = 'All sentences might...not be punctually, correct.'
    print('User input is:', input)
    assert calculateAverage(input) == 5.57, "Test_case_2 Should be 5.57"
    print('The average of word length is:', calculateAverage(input))
    print('-------------------------------')


# /////////////////////Test new types of alphabets
def test_case_3():
    input = 'ä комбиниране Săedinenieto työpaikat'
    print('User input is:', input)
    assert calculateAverage(input) == 8.25, "Test_case_2 Should be 8.25"
    print('The average of word length is:', calculateAverage(input))
    print('-------------------------------')


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    print("Everything passed")

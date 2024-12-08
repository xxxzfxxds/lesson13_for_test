from functions import salary,Hello_who

def test_Hello_who_max():
    assert Hello_who("Max")=="Hello, Max"
    assert Hello_who("Max1") == "Hello, Max1"
    assert Hello_who("Max2") == "Hello, Max2"
    assert Hello_who("Max3") == "Hello, Max3"
    assert Hello_who("Max4") == "Hello, Max4"
    assert Hello_who("Max5") == "Hello, Max5"
    assert Hello_who("Max6") == "Hello, Max6"
    assert Hello_who("Max7") == "Hello, Max7"
def test_salary():
    assert (2,2)!=8

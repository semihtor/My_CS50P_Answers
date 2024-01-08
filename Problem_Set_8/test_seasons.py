from seasons import check_date_of_birth

def main():
    test_check_date_of_birth()

def test_check_date_of_birth():
    assert check_date_of_birth("111-11-11") == None
    assert check_date_of_birth("1111-111-11") == None
    assert check_date_of_birth("1111-11-111") == None
    assert check_date_of_birth("November 11th, 1111") == None
    assert check_date_of_birth("1985-05-03") == ('1985', '05', '03')

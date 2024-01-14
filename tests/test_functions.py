from coursework.src.functions import modify_date, modify_from, modify_to

def test_modify_date():
    assert modify_date("2018-04-16T17:34:19.241289") == "16-04-2018"
    assert modify_date("2018-02-13T04:43:11.374324") == "13-02-2018"
    assert modify_date("2018-07-22T07:42:32.953324") == "22-07-2018"

def test_modify_from():
    assert modify_from("Счет 33355011456314142963") == "Счет **2963"
    assert modify_from("Visa Platinum 1813166339376336") == "Visa Platinum 1813 16** **** 6336"
    assert modify_from("Maestro 1913883747791351") == "Maestro 1913 88** **** 1351"
    assert modify_from("") == "Открытие вклада"


def test_modify_to():
    assert modify_to("Счет 33355011456314142963") == "Счет **2963"
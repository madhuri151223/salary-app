from app import calculate_salary

def test_salary():
    assert calculate_salary(5000, 500) == 5500

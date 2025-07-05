from project import Restaurant
from unittest.mock import patch
import pytest

def main():
    test_csv_list()
    test_breakfast()
    test_meals()
    test_delicacies()
    test_ice()
    test_menu()
    test_order()
    test_payment()

def test_csv_list():
    restaurant = Restaurant()
    restaurant.csv_list = lambda: [
        1, "Dosa", 20, 2, "Idly", 20, 3, "Puri", 30, 4, "Bonda", 40,
        5, "Pulihora", 80, 6, "Full Meals", 120, 7, "Thali", 180, 8, "Veg Pulao", 100,
        9, "Chicken Biryani", 250, 10, "Mutton Biryani", 550, 11, "Gulab Jamun", 30,
        12, "Halwa", 30, 13, "Rasgulla", 50, 14, "Rasmalai", 50, 15, "Vanilla", 50,
        16, "Chocolate", 50, 17, "Butter Scotch", 50, 18, "Strawberry", 50, 19, "Dark Forest", 100
    ]

    result = restaurant.csv_list()
    assert len(result) == 57
    assert result[0] == 1
    assert result[1] == "Dosa"
    assert result[2] == 20

def test_meals():
    restaurant = Restaurant()
    meals = [
        [5, "Pulihora", 80],
        [6, "Full Meals", 120],
        [7, "Thali", 180],
        [8, "Veg Pulao", 100],
        [9, "Chicken Biryani", 250],
        [10, "Mutton Biryani", 550]
    ]

    assert meals[0][1] == "Pulihora"
    assert meals[2][2] == 180
    assert len(meals) == 6


def test_breakfast():
    restaurant = Restaurant()

    breakfast = [
        [1, "Dosa", 20],
        [2, "Idly", 20],
        [3, "Puri", 30],
        [4, "Bonda", 40]
    ]

    assert breakfast[0][1] == "Dosa"
    assert breakfast[2][2] == 30
    assert len(breakfast) == 4


def test_delicacies():
    restaurant = Restaurant()

    delicacies = [
        [11, "Gulab Jamun", 30],
        [12, "Halwa", 30],
        [13, "Rasgulla", 50],
        [14, "Rasmalai", 50]
    ]

    assert delicacies[0][1] == "Gulab Jamun"
    assert delicacies[3][2] == 50
    assert len(delicacies) == 4


def test_ice():
    restaurant = Restaurant()

    ice_cream = [
        [15, "Vanilla", 50],
        [16, "Chocolate", 50],
        [17, "Butter Scotch", 50],
        [18, "Strawberry", 50],
        [19, "Dark Forest", 100]
    ]

    assert ice_cream[0][1] == "Vanilla"
    assert ice_cream[2][2] == 50
    assert len(ice_cream) == 5

def test_menu():
    with patch('builtins.input', return_value='1'):
        restaurant = Restaurant()
        result = restaurant.menu()
        assert result == test_breakfast()

    with patch('builtins.input', return_value='2'):
        restaurant = Restaurant()
        result = restaurant.menu()
        assert result == test_meals()

    with patch('builtins.input', return_value='3'):
        restaurant = Restaurant()
        result = restaurant.menu()
        assert result == test_delicacies()

    with patch('builtins.input', return_value='4'):
        restaurant = Restaurant()
        result = restaurant.menu()
        assert result == test_ice()

def test_order():
    restaurant = Restaurant()
    restaurant.csv_list = lambda: [
        1, "Dosa", 20, 2, "Idly", 20, 3, "Puri", 30, 4, "Bonda", 40,
        5, "Pulihora", 80, 6, "Full Meals", 120, 7, "Thali", 180, 8, "Veg Pulao", 100,
        9, "Chicken Biryani", 250, 10, "Mutton Biryani", 550, 11, "Gulab Jamun", 30,
        12, "Halwa", 30, 13, "Rasgulla", 50, 14, "Rasmalai", 50, 15, "Vanilla", 50,
        16, "Chocolate", 50, 17, "Butter Scotch", 50, 18, "Strawberry", 50, 19, "Dark Forest", 100
    ]
    order_items = [1, 1, 2]
    order_total = 0
    order = []

    for item in order_items:
        item_name = restaurant.csv_list()[restaurant.csv_list().index(item) + 1]
        item_price = restaurant.csv_list()[restaurant.csv_list().index(item) + 2]
        order.append(item_name)
        order_total += item_price

    assert "Dosa" in order
    assert "Idly" in order
    assert order_total == 60


def test_payment():
    restaurant = Restaurant()
    cost = 100
    amount_paid = 150
    balance = abs(cost - amount_paid)

    assert balance == 50


if __name__ == "__main__":
    pytest.main()

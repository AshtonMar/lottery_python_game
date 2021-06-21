import unittest
from datetime import  date, timedelta

def test_validate_age(id_number):
    id_number = list(id_number)
    year = id_number[0] + id_number[1]
    month = id_number[2] + id_number[3]
    day = id_number[4] + id_number[5]
    date_of_birth = date(int(year), int(month), int(day))
    age = str((date.today() - date_of_birth) // timedelta(days=365.245))
    age = list(age)
    age = age[2] + age[3]
    age = int(age)
    result = age
    return result
class AgeValidate(unittest.TestCase):
    def setUp(self):
        self.valid_age = 18
        self.invalid_age = 17
    def test_gen_age(self):
        test_validate_age("0208075070085")
        self.assertTrue(self. valid_age >= 18 and self.invalid_age <= 17)
if __name__ == '__main__':
    unittest.main()

import random
def random_generated_numbers():
    x = random.sample(range(1, 49), 6)
    print(x)
    return x
class Randomness(unittest.TestCase):
    def setUp(self):
        self.a = 1
        self.b = 49
    def test_gen_number(self):
        random_generated_numbers()
        self.assertTrue(self.a >= 1 and self.b <=20)
if __name__ == '__main__':
    unittest.main()

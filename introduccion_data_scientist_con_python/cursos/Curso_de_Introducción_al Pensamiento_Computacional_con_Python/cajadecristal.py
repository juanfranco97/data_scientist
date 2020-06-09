import unittest

def is_adult(age):
    return (age >= 18)


class WhiteBoxTest(unittest.TestCase):
    
    def test_is_adult_true(self):
        age = 20
        result = is_adult(age)
        self.assertTrue(result)
    
    def test_is_adult_false(self):
        age = 10
        result = is_adult(age)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
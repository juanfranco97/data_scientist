def reverse_string(string):
    return string[::-1]


if __name__ == '__main__':
    import unittest

    class StringTests(unittest.TestCase):

        def setUp(self):
            self.strings = {
                'hola': 'aloh',
                'adios': 'soida',
                'roma': 'amor'
            }
        def test_reverse_string(self):
            for key, value in self.strings.items():
                self.assertEqual(key, reverse_string(value))

        def tearDown(self):
            del self.strings
    unittest.main()
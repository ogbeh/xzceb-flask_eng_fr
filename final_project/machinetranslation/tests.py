from translator import *
import unittest

class TestUtils(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        self.assertNotEqual(frenchToEnglish("Hola"), "Bonjour")

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertNotEqual(frenchToEnglish("Hola"), "Hello")


if __name__ == '__main__':
    unittest.main()

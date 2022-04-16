from translator import french_to_english, english_to_french
import unittest

class TestUtils(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("Hola"), "Bonjour")

    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(french_to_english("Hola"), "Hello")


if __name__ == '__main__':
    unittest.main()

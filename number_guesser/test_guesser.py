from number_guesser import choice
import unittest


class ChoiceTestCase(unittest.TestCase):
    def test_choice(self):
        result = choice(42, 25)
        self.assertEqual(result, 'little_less')

        result = choice(42, 50)
        self.assertEqual(result, 'little_more')

        result = choice(42, 42)
        self.assertEqual(result, 'well_done')


if __name__ == '__main__':
    unittest.main()

import unittest


class Homo:
    def get_safe(self):
        """ Homo is not safe to the duck, but why? """
        return False


class HomoTestCase(unittest.TestCase):
    """ Homo test """

    def test_is_safe(self):
        person = Homo()

        result = person.get_safe()

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

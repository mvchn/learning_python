import unittest
from models import Book


class BookTestCase(unittest.TestCase):
    """ Book test """

    def test_get_name(self):
        book = Book(1, 'test', 'test title', 55, 'category', 2)

        result = book.get_name()

        self.assertEqual(result, 'test title TEST')


if __name__ == '__main__':
    unittest.main()

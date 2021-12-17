import unittest
from Group_work5 import get_extention
from Group_work5 import count_digit


class CountDigitsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.num_list = [1, 1, 3, 2, 1, 3, 4]
        self.answer = {
            1: 3,
            2: 1,
            3: 2,
            4: 1
        }

    def test_succesful_work(self):
        self.assertEqual(count_digit(self.num_list), self.answer)


if __name__ == '__main__':
    unittest.main()


class TestExtensions(unittest.TestCase):
    def setUp(self) -> None:
        self.succesful_data = ["help.docx", "koka.txt", "main.pdf", "test.txt", "test1.csv"]
        self.succesful = ['docx', 'txt', 'pdf', 'txt', 'csv']
        self.wrong_data = ["help.docx", "koka", "main.pdf", "test.txt", "test1.csv"]

    def test_succesful(self):
        self.assertEqual(get_extention(self.succesful_data), self.succesful)

    def test_wrong(self):
        with self.assertRaises(EOFError) as context:
            get_extention(self.wrong_data)


if __name__ == '__main__':
    unittest.main()
import random
import unittest


def process_input_text(some_text):
    if some_text.isdigit():
        some_text = int(some_text)
        if some_text % 2 == 0:
            return "This number is even"
        else:
            return "This number is odd"
    elif some_text.isalpha():
        some_text = len(some_text)
        return f'This word has {some_text} letter'
    else:
        raise ValueError("Invalid input")


some_text = input("Write me something, please: ")
result = process_input_text(some_text)
print(result)


class MyTestClass(unittest.TestCase):
    def test_is_even(self):
        random_even_number = random.randint(1, 100000) * 2
        random_odd_number = random_even_number - 1
        self.assertEqual(process_input_text(str(random_even_number)), "This number is even")
        self.assertEqual(process_input_text(str(random_odd_number)), "This number is odd")

    def test_invalid_input(self):
        invalid_input = " "
        with self.assertRaisesRegex(ValueError, "Invalid input"):
            process_input_text(invalid_input)


if __name__ == '__main__':
    unittest.main()


def find_largest_number(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            largest_number = float('-inf')

            for line in lines:
                parts = line.split()
                if len(parts) == 2:
                    try:
                        current_number = int(parts[0])
                        largest_number = max(largest_number, current_number)
                    except ValueError:
                        pass

            return largest_number

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def find_words_for_numbers(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            number_word_mapping = {}

            for line in lines:
                parts = line.split()
                if len(parts) == 2:
                    try:
                        current_number = int(parts[0])
                        word = parts[1]
                        number_word_mapping[current_number] = word
                    except ValueError:
                        pass

            return number_word_mapping

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def concatenate_words(file_path):
    largest_number = find_largest_number(file_path)

    if largest_number is not None:
        number_word_mapping = find_words_for_numbers(file_path)
        if number_word_mapping is not None:
            concatenated_words = ""

            current_number = 1
            row = 1

            while current_number <= largest_number:
                last_number_in_row = current_number + row - 1
                word = number_word_mapping.get(last_number_in_row, "")
                concatenated_words += word + " "

                current_number += row
                row += 1

            print(f"{concatenated_words.strip()}")


file_path = 'text.txt'
concatenate_words(file_path)

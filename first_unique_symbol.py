"""
TASK:
Вам потрібно розробити алгоритм програми, яка повинна виконувати наступне:
- програма приймає на вхід довільний текст і знаходить в кожному слові цього тексту найперший символ, який більше НЕ
повторюється в аналізуємому слові
- далі із отриманого набору символів програма повинна вибрати перший унікальний (тобто той, який більше не
зустручається в наборі) і повернути його.
"""


def get_unique_letters_list(text: str) -> list or str:
    """Go through all words in text and find first unique letter in it"""
    if len(text) == 0:
        raise ValueError('Text should not be empty')
    else:
        unique_letters_list = []  # result list
        paragraphs = text.split('\n')
        for paragraph in paragraphs:
            words = paragraph.split(" ")
            for word in words:
                for letter in word:
                    if word.count(letter) == 1 and letter.isalpha():
                        unique_letters_list.append(letter)
                        break
        return unique_letters_list


def get_one_unique_letter(text: str) -> str:
    """Analyze letters from previous step and return one that is unique"""
    unique_letter_list = get_unique_letters_list(text)
    if len(unique_letter_list) == 0:
        return 'There is no unique letter. Maybe you provide no letters. Try other text.'
    for letter in unique_letter_list:
        if unique_letter_list.count(letter) == 1:
            return f"First unique letter is - '{letter}'"


unique_letter = get_one_unique_letter(""" """)  # provide your text here, please
print(unique_letter)

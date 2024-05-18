"""
Модуль с функциями для работы с CSV файлами, хранящими данные.
"""


def get_from_csv(filename):
    """Достает данные из CSV файла"""
    data = []
    with open(f"./data/{filename}.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            first, second, third = line[:-1].split(";")
            data.append([cnt, first, second, third])
            cnt += 1
    return data


def get_csv_count(filename):
    """Считает количество строк (записей) в CSV файле"""
    with open(f"./data/{filename}.csv", "r", encoding="utf-8") as f:
        count = len(f.readlines()) - 1
        return count


def write_word(new_word, translation, comment="-"):
    """Записывает слово в соответствующий CSV файл"""
    new_word_line = f"{new_word};{translation};{comment}\n"
    with open("./data/words.csv", "a", encoding="utf-8") as f:
        f.write(new_word_line)


def delete_word(word_id):
    """Удаляет слово из соответствующего CSV файла"""
    with open("./data/words.csv", "r", encoding="utf-8") as f:
        existing_words = [l.strip("\n") for l in f.readlines()]
        title = existing_words[0]
        old_words = existing_words[1:]
    old_words.pop(word_id)
    new_words = [title] + old_words
    with open("./data/words.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_words))
        f.write("\n")

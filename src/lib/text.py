import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    This function brings the text to a standard form.
    What exactly does it do:
      It converts to lowercase (casefold).
      Removes extra spaces and special characters.
      Replaces ё --> e (yo2e).

    Return returns the new text
    '''
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё','е')
    text = text.replace('\t', ' ').replace('\r', ' ')
    text = text.strip()
    text = ' '.join(text.split())
    return text


def tokenize(text: str) -> list[str]:
    '''
    This function splits the text into words (tokens).

    '''
    pattern = r"\w+(?:-\w+)*"
    tokens = re.findall(pattern, text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str,int]:
    '''
    This function It counts how many times each
    unique token is repeated.
    '''
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str,int], n: int = 5) -> list[tuple[str,int]]:
    top = list(freq.items())
    top.sort(key=lambda x:(-x[1], x[0]))
    return top[:n]


if __name__ == "__main__":
    print("Время для тестов")

    assert normalize("ПрИвЕт\nМир\t") == "привет мир", "Ошибка: пробелы/регистр"
    assert normalize("ёжик, Ёлка") == "ежик, елка", "Ошибка: замена ё"
    print("normalize: OK")

    assert tokenize("привет, мир!") == ["привет", "мир"], "Ошибка: пунктуация"
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"], "Ошибка: дефис"
    assert tokenize("2025 год") == ["2025", "год"], "Ошибка: цифры"
    print("tokenize: OK")

    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}, "Ошибка: неверный подсчет"
    print("count_freq: OK")

    assert top_n(freq, 2) == [("a", 3), ("b", 2)], "Ошибка: неверный топ"
    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)], "Ошибка: не в алфавитном порядке"
    print("top_n: OK")

    print("Ура!")

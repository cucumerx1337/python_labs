import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Приводит текст к единому регистру, заменяет ё на е и убирает лишние пробелы."""
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    for ch in ("\t", "\r", "\n"):
        text = text.replace(ch, " ")

    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    """Разбивает строку на токены (слова с дефисами внутри и цифры)."""
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает частоту появления каждого слова."""
    freq = {}
    for word in tokens:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает n самых частых слов с сортировкой по частоте и алфавиту."""
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]


if __name__ == "__main__":
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"

    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]

    f = count_freq(["a", "b", "a", "c", "b", "a"])
    assert f == {"a": 3, "b": 2, "c": 1}
    assert top_n(f, 2) == [("a", 3), ("b", 2)]

    f2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(f2, 2) == [("aa", 2), ("bb", 2)]
    print("OK")

from text_stats import normalize, tokenize, count_freq, top_n

def test_normalize():
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир", "Ошибка: пробелы/регистр"
    assert normalize("ёжик, Ёлка") == "ежик, елка", "Ошибка: замена ё"
    print("normalize: OK")

def test_tokenize():
    assert tokenize("привет, мир!") == ["привет", "мир"], "Ошибка: пунктуация"
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"], "Ошибка: дефис"
    assert tokenize("2025 год") == ["2025", "год"], "Ошибка: цифры"
    print("tokenize: OK")

def test_count_freq():
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}, "Ошибка: неверный подсчет"
    print("count_freq: OK")

def test_top_n():
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert top_n(freq, 2) == [("a", 3), ("b", 2)], "Ошибка: неверный топ"
    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)], "Ошибка: не в алфавитном порядке"
    print("top_n: OK")

if __name__ == "__main__":
    print("Время для тестов")
    test_normalize()
    test_tokenize()
    test_count_freq()
    test_top_n()
    print("Ypa!")

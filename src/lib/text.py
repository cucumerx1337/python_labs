import re

_CONTROL_RE = re.compile(r"[\x00-\x1f\x7f-\x9f]")
_SPACES_RE = re.compile(r"\s+")
_TOKEN_RE = re.compile(r"\w+(?:-\w+)*")


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Привести текст к нормальному виду."""
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")  # ё -> е
    text = text.casefold() if casefold else text.lower()
    text = _CONTROL_RE.sub(" ", text)  # \t, \r, \n -> пробел
    return _SPACES_RE.sub(" ", text).strip()  # схлопнуть пробелы


def tokenize(text: str) -> list[str]:
    """Разбить текст на слова (\\w+ и дефис внутри слова)."""
    return _TOKEN_RE.findall(text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитать частоты слов."""
    freq: dict[str, int] = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Топ-N по убыванию частоты, при равенстве по алфавиту."""
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]

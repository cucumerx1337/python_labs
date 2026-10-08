import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from lib.text import count_freq, normalize, tokenize, top_n

USE_TABLE_VIEW = False


def main():
    raw_input = sys.stdin.read()
    if not raw_input.strip():
        return

    words = tokenize(normalize(raw_input))
    freq = count_freq(words)
    top_words = top_n(freq, n=5)

    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    if USE_TABLE_VIEW and top_words:
        col_width = max(len("слово"), max(len(w) for w, _ in top_words))
        print(f"{'слово':<{col_width}} | частота")
        print("-" * (col_width + 11))
        for word, count in top_words:
            print(f"{word:<{col_width}} | {count}")
    else:
        for word, count in top_words:
            print(f"{word}:{count}")


if __name__ == "__main__":
    main()

from pathlib import Path
import sys

# Добавляем путь к корню репозитория
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.lib.tables import check_rows


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Считывает текстовый файл и возвращает его содержимое в виде строки.

    Параметры:
        path: путь к файлу (строка или объект Path)
        encoding: кодировка (по умолчанию utf-8)

    Ошибки:
        FileNotFoundError: если файл отсутствует
        ValueError: если путь указывает на директорию
    """
    target = Path(path)

    if not target.exists():
        raise FileNotFoundError(f"Файл не найден: {target}")
    if not target.is_file():
        raise ValueError(f"Путь не является файлом: {target}")

    return target.read_text(encoding=encoding)


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """Записывает строки данных в CSV-файл.

    Параметры:
        rows: список кортежей или списков со значениями
        path: путь для сохранения CSV
        header: опциональный кортеж названий колонок

    Ошибки:
        ValueError: если строки не совпадают по длине с заголовком или путь является папкой
    """
    target = Path(path)

    if target.exists() and not target.is_file():
        raise ValueError(f"Невозможно перезаписать директорию: {target}")

    # Валидация входных данных
    if header is not None:
        check_rows(rows, header)
    else:
        check_rows(rows)

    # Создание родительской папки при отсутствии
    if not target.parent.exists():
        target.parent.mkdir(parents=True, exist_ok=True)

    # Запись в файл
    with target.open("w", encoding="utf-8") as file:
        if header is not None:
            file.write(",".join(header) + "\n")
        for row in rows:
            file.write(",".join(str(val) for val in row) + "\n")


if __name__ == "__main__":
    test_mode = 0

    if test_mode == 0:
        write_csv([("word", "count"), ("test", 3)], "src/lab04/data/check.csv")
        print(read_text("src/lab04/data/check.csv"), "\n------------")

        write_csv(
            [("word", "count"), ("test", 3)],
            "src/lab04/data/check.csv",
            header=("word", "count"),
        )
        print(read_text("src/lab04/data/check.csv"), "\n------------")

        write_csv([], "src/lab04/data/check.csv", header=None)
        print(read_text("src/lab04/data/check.csv"), "\n------------")

        write_csv([], "src/lab04/data/check.csv", header=("word", "count"))
        print(read_text("src/lab04/data/check.csv"), "\n------------")

    elif test_mode == 1:
        print(read_text("src/lab04/data/check.csv"))
        print(read_text("src/lab04/data/check.csv", encoding="utf-8"))

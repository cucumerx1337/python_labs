import csv
import json
from json import JSONDecodeError
from pathlib import Path
import sys

# Добавляем путь к корню репозитория
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


def check_headers(data: list[dict]) -> None:
    """Проверяет одинаковость набора ключей во всех записях."""
    if not data:
        return
    reference_keys = data[0].keys()
    for row in data:
        if row.keys() != reference_keys or None in row:
            raise ValueError("Несогласованный состав или количество полей в строках")


def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    """Конвертирует JSON-файл со списком объектов в CSV-файл.

    Параметры:
        json_path: путь к исходному JSON-файлу
        csv_path: путь для сохранения результирующего CSV-файла

    Ошибки:
        FileNotFoundError: если исходный файл не существует
        TypeError: если корневой элемент JSON не является списком
        ValueError: если JSON некорректен, пуст или содержит элементы, не являющиеся словарями
    """
    json_target = Path(json_path)
    csv_target = Path(csv_path)

    if not json_target.exists():
        raise FileNotFoundError(f"Файл не найден: {json_target}")
    if not json_target.is_file():
        raise ValueError(f"Указанный путь не является файлом: {json_target}")

    try:
        with json_target.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except JSONDecodeError as e:
        raise ValueError(f"Ошибка декодирования JSON: {e}")

    if not isinstance(data, list):
        raise TypeError("Корневой элемент JSON должен быть списком")
    if len(data) == 0:
        raise ValueError("JSON-список не должен быть пустым")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы списка должны быть словарями")

    all_keys = set()
    for row in data:
        all_keys.update(row.keys())

    headers = sorted(list(all_keys))

    if not csv_target.parent.exists():
        csv_target.parent.mkdir(parents=True, exist_ok=True)

    with csv_target.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    """Конвертирует CSV-файл в JSON-файл со списком объектов.

    Параметры:
        csv_path: путь к исходному CSV-файлу
        json_path: путь для сохранения JSON-файла

    Ошибки:
        FileNotFoundError: если исходный файл не существует
        ValueError: если CSV некорректен, пуст или не содержит строк с данными
    """
    csv_target = Path(csv_path)
    json_target = Path(json_path)

    if not csv_target.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_target}")
    if not csv_target.is_file():
        raise ValueError(f"Указанный путь не является файлом: {csv_target}")

    with csv_target.open("r", encoding="utf-8") as f:
        sample = f.read(2048)
        if not sample.strip():
            raise ValueError("CSV-файл не должен быть пустым")
        f.seek(0)

        sniffer = csv.Sniffer()
        try:
            dialect = sniffer.sniff(sample)
        except csv.Error:
            dialect = csv.excel

        if not sniffer.has_header(sample):
            raise ValueError("CSV-файл должен содержать заголовок")

        reader = csv.DictReader(f, dialect=dialect)
        data = list(reader)

    if len(data) == 0:
        raise ValueError("CSV-файл должен содержать как минимум одну строку с данными")
    check_headers(data)

    if not json_target.parent.exists():
        json_target.parent.mkdir(parents=True, exist_ok=True)

    with json_target.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    sample_json = ROOT_DIR / "data/samples/people.json"
    out_csv = ROOT_DIR / "data/out/people_from_json.csv"
    out_json = ROOT_DIR / "data/out/people_from_csv.json"

    print("=" * 60)

    try:
        print("Test 1: JSON -> CSV")
        with open(sample_json, "r", encoding="utf-8") as f:
            initial_json_len = len(json.load(f))

        json_to_csv(sample_json, out_csv)

        with open(out_csv, "r", encoding="utf-8") as f:
            resulting_csv_len = len(f.readlines()) - 1

        print(f" -> Zapisi JSON: {initial_json_len}")
        print(f" -> Zapisi CSV: {resulting_csv_len}")

        assert initial_json_len == resulting_csv_len, "Error"
        print(" Success")
        print("-" * 60)

        print("Test 2: CSV -> JSON")
        csv_to_json(out_csv, out_json)

        with open(out_json, "r", encoding="utf-8") as f:
            final_json_len = len(json.load(f))

        print(f" -> Zapisi CSV: {resulting_csv_len}")
        print(f" -> Zapisi JSON: {final_json_len}")

        assert resulting_csv_len == final_json_len, "Error"
        print(" Success")
        print("=" * 60)

    except Exception as e:
        print(f"\nError: {e}")

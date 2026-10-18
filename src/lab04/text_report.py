import argparse
from multiprocessing import Process, Queue
from pathlib import Path
import sys

# Добавляем корень проекта в список путей поиска
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.lab04.io_txt_csv import check_rows, read_text, write_csv
from src.lib.tables import check_rows, create_table
from src.lib.text import count_freq, normalize, tokenize, top_n

SUPPORTED_FLAGS = ["--in", "--per-file", "--total", "--encoding"]


def args_parser(raw_args: list[str]) -> dict[str, list[str]]:
    """Вспомогательный разбор аргументов командной строки."""
    parsed: dict[str, list[str]] = {}
    active_flag = None

    for item in raw_args:
        if item in SUPPORTED_FLAGS:
            if item not in parsed:
                parsed[item] = []
            active_flag = item
            continue

        if active_flag:
            parsed[active_flag].append(item)

    return parsed


def report_for_each(
    file_paths: list[str], output_csv: str, raw_texts: list[str], queue: Queue
):
    """Подсчет частот слов индивидуально для каждого входного файла."""
    try:
        file_records = []
        for idx, text in enumerate(raw_texts):
            tokens = tokenize(text)
            frequencies = count_freq(tokens)
            words_top = top_n(frequencies, n=-1)
            for word, count in words_top:
                file_records.append([file_paths[idx], word, count])

        queue.put((1, file_records))
    except Exception as exc:
        queue.put((1, exc))


def report_for_all(output_csv: str, raw_texts: list[str], queue: Queue):
    """Суммарный подсчет частот слов по всем файлам вместе."""
    try:
        combined = "\n".join(raw_texts)
        tokens = tokenize(combined)
        frequencies = count_freq(tokens)
        total_top = list(top_n(frequencies, n=-1))

        queue.put((2, total_top))
    except Exception as exc:
        queue.put((2, exc))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Генерация отчетов по частотам слов (ЛР4)"
    )

    parser.add_argument(
        "--in",
        nargs="+",
        required=True,
        dest="input_files",
        help="Пути к входным текстовым файлам",
    )
    parser.add_argument(
        "--per-file",
        default="src/lab04/data/reports/report_per_file.csv",
        help="Файл для пофайлового отчета",
    )
    parser.add_argument(
        "--total",
        default="src/lab04/data/reports/report_total.csv",
        help="Файл для общего сводного отчета",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Кодировка входных файлов",
    )

    args = parser.parse_args()

    per_file_dest = args.per_file
    total_dest = args.total

    # Считываем и нормализуем текст из всех переданных файлов
    normalized_texts = []
    for filepath in args.input_files:
        raw_content = read_text(path=filepath, encoding=args.encoding)
        normalized_texts.append(normalize(raw_content, casefold=True))

    # Запускаем параллельные процессы для подготовки отчетов
    task_queue = Queue()

    process_each = Process(
        target=report_for_each,
        name="Process-PerFile",
        args=[args.input_files, per_file_dest, normalized_texts, task_queue],
    )
    process_all = Process(
        target=report_for_all,
        name="Process-Total",
        args=[total_dest, normalized_texts, task_queue],
    )

    process_each.start()
    process_all.start()

    process_each.join()
    process_all.join()

    # Собираем данные из очереди
    results = {}
    for _ in range(2):
        task_id, data = task_queue.get()
        results[task_id] = data

    for task_id, data in results.items():
        if isinstance(data, BaseException):
            print(f"Ошибка выполнения в подпроцессе {task_id}: {data}")
            raise data

        if task_id == 1:
            write_csv(data, path=per_file_dest, header=("file", "word", "count"))
            print(create_table(header=("file", "word", "count"), rows=data))
        elif task_id == 2:
            write_csv(rows=data, path=total_dest, header=("word", "count"))
            print(create_table(header=("word", "count"), rows=data))

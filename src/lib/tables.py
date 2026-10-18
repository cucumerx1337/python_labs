def check_rows(
    rows: list[tuple | list], header: tuple[str, ...] | None = None
) -> None:
    """Проверка корректности структуры строк перед записью или выводом."""
    if header is not None:
        header_len = len(header)
        for row in rows:
            if len(row) != header_len:
                raise ValueError(
                    f"Длина строки {len(row)} не совпадает с количеством колонок в заголовке {header_len}"
                )
    else:
        for row in rows:
            if any(item == "" for item in row):
                raise ValueError(f"Обнаружена пустая ячейка в строке: {row}")


def create_table(header: tuple[str, ...], rows: list[tuple | list]) -> str:
    """Генерация таблицы с рамками из псевдографики."""
    check_rows(header=header, rows=rows)

    # Определяем ширину каждой колонки
    col_widths = []
    for idx, col_name in enumerate(header):
        content_max = max((len(str(r[idx])) for r in rows), default=0)
        col_widths.append(max(len(col_name), content_max))

    # Формируем горизонтальные линии
    top_line = "┌" + "┬".join("─" * (w + 2) for w in col_widths) + "┐\n"
    mid_line = "├" + "┼".join("─" * (w + 2) for w in col_widths) + "┤\n"
    bot_line = "└" + "┴".join("─" * (w + 2) for w in col_widths) + "┘\n"

    # Шапка
    header_line = (
        "│ "
        + " │ ".join(f"{header[i]:<{col_widths[i]}}" for i in range(len(header)))
        + " │\n"
    )

    # Строки с данными
    row_lines = []
    for r in rows:
        formatted_row = "│ " + " │ ".join(
            f"{str(r[i]):<{col_widths[i]}}" for i in range(len(header))
        ) + " │\n"
        row_lines.append(formatted_row)

    return top_line + header_line + mid_line + "".join(row_lines) + bot_line

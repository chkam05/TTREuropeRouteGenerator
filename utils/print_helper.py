import textwrap
from typing import List, Any


class PrintHelper:
    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static utility class and cannot be instantiated.")

    @staticmethod
    def _format_line(row_cells, separator: str, col_widths: List[int]):
        return separator.join(f" {cell.ljust(col_widths[i])} " for i, cell in enumerate(row_cells))

    @staticmethod
    def _max_word_len(text):
        return max((len(word) for word in text.split()), default=0)

    @staticmethod
    def _print_border_line(length: int):
        print('+' + '-' * (length - 2) + '+')

    @staticmethod
    def _print_separator(col_widths: List[int]):
        line = "+"
        for w in col_widths:
            line += "-" * (w + 2) + "+"
        print(line)

    @staticmethod
    def _wrap_row(row, col_widths: List[int]):
        wrapped = [
            textwrap.wrap(cell.strip(), width=col_widths[i], break_long_words=False) or [""]
            for i, cell in enumerate(row)
        ]
        max_lines = max(len(lines) for lines in wrapped)
        return [
            [lines[i] if i < len(lines) else '' for lines in wrapped]
            for i in range(max_lines)
        ]

    @staticmethod
    def print_block(text: str, align: int = 0, max_length: int = 100, print_bottom_line: bool = True):
        spaces = max_length - (len(text) + 4)
        PrintHelper._print_border_line(max_length)

        if align <= 0:
            print('| ' + text + ' ' * spaces + ' |')
        elif align == 1:
            left = spaces // 2
            right = spaces - left
            print('| ' + ' ' * left + text + ' ' * right + ' |')
        else:
            print('| ' + ' ' * spaces + text + ' |')

        if print_bottom_line:
            PrintHelper._print_border_line(max_length)

    @staticmethod
    def print_table(headers: List[str], content: List[List[Any]], max_width: int = 100, separator='|'):
        # Convert all cells to string
        rows = [[str(cell) for cell in headers]] + [[str(cell) for cell in row] for row in content]
        num_cols = max(len(row) for row in rows)

        # Normalize row lengths
        for row in rows:
            while len(row) < num_cols:
                row.append("")

        # Initial column widths based on longest word in each column
        col_widths = [
            max(
                max(PrintHelper._max_word_len(row[i]) for row in rows),
                len(headers[i]) if i < len(headers) else 0
            )
            for i in range(num_cols)
        ]

        # Available space for content (excluding + signs and padding)
        border_chars = num_cols + 1           # '+' between and around columns
        padding_spaces = 2 * num_cols         # space left and right of each cell
        available_width = max_width - border_chars - padding_spaces
        total_raw_width = sum(col_widths)

        # Scale down if total exceeds available
        if total_raw_width > available_width:
            scale = available_width / total_raw_width
            col_widths = [max(1, int(w * scale)) for w in col_widths]

        # Adjust to fit exactly
        current = sum(col_widths)
        diff = available_width - current
        i = 0
        while diff != 0:
            col = i % num_cols
            if diff > 0:
                col_widths[col] += 1
                diff -= 1
            elif diff < 0 and col_widths[col] > 1:
                col_widths[col] -= 1
                diff += 1
            i += 1

        # Print header
        PrintHelper._print_separator(col_widths)
        for line in PrintHelper._wrap_row(rows[0], col_widths):
            print(f"|{PrintHelper._format_line(line, separator, col_widths)}|")
        PrintHelper._print_separator(col_widths)

        # Print rows
        for row in rows[1:]:
            for line in PrintHelper._wrap_row(row, col_widths):
                print(f"|{PrintHelper._format_line(line, separator, col_widths)}|")
        PrintHelper._print_separator(col_widths)

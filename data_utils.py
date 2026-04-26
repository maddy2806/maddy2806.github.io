"""EX09 - Data related utility functions."""

__author__ = "730764815"
__author__ = "730647310"

from csv import DictReader


def get_keys(
    input_dict: (
        dict[str, list[str]]
        | dict[str, list[int]]
        | dict[str, list[str | int]]
        | dict[str, int]
        | dict[str, str]
    ),
) -> list[str]:
    """Return the keys of a dictionary as a list"""
    result: list[str] = []
    for key in input_dict:
        result.append(key)
    return result


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into row based table."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="ut18")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all values in a single column."""
    result: list[str] = []
    for row in table:
        result.append(row[column])
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table into column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(data: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Return the first rows of a column-based table."""
    result: dict[str, list[str]] = {}
    for column in data:
        result[column] = data[column][:n]
    return result


def select(data: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Return a table with only selected columns."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = data[column]
    return result


def concat(
    data1: dict[str, list[str]], data2: dict[str, list[str]]
) -> dict[str, list[str]]:
    """Combine two column-based tables."""
    result: dict[str, list[str]] = {}
    for column in data1:
        result[column] = data1[column][:]

    for column in data2:
        if column in result:
            result[column] += data2[column]
        else:
            result[column] = data2[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Count how many times each value appears in a list."""
    result: dict[str, int] = {}
    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result


def convert_columns_to_int(
    data: dict[str, list[str]], columns_conv: list[str]
) -> dict[str, list[str | int]]:
    """Convert selected columns to integers"""
    result: dict[str, list[str | int]] = {}
    for column in data:
        result[column] = []
        for value in data[column]:
            if column in columns_conv and value != "":
                result[column].append(int(value))
            else:
                result[column].append(value)
    return result


def average_rating(values: list[str]) -> float:
    """Return the adverage of non-empty numeric rating values."""
    total: int = 0
    count_values: int = 0
    for value in values:
        if value != "":
            total += int(value)
            count_values += 1
    if count_values == 0:
        return 0.0
    return total / count_values

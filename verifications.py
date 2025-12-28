import pandas as pd
from datetime import datetime

def cell1_check(row):
    cell1 = row[0]
    if pd.isna(cell1):
        return (False, "Пустая ячейка")
    try:
        temp = int(cell1)
        return (True, "")
    except (TypeError, ValueError):
        return (False, "Не является числом")

def cell2_check(row):
    cell2 = row[1]
    if pd.isna(cell2):
        return (False, "Пустая ячейка")
    if cell2 != "ИБМ":
        return (False, "Не соответствует значению 'ИБМ'")
    return (True, "")

def cell3_check(row):
    cell3 = row[2]
    if pd.isna(cell3):
        return (False, "Пустая ячейка")
    return (True, "")

def cell4_check(row):
    cell4 = row[3]
    if pd.isna(cell4):
        return (False, "Пустая ячейка")
    try:
        date = pd.to_datetime(cell4)
        return (True, "")
    except (ValueError, TypeError):
        return (False, "Не является датой")

def cell5_check(row):
    cell5 = row[4]
    if pd.isna(cell5):
        return (False, "Пустая ячейка")
    try:
        date = pd.to_datetime(cell5)
        return (True, "")
    except (ValueError, TypeError):
        return (False, "Не является датой")

def cell6_check(row):
    cell6 = row[5]
    if pd.isna(cell6):
        return (False, "Пустая ячейка")
    return (True, "")

def cell7_check(row):
    cell7 = row[6]
    if pd.isna(cell7):
        return (False, "Пустая ячейка")
    try:
        date = pd.to_datetime(cell7)
        return (True, "")
    except (ValueError, TypeError):
        return (False, "Не является датой")

def cell8_check(row):
    cell8 = row[7]
    if pd.isna(cell8):
        return (False, "Пустая ячейка")
    return (True, "")

def cell9_check(row):
    cell9 = row[8]
    if pd.isna(cell9):
        return (False, "Пустая ячейка")
    return (True, "")

def cell10_check(row):
    cell10 = row[9]
    if pd.isna(cell10):
        return (False, "Пустая ячейка")
    return (True, "")

def cell11_check(row):
    cell11 = row[10]
    if pd.isna(cell11):
        return (False, "Пустая ячейка")
    if cell11 != "ИБМ":
        return (False, "Не соответствует значению 'ИБМ'")
    return (True, "")

def cell12_check(row):
    cell12 = row[11]
    if pd.isna(cell12):
        return (False, "Пустая ячейка")
    return (True, "")

def cell13_check(row):
    cell13 = row[12]
    if pd.isna(cell13):
        return (False, "Пустая ячейка")
    return (True, "")

def cell14_check(row):
    cell14 = row[13]
    if pd.isna(cell14):
        return (False, "Пустая ячейка")
    try:
        if "," in cell14:
            temp_dates = cell14.split(",")
        else:
            temp_dates = [cell14]
        dates = []
        for date in temp_dates:
            dates.append(date.split("от")[1].strip().split(" ")[0])

        for date in dates:
            try_date = pd.to_datetime(date, format='%d.%m.%Y')
        return (True, "")
    except (ValueError, TypeError, IndexError):
        return (False, "Не является датой")

def dates_comparation45(date4, date5):
    if date4 >= date5:
        return (True, "")
    else:
        return (False, "Дата уведомления ТО раньше даты события")

def dates_comparation75(date7, date5):
    if date7 >= date5:
        return (True, "")
    else:
        return (False, "Дата уведомления СК раньше даты события")

def dates_comparation5t(date5):
    if (datetime.today() - date5).days > 5:
        return (False, "Проверить заполнение данных по уведомлениям ТО и СК")
    return (True, "")

def dates_comparation145(date14, date5):
    if "," in date14:
        temp_dates = date14.split(",")
    else:
        temp_dates = [date14]
    dates = []
    for date in temp_dates:
        dates.append(date.split("от")[1].strip().split(" ")[0])

    for date in dates:
        if date5 <= pd.to_datetime(date, format='%d.%m.%Y'):
            return (False, "Дата события раньше даты полиса")
    return (True, "")

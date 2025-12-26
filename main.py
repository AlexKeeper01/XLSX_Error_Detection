import pandas as pd
import json
from verifications import *


CONFIG_PATH = "data/config.json"

def parce_rows(table, config):
    start = 0
    end = len(table)

    if config["start_row"] != "None":
        start = int(config["start_row"]) - 7
    if config["end_row"] != "None":
        end = int(config["end_row"]) - 7

    result = []
    for i in range(start, end):
        row = table.iloc[i]
        temp = []
        for j in range(int(config["columns"])):
            temp.append(row.iloc[j])
        result.append(temp)
    return result


def feedback_index(row, col, config):
    return config["columns_names"][col] + " " + str(row + 7)

def error_print(errors_array, config):
    count = 0
    if config["exact_row_num"] == "None" and config["exact_col_char"] == "None":
        for error in errors_array:
            print(error[0])
            count += 1
    elif config["exact_row_num"] != "None" and config["exact_col_char"] == "None":
        for error in errors_array:
            if " " + config["exact_row_num"] + " " in " " + error[1] + " ":
                print(error[0])
                count += 1
    elif config["exact_row_num"] == "None" and config["exact_col_char"] != "None":
        for error in errors_array:
            if config["exact_col_char"] + " " in " " + error[1] + " ":
                print(error[0])
                count += 1
    else:
        for error in errors_array:
            if config["exact_row_num"] + " " in " " + error[1] + " " and config["exact_col_char"] + " " in " " + error[1] + " ":
                print(error[0])
                count += 1
    if count == 0:
        print("Ошибки не обнаружены!")


def check_all(table, config):
    errors = []
    for i in range(len(table)):
        row = table[i]

        res_1 = cell1_check(row, config)
        if not res_1[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 0, config)}: {res_1[1]}",
                           feedback_index(i, 0, config), res_1[1]])

        res_2 = cell2_check(row, config)
        if not res_2[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 1, config)}: {res_2[1]}",
                           feedback_index(i, 1, config), res_2[1]])

        res_3 = cell3_check(row, config)
        if not res_3[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 2, config)}: {res_3[1]}",
                           feedback_index(i, 2, config), res_3[1]])

        res_4 = cell4_check(row, config)
        if not res_4[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 3, config)}: {res_4[1]}",
                           feedback_index(i, 3, config), res_4[1]])

        res_5 = cell5_check(row, config)
        if not res_5[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 4, config)}: {res_5[1]}",
                           feedback_index(i, 4, config), res_5[1]])

        if res_4[0] and res_5[0]:
            res_4_5 = dates_comparation45(pd.to_datetime(row[3]), pd.to_datetime(row[4]))
            if not res_4_5[0]:
                errors.append([f"Ошибка в ячейках {feedback_index(i, 3, config)} и {feedback_index(i, 4, config)}: {res_4_5[1]}",
                               feedback_index(i, 3, config) + " " + feedback_index(i, 4, config), res_4_5[1]])

        res_6 = cell6_check(row, config)
        if not res_6[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 5, config)}: {res_6[1]}",
                           feedback_index(i, 5, config), res_6[1]])

        res_7 = cell7_check(row, config)
        if not res_7[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 6, config)}: {res_7[1]}",
                           feedback_index(i, 6, config), res_7[1]])

        if res_7[0] and res_5[0]:
            res_7_5 = dates_comparation75(pd.to_datetime(row[6]), pd.to_datetime(row[4]))
            if not res_7_5[0]:
                errors.append([f"Ошибка в ячейках {feedback_index(i, 6, config)} и {feedback_index(i, 4, config)}: {res_7_5[1]}",
                               feedback_index(i, 6, config) + " " + feedback_index(i, 4, config), res_7_5[1]])

        if (res_7[1] == "Пустая ячейка" or res_4[1] == "Пустая ячейка") and res_5[0]:
            res_5t = dates_comparation5t(pd.to_datetime(row[4]))
            if not res_5t[0]:
                errors.append([f"Предупреждение из ячейки {feedback_index(i, 4, config)}: {res_5t[1]}",
                               feedback_index(i, 4, config), res_5t[1]])

        res_8 = cell8_check(row, config)
        if not res_8[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 7, config)}: {res_8[1]}",
                           feedback_index(i, 7, config), res_8[1]])

        res_9 = cell9_check(row, config)
        if not res_9[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 8, config)}: {res_9[1]}",
                           feedback_index(i, 8, config), res_9[1]])

        res_10 = cell10_check(row, config)
        if not res_10[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 9, config)}: {res_10[1]}",
                           feedback_index(i, 9, config), res_10[1]])

        res_11 = cell11_check(row, config)
        if not res_11[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 10, config)}: {res_11[1]}",
                           feedback_index(i, 10, config), res_11[1]])

        res_12 = cell12_check(row, config)
        if not res_12[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 11, config)}: {res_12[1]}",
                           feedback_index(i, 11, config), res_12[1]])

        res_13 = cell13_check(row, config)
        if not res_13[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 12, config)}: {res_13[1]}",
                           feedback_index(i, 12, config), res_13[1]])

        res_14 = cell14_check(row, config)
        if not res_14[0]:
            errors.append([f"Ошибка в ячейке {feedback_index(i, 13, config)}: {res_14[1]}",
                           feedback_index(i, 13, config), res_14[1]])

        if res_5[0] and res_14[0]:
            res_14_5 = dates_comparation145(row[13], pd.to_datetime(row[4]))
            if not res_14_5[0]:
                errors.append([f"Ошибка в ячейках {feedback_index(i, 13, config)} и {feedback_index(i, 4, config)}: {res_14_5[1]}",
                               feedback_index(i, 13, config) + " " + feedback_index(i, 4, config), res_14_5[1]])


    return errors


if __name__ == "__main__":
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    table = pd.read_excel(config["database_path"], header=5, usecols="A:AI", dtype=str).dropna(how="all")
    parced_result = parce_rows(table, config)
    all_errors = check_all(parced_result, config)
    error_print(all_errors, config)





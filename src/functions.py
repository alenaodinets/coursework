import json
import os.path
from datetime import datetime

def load_operations():
    """открываем файл """
    operations_json = os.path.join("../../coursework", "operations.json")
    with open(operations_json, "r", encoding="utf-8") as file:
        convert_js = json.load(file)
    return convert_js

def sorted_list(file):
    """создаем список с EXECUTED, сортируем по дате и выводим
     последние пять"""
    new_data = []
    for item in file:
        if item == {}:
            continue
        elif item["state"] == "EXECUTED":
            new_data.append(item)
    sort_data = sorted(new_data, key=lambda x: x["date"], reverse=True)
    five_last_operations = sort_data[:5]
    return five_last_operations

def modify_date(data):
    """форматируем дату
    :param data: "2019-08-26T10:50:58.294041"
    :return "26-08-2019"
    """
    format_date = datetime.fromisoformat(data.replace("T", " "))
    return format_date.strftime("%d-%m-%Y")

def modify_to(bill):
    """форматирует данные счета получателя
    :param bill "Счет 11492155674319392427"
    :return "Счет **2427"""
    account_number_silens = f"{bill[:4]} **{bill[-4:]}"
    return account_number_silens

def modify_from(bill):
    """форматирует данные счета отправителя
        :param bill "Maestro 1913883747791351"
        :return "Maestro 1913 88** **** 1351"""
    if bill[0] == "С":
        silent = f"{bill[:4]} **{bill[-4:]}"
    elif bill[0] != "С":
        silent = f"{bill[:-12]} {bill[-12:-10]}** **** {bill[-4:]}"
    return silent

def format_operation(transaction):
    """Вывод полной оформленной информации"""
    transaction["date"] = modify_date(transaction["date"])
    if transaction.get("from") is None:
        transaction["from"] = "Открытие вклада"
    else:
        transaction["from"] = modify_from(transaction["from"])
    transaction["to"] = modify_to(transaction["to"])
    return f"{transaction["date"]} {transaction["description"]}\n{transaction["from"]} -> {transaction["to"]}\n{transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]}."



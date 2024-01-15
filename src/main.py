from coursework.src.functions import sorted_list, load_operations, format_operation

file = load_operations()
date = sorted_list(file)
for trans in date:
    formated = format_operation(trans)
    print(f"{formated}\n")

with open("list.csv", "r") as list_file:
    contents = list_file.read().splitlines()

    for row in contents:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} year old and {row_data[2]}")

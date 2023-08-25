flight_table = [
    ("P1", "VSCode", 100, "MID"),
    ("P23", "Eclipse", 234, "MID"),
    ("P93", "Chrome", 189, "High"),
    ("P42", "JDK", 9, "High"),
    ("P9", "CMD", 7, "High"),
    ("P87", "NotePad", 23, "Low")
]

def print_flight_table(table):
    print("P_ID\tProcess\tStart Time\tPriority")
    print("-" * 40)
    for row in table:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}")

def sort_flight_table(table, sort_option):
    if sort_option == 1:
        sorted_table = sorted(table, key=lambda x: x[0])
    elif sort_option == 2:
        sorted_table = sorted(table, key=lambda x: x[2])
    elif sort_option == 3:
        sorted_table = sorted(table, key=lambda x: x[3])
    else:
        print("Invalid sorting option.")
        return None
    return sorted_table

print("Flight Table:")
print_flight_table(flight_table)

print("\nSorting Options:")
print("1. Sort by P_ID")
print("2. Sort by Start Time")
print("3. Sort by Priority")

sort_option = int(input("\nEnter sorting option: "))
sorted_flight_table = sort_flight_table(flight_table, sort_option)

if sorted_flight_table:
    print("\nSorted Flight Table:")
    print_flight_table(sorted_flight_table)
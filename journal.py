import utils

while True:
    print("Menu:")
    print("1. Add a new entry")
    print("2. View previous entries")
    print("3. Summarize entries")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 4:
        break
    elif choice == 1:
        utils.write_new_entry()
        print("New Entry Added")
    elif choice == 2:
        utils.list_entries()
    elif choice == 3:
        utils.summarize()
    else:
        print("No Such Choice. Enter again")


print("Finish")

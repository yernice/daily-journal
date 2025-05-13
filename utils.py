from datetime import datetime
import os

def write_new_entry():
    today = datetime.now()
    new_entry = open(f"journal_entries\{today.day}-{today.month}-{today.year}.txt", "a")
    time = today.strftime("%H:%M")
    new_entry.write(f"{time}\n")

    print("Write your entry and type 'EOF' on a separate line to inicate end of an entry:")
    paragraph = []
    while True:
        line = input()
        if line == "EOF":
            break
        paragraph.append(line)
    
    entry = "\n".join(paragraph)
    new_entry.write(entry)
    new_entry.write("\n\n")
    new_entry.close()

def list_entries():
    num = 1
    print("These are all the entries: ")
    for entry in os.listdir("journal_entries"):
        print(f"{num}. {entry}")
        num += 1

    while True:
        print("Do you want to check the contents of any of them? y/n")
        choice = input("Enter a letter: ")
        if choice.lower() == 'n':
            break
        
        choice = int(input("Which one? Enter a number: "))
        num = 1        
        for entry in os.listdir("journal_entries"):
            if num == choice:
                read = open(f"journal_entries\{entry}")
                print(read.read())
                num -= 1
                read.close()

                break

            num += 1
            
        if num == choice:
            print("No such entry")

def summarize():
    for entry in os.listdir("journal_entries"):
        print(f"------------{entry}------------")
        read = open(f"journal_entries\{entry}")
        print(read.read())
        print("\n\n")
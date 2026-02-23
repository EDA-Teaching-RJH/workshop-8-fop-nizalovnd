import csv

def main():
    with open("contacts.csv", "r") as contacts:
        reader = csv.DictReader(contacts, delimiter=",")
        for line in reader:
            print(f"Person name is: {line["name"]} and their email is:{line["email"]}")

if __name__ == "__main__":
    main()
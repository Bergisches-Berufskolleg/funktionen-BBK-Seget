def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def main():
    year = int(input("Bitte gib ein Jahr ein: "))
    if isLeapYear(year):
        print(f"{year} ist ein Schaltjahr.")
    else:
        print(f"{year} ist kein Schaltjahr.")

if __name__ == "__main__":
    main()

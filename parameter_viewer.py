import csv

PARAMETER_FILE = "control_parameters.csv"


def display_parameters() -> None:
    try:
        with open(PARAMETER_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("No control parameter data found.")
                return

            print("\nCONTROL PARAMETER DATA")
            print("-" * 40)

            for row in rows:
                print(" | ".join(row))

    except FileNotFoundError:
        print("Control parameter file not found.")
    except OSError as error:
        print(f"Error reading control parameter data: {error}")


if __name__ == "__main__":
    display_parameters()

import csv
import logging
# logging cofigurations
logging.basicConfig(
    filename="app.log",              # Log file name
    level=logging.DEBUG,             # Log all levels DEBUG and above
    format="%(asctime)s - %(levelname)s - %(message)s" # Format for logging
)


with open('attendance_score.csv', newline='') as file:

    csv_reader = csv.DictReader(file)  # Create DictReader

    student_list = list(csv_reader)  # List to store dictionaries

def average_score(data):
    """Calculates the average of the 'Score' column in a CSV DictReader."""
    try:
        scores = [float(row['Score']) for row in data if row['Score']]
        if not scores:
            raise ValueError("No valid scores found.")
        return sum(scores) / len(scores)
    except KeyError:
        print("Error: The 'Score' column is missing in the CSV file.")
        return None
    except ValueError as e:
        print(f"Value error: {e}")
        return None


avg = average_score(student_list)
if avg is not None:
    print(f"Average Score: {avg:.2f}")



# to run this code use =>>   python practice.py
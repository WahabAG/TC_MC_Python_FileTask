import csv
import logging

with open('attendance_score.csv', 'r') as file:

    csv_reader = csv.DictReader(file)  # Create DictReader

    student_list = []  # List to store dictionaries
    for row in csv_reader:
        student_list.append(row) #appending all dictionary to a list



logging.basicConfig(
    filename="app.log",              # Log file name
    level=logging.DEBUG,             # Log all levels DEBUG and above
    format="%(asctime)s - %(levelname)s - %(message)s" # Format for logging
)


# working on average calculation
def average(data):
# calculating average of score in the score column
    try:
        logging.info("Program started")
        # Extract all valid scores into a list
        scores = []
        for student in data:
            value = student.get("Score") # check it's not empty or None
            if value:  
                scores.append(float(value))  # convert to float and append to score list

        if not scores:
            raise ValueError("No valid scores found.")
        logging.info("Score calculated")

        # Compute average
        return sum(scores) / len(scores)
        
    except ValueError as e:
        logging.error(ValueError)
        print(f"Value error: {e}")
        return None

avg = average(student_list)
if avg is not None:
    print(f"Average Score: {avg:.2f}")


# to run this code use =>>   python practice.py
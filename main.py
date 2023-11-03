import re
import json
# Define a dictionary with days of the week and associated tests
test_schedule = {
    "Monday": "Blood tests",
    "Tuesday": "X-rays",
    "Wednesday": "CT scans",
    "Thursday": "Ultrasounds",
    "Friday": "MRIs",
    "Saturday": "None",
    "Sunday": "None"
}

# Define a function to handle user input and search for test
def search_test():
    # Get user input and suggest search terms using regex
    search_term = input("Enter a test name: ")
    suggestions = [day for day in test_schedule.keys() if re.search(search_term, day, re.IGNORECASE)]
    if suggestions:
        print("Did you mean:")
        for suggestion in suggestions:
            print(suggestion)
    # Search for test and return associated day
    for day, test in test_schedule.items():
        if re.search(search_term, test, re.IGNORECASE):
            print(f"{test} is typically performed on {day}.")
            return
    print(f"Test '{search_term}' not found.")

# Run the program
search_test()
tests = [
    {"name": "Pro BNP", "day": "شنبه یکشنبه دوشنبه سشنبه چهارشنبه", "machine": "کوباس", "personnel": "خانم ترابی"},
    {"name": "Test 2", "day": "Tuesday", "machine": "Machine 2", "personnel": "Mary"},
    {"name": "Test 3", "day": "Wednesday", "machine": "Machine 1", "personnel": "Bob"},
]

def search_test(name):
    for test in tests:
        if test["name"].startswith(name):
            return f"Test: {test['name']}, Day: {test['day']}, Machine: {test['machine']}, Personnel: {test['personnel']}"
    return "Test not found"

test_name = input("Enter test name: ")
result = search_test(test_name)
print(result)
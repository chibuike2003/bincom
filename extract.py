# import re
# import os


# # Read the contents of the file
# with open("name.txt", "r") as file:
#     full_name = file.read()

# # Extract first name, middle name, and last name using regex
# name_pattern = r"^([A-Za-z]+)\s+([A-Za-z]+)\s+([A-Za-z]+)$"
# matches = re.match(name_pattern, full_name)

# if matches:
#     first_name = matches.group(1)
#     middle_name = matches.group(2)
#     last_name = matches.group(3)

#     print("First Name:", first_name)
#     print("Middle Name:", middle_name)
#     print("Last Name:", last_name)
# else:
#     print("Invalid name format in the file.")

# file_path = os.path.abspath("name.txt")
# print("File Path:", file_path)


# def extract_baby_names(filename):
#     # Read the contents of the file
#     with open(filename, "r") as file:  # Fix: Use the variable 'filename' instead of 'baby_names.txt'
#         data = file.read()

#     # Extract baby names using regex
#     name_pattern = r"\b[A-Za-z]+\b"  # assuming baby names consist of only alphabetical characters
#     baby_names = re.findall(name_pattern, data)

#     return baby_names


# def sort_names(names):
#     # Implementing a simple sorting algorithm (e.g., Bubble Sort)
#     n = len(names)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if names[j] > names[j+1]:
#                 names[j], names[j+1] = names[j+1], names[j]


# def binary_search(names, target):
#     # Implementing binary search
#     low = 0
#     high = len(names) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if names[mid] == target:
#             return mid
#         elif names[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1  # target not found


# def test_baby_names():
#     # Test extraction of baby names
#     filename = "baby_names.txt"
#     expected_names = ['Emma', 'Liam', 'Olivia', 'Noah', ...]  # Replace '...' with the rest of the expected names
#     extracted_names = extract_baby_names(filename)
#     assert extracted_names == expected_names, "Extraction of baby names failed."

#     # Test sorting of names
#     sorted_names = sorted(expected_names)
#     sort_names(extracted_names)
#     assert extracted_names == sorted_names, "Sorting of names failed."

#     # Test binary search
#     target_name = 'Emily'
#     expected_index = -1  # 'Emily' is not in the expected_names list
#     index = binary_search(extracted_names, target_name)
#     assert index == expected_index, "Binary search failed for name not in the list."

#     target_name = 'Emma'
#     expected_index = 0  # 'Emma' is at index 0 in the expected_names list
#     index = binary_search(extracted_names, target_name)
#     assert index == expected_index, "Binary search failed for name in the list."

#     # Add more test cases as needed

#     print("All test cases passed.")


# # Run the test
# test_baby_names()



















import re
import os


# Read the contents of the file
with open("name.txt", "r") as file:
    full_name = file.read()

# Extract first name, middle name, and last name using regex
name_pattern = r"^([A-Za-z]+)\s+([A-Za-z]+)\s+([A-Za-z]+)$"
matches = re.match(name_pattern, full_name)

if matches:
    first_name = matches.group(1)
    middle_name = matches.group(2)
    last_name = matches.group(3)

    print("First Name:", first_name)
    print("Middle Name:", middle_name)
    print("Last Name:", last_name)
else:
    print("Invalid name format in the file.")

file_path = os.path.abspath("name.txt")
print("File Path:", file_path)


def extract_baby_names(filename):
    # Read the contents of the file
    with open(filename, "r") as file:  # Fix: Use the variable 'filename' instead of 'baby_names.txt'
        data = file.read()

    # Extract baby names using regex
    name_pattern = r"\b[A-Za-z]+\b"  # assuming baby names consist of only alphabetical characters
    baby_names = re.findall(name_pattern, data)

    return baby_names


def sort_names(names):
    # Implementing a simple sorting algorithm (e.g., Bubble Sort)
    n = len(names)
    for i in range(n):
        for j in range(0, n-i-1):
            if names[j] > names[j+1]:
                names[j], names[j+1] = names[j+1], names[j]


def binary_search(names, target):
    # Implementing binary search
    low = 0
    high = len(names) - 1

    while low <= high:
        mid = (low + high) // 2
        if names[mid] == target:
            return mid
        elif names[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # target not found


def test_baby_names():
    # Test extraction of baby names
    filename = "baby_names.txt"
    expected_names = ['Emma', 'Liam', 'Olivia', 'Noah', '...']  # Replace '...' with the rest of the expected names
    extracted_names = extract_baby_names(filename)
    assert extracted_names == expected_names, "Extraction of baby names failed."

    # Test sorting of names
    sorted_names = sorted(expected_names)
    sort_names(extracted_names)
    assert extracted_names == sorted_names, "Sorting of names failed."

    # Test binary search
    target_name = 'Emily'
    expected_index = -1  # 'Emily' is not in the expected_names list
    index = binary_search(extracted_names, target_name)
    assert index == expected_index, "Binary search failed for name not in the list."

    target_name = 'Emma'
    expected_index = 0  # 'Emma' is at index 0 in the expected_names list
    index = binary_search(extracted_names, target_name)
    assert index == expected_index, "Binary search failed for name in the list."

    # Add more test cases as needed

    print("All test cases passed.")


# Run the test
test_baby_names()

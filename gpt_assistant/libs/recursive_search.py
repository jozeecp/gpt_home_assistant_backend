def recursive_search(data, search_string):
    if isinstance(data, dict):
        for key, value in data.items():
            if recursive_search(value, search_string):
                return True
    elif isinstance(data, list):
        for item in data:
            if recursive_search(item, search_string):
                return True
    elif isinstance(data, str):
        if search_string in data:
            return True
    return False


def search_dicts(list_of_dicts, search_string):
    matches = []
    for dict_item in list_of_dicts:
        if recursive_search(dict_item, search_string):
            matches.append(dict_item)
    return matches


# Example usage:
# list_of_dicts = [
#     {'name': 'John', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'swimming']},
#     {'name': 'Jane', 'age': 25, 'city': 'Chicago', 'hobbies': ['painting', 'cycling']},
#     {'name': 'Doe', 'age': 35, 'city': 'Los Angeles', 'hobbies': ['writing', 'hiking']},
#     {'name': 'Sam', 'age': 40, 'city': 'San Francisco', 'hobbies': [{'indoor': 'chess', 'outdoor': 'fishing'}]}
# ]

# search_string = 'chess'
# matches = search_dicts(list_of_dicts, search_string)
# print(matches)

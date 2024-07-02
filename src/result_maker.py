import json
from files import CSV_FILE_PATH, JSON_FILE_PATH, RESULT_FILE_PATH
from csv import DictReader

books_list = []
new_users = []
books_count = 0
users_count = 0

with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)

for user in users:
    user_json = {
        "name": user['name'],
        "gender": user['gender'],
        "address": user['address'],
        "age": user['age'],
        "books": []
    }
    new_users.append(user_json)


with open (CSV_FILE_PATH, newline='') as books:
    reader = DictReader(books)

    for row in reader:
        del row['Publisher']
        books_list.append(row)


while books_count < len(books_list):
    new_users[users_count]['books'].append(books_list[books_count])
    books_count += 1
    users_count += 1
    if users_count == len(new_users):
        users_count = 0

with open(RESULT_FILE_PATH, 'w') as result:
    json.dump(new_users, result, indent=4)

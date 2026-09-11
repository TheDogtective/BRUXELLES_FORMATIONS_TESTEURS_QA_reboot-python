"""
Exercice 1 — Reboot Python
Les consignes sont dans enonce.md (section EXO 1).
"""

users = [
    {"id": 1,  "name": "Alice",   "age": 25, "active": True,  "role": "admin"},
    {"id": 2,  "name": "Bob",     "age": 17, "active": False, "role": "user"},
    {"id": 3,  "name": "Charlie", "age": 32, "active": True,  "role": "user"},
    {"id": 4,  "name": "Diana",   "age": 16, "active": True,  "role": "user"},
    {"id": 5,  "name": "Evan",    "age": 42, "active": False, "role": "admin"},
    {"id": 6,  "name": "Fatima",  "age": 29, "active": True,  "role": "organizer"},
    {"id": 7,  "name": "Gael",    "age": 15, "active": True,  "role": "user"},
    {"id": 8,  "name": "Hana",    "age": 38, "active": True,  "role": "organizer"},
    {"id": 9,  "name": "Igor",    "age": 51, "active": False, "role": "user"},
    {"id": 10, "name": "Julia",   "age": 22, "active": True,  "role": "user"},
    {"id": 11, "name": "Karim",   "age": 19, "active": True,  "role": "user"},
    {"id": 12, "name": "Lena",    "age": 17, "active": True,  "role": "user"},
    {"id": 13, "name": "Marco",   "age": 45, "active": True,  "role": "admin"},
    {"id": 14, "name": "Nadia",   "age": 28, "active": False, "role": "organizer"},
    {"id": 15, "name": "Omar",    "age": 33, "active": True,  "role": "user"},
    {"id": 16, "name": "Priya",   "age": 14, "active": False, "role": "user"},
]


# ----- Partie A : les bases -----

# Q1 — Afficher le nom de chaque utilisateur.

""" # define the function
def display_all_users(users):
    for user in users:
        print(user["name"])

# function's call
display_all_users(users)

 """
# Q2 — Afficher uniquement les utilisateurs actifs.

""" def active_users(users):
    for user in users:
        if user["active"] == True:
            print(user["name"])

active_users(users)
 """
# Q3 — Compter les utilisateurs actifs et afficher "<n> utilisateurs actifs".

def user_count(users):
    count = 0
    for user in users:
        if user["active"] == True:
            count +=1
    return count

# print(f'{user_count(users)} utilisateurs actifs')




# Q4 — Afficher uniquement les utilisateurs majeurs (18 ans ou plus).

""" def adult_users(users):
    for user in users:
        if user["age"] >= 18:
            print(user)

adult_users(users) """

# Q5 — Afficher les utilisateurs qui sont à la fois actifs ET majeurs.

""" def adult_active_users(users):
    for user in users:
        if user["age"] >= 18 and user["active"] == True:
            print(user)

adult_active_users(users)
 """

# ----- Partie B : les fonctions -----

# Q6
""" def is_adult(user):
        return user["age"] >= 18
for user in users:
    statut_majeur = is_adult(user)
    print(f"{user['name']} (Âge: {user['age']}) -> Majeur: {statut_majeur}") """

# Q7
""" def get_active_users(users):
    # return [u for u in users if u["active"]]  version rapide : compréhension de liste
    active_users = []
    for user in users:
        if user["active"]: 
            active_users.append(user)
    return active_users
print(get_active_users(users)) """

# Q8
""" def get_active_adults(users):
    adult_active_users = []
    for user in users:
        if user["age"] >= 18 and user["active"]:
            adult_active_users.append(user)
    return adult_active_users
print(get_active_adults(users))
     """


# Q9
""" def find_user_by_id(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
print(find_user_by_id(users, 3))
print(find_user_by_id(users, 999))
 """

# ----- Partie C : le challenge -----

# Q10
def get_statistics(users):
    dict_stat = {
    "total": len(users),
    "active": user_count(users),
    "inactive": len([user for user in users if not user["active"]]),
    "adults": len([user for user in users if user["age"] >= 18]),
    "minors": len([user for user in users if user["age"] < 18])
    }
    return dict_stat

print(get_statistics(users))           
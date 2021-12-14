def users_hobby(users, hobby, result):
    with open(users, "rt") as f:
        lst_users = f.readlines()
    with open(hobby, "rt") as f:
        lst_hobby = f.readlines()
    for _ in range(len(lst_hobby), len(lst_users)):
        lst_hobby.append(None)
    users_hobby = {u.strip(): h.strip().split(",") if h else "" for u, h in zip(lst_users, lst_hobby)}

    with open(result, "wt") as f:
        for i in users_hobby.items():
            f.write(f"{i[0]}: {', '.join(i[1]) if i[1] else ''}\n")

users_hobby("users.csv", "hobby.csv", "users_hobby.csv")

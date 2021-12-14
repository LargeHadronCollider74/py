def users_hobby(users, hobby, result):
    try:
        f_u = open(users, "rt")
        f_h = open(hobby, "rt")
        f_r = open(result, "wt")
        u = f_u.readline()
        h = f_h.readline()
        while u:
            f_r.write(f"{u.strip()}: {h.strip() if h else ''}\n")
            u = f_u.readline()
            if h:
                h = f_h.readline()
    except:
        raise
    finally:
        f_u.close()
        f_h.close()
        f_r.close()

users_hobby("users.csv", "hobby.csv", "users_hobby2.csv")

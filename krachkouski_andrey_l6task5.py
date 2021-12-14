import sys

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


if (3 < len(sys.argv)):
    users_hobby(sys.argv[1], sys.argv[2], sys.argv[3])
    print('Finish')
else:
    print('Using: "l6 task5.py" users_file_name hobby_file_name result_file_name')


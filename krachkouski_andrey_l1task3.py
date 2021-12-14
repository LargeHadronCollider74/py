for i in range(101):
    postfix = "процент"
    if ((11 <= i) and (i <= 19)) or ((i % 10) in (0,5,6,7,8,9)):
        postfix = postfix + "ов"
    elif ((i % 10) in (2,3,4)):
        postfix = postfix + "а"

    print(f"{i} {postfix}")



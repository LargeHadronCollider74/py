duration = 0
while 1:
    try:
        result = input("duration [sec]: ")
        duration = int(result)
        if (0 > duration):
            print("only positive number allowed!")
            continue
        break
    except ValueError:
        print("only integer number allowed!")
    except KeyboardInterrupt as e:
        duration = -1
        print(f"\r\ninterrupted..")
        break
    except Exception as e:
        duration = -1
        print(f"\r\nerror - {e=}")
        break
# while 1:
#     result = input(invoce)
#     if result.isnumeric():
#         duration = int(result)
#     print("number only allowed!")
if (0 <= duration):
    if (60 > duration):
        print(f"{duration} sec")
    elif (60*60 > duration):
        print(f"{duration//60} min {duration%60} sec")
    elif (24*60*60 > duration):
        hour = duration // 3600
        min = (duration%3600) // 60
        sec = duration%60
        print(f"{hour} h {min} min {sec} sec")
    else:
        day = duration // (24*3600)
        hour = (duration % (24*3600)) // 3600
        min =(duration % 3600) // 60
        sec = duration % 60
        print(f"{day} day {hour} h {min} min {sec} sec")



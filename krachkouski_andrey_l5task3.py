import sys
import itertools

def tuple_gen():
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Николай', 'Иван', 'Харитон', 'Ульяна', 'Яков']
    klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
    # if (len(klasses) > len(tutors)):
    #     klasses = klasses[0:len(tutors)]
    # return ((t, k) for t, k in itertools.zip_longest(tutors, klasses))
    for _ in range(len(klasses), len(tutors)):
        klasses.append(None)
    return ((t, k) for t, k in zip(tutors, klasses))

gen = tuple_gen()
print(type(gen), sys.getsizeof(gen), gen.__sizeof__())
first = next(gen)
print(first, type(first))
for i in gen:
    print(i)

import itertools

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        result = ""
        for i in self.matrix:
            result = result + f"[{','.join(str(x) for x in i)}]\n"
        return result
    def __add__(self, other):
        result = []
        for x, y in itertools.zip_longest(self.matrix, other.matrix):
            row = []
            if x and y:
                for i, j in itertools.zip_longest(x, y):
                    row.append((i if i else 0) + (j if j else 0))
            else:
                row_len = max(len(self.matrix[0]) if self.matrix[0] else 0, len(other.matrix[0]) if other.matrix[0] else 0)
                row = list(x) if x else list(y)
                while len(row) < row_len:
                    row.append(0)
            result.append(row)
        return Matrix(result)

x = Matrix([[1,2],[3,4],[14,15],[16,17]])
print(x)
y = Matrix([[5,6,7],[8,9,10],[11,12,13]])
print(y)
z = x + y
print(z)

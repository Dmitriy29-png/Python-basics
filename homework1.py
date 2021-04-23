
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[-4, 0, 3], [-5, 2, 1], [0, 1, 8], [1, 13, -1]])
new_m = Matrix([[5, 6, 2], [-2, 4, 2], [1, 2, -2], [23, 2, -7]])
print(m)
print(new_m)
print(m.__add__(new_m))
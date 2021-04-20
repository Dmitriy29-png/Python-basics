
class Road:

    def __init__(self, length, width, weight, depth):
        self.length = length
        self.width = width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self.length
        wid = self.width
        weig = self.weight
        dep = self.depth
        total = leng * wid * weig * dep / 1000
        return print(f'To cover the entire roadway, it is necessary\n '\
                     f'{leng} m  * {wid} m  * {weig} kg * {dep} sm = {total} t')


r = Road(20, 5000, 25, 5)
r.mass()
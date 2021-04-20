class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Start rendering- {self.title}'


class Pen(Stationary):

    def draw(self):
        return f'You took {self.title}. Wrote a letter'


class Pencil(Stationary):

    def draw(self):
        return f'You took {self.title}.Painted a portrait'


class Handle(Stationary):

    def draw(self):
        return f'You took {self.title}.Wrote on the wal'


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
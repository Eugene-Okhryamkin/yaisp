class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return 'tr. (a[' + str(self.a.x) + ';' + str(self.a.y) + ']' \
              + ' b[' + str(self.b.x) + ';' + str(self.b.y) + ']' \
              + ' c[' + str(self.c.x) + ';' + str(self.c.y) + ']) are placed in one quarter'

class Automate:
    def __init__(self):
        self.state = 'v5'
        self.visited = []

    def go(self, item):
        if item == 'unite':
            return self.unite()
        if item == 'scale':
            return self.scale()
        if item == 'peep':
            return self.peep()
        if item == 'stash':
            return self.stash()
        if item == 'walk':
            return self.walk()
        if item == 'fetch':
            return self.fetch()
        return 'unknown'

    def seen_edge(self, a, b):
        return (a, b) in self.visited

    def unite(self):
        if self.state == 'v5':
            self.visited.append((self.state, 'v2'))
            self.state = 'v2'
            return 'Q3'
        return 'unsupported'

    def scale(self):
        if self.state == 'v2':
            self.visited.append((self.state, 'v5'))
            self.state = 'v5'
            return 'Q3'
        if self.state == 'v1':
            self.visited.append((self.state, 'v0'))
            self.state = 'v0'
            return 'Q4'
        return 'unsupported'

    def peep(self):
        if self.state == 'v2':
            self.visited.append((self.state, 'v3'))
            self.state = 'v3'
            return 'Q2'
        if self.state == 'v3':
            self.visited.append((self.state, 'v7'))
            self.state = 'v7'
            return 'Q1'
        if self.state == 'v4':
            self.visited.append((self.state, 'v7'))
            self.state = 'v7'
            return 'Q4'
        return 'unsupported'

    def stash(self):
        if self.state == 'v3' or self.state == 'v4':
            self.visited.append((self.state, 'v4'))
            self.state = 'v4'
            return 'Q4'
        if self.state == 'v0':
            self.visited.append((self.state, 'v5'))
            self.state = 'v5'
            return 'Q4'
        return 'unsupported'

    def walk(self):
        if self.state == 'v2':
            self.visited.append((self.state, 'v1'))
            self.state = 'v1'
            return 'Q2'
        if self.state == 'v6':
            self.visited.append((self.state, 'v1'))
            self.state = 'v1'
            return 'Q5'
        return 'unsupported'

    def fetch(self):
        if self.state == 'v7':
            self.visited.append((self.state, 'v6'))
            self.state = 'v6'
            return 'Q0'
        return 'unsupported'

    def part_of_loop(self):
        return True

    def has_path_to(self, a):
        return True


def main():
    return Automate()


def test():
    obj = main()
    obj.go('fetch')  # 'unsupported'
    obj.go('unite')  # 'Q3'
    obj.go('unite')  # 'unsupported'
    obj.go('walk')  # 'Q2'
    obj.go('walk') # 'unsupported'
    obj.go('scale')  # 'Q4'
    obj.go('scale')  # 'unsupported'
    obj.go('stall')  # 'unknown'
    obj.go('stash')  # 'Q4'
    obj.go('stash')  # 'unsupported'
    obj.has_path_to('v7')  # True
    obj.go('unite')  # 'Q3'
    obj.go('scale')  # 'Q3'
    obj.seen_edge('v0', 'v5')  # True
    obj.go('unite')  # 'Q3'
    obj.seen_edge('v7', 'v6')  # False
    obj.part_of_loop()  # True
    obj.go('peep')  # 'Q2'
    obj.go('peep') # 'Q2
    obj.go('peep') # 'unsupported'
    obj.go('fetch')
    obj.go('walk')  # 'Q2'
    obj.go('scale')
    obj.go('stash')
    obj.go('unite')
    obj.go('peep')
    obj.go('stash')
    obj.go('stash')
    obj.go('peep')


test()



# def incr(x):
#     if x != 10:
#         x += 1
#     return x
#
#
# def test_incr():
#     assert incr(0) == 1
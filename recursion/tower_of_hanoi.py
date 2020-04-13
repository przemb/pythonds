#
#            #             |             |
#          #####           |             |
#        #########     ____|____    _____|______
# idx:    source         dest           tmp
#        [3, 2, 1]        []            []


class Tower:
    def __init__(self, name, num=0):
        self.name = name
        self.data = [x for x in range(num, 0, -1)]


class TowerOfHanoi:
    def __init__(self, num):
        self.tower1 = Tower("SOURCE", num)
        self.tower2 = Tower("DEST")
        self.tower3 = Tower("TMP")
        self.height = num

    def __repr__(self):
        return f"state: {str(self.tower1.data):10}  " \
               f"       {str(self.tower2.data):10}  " \
               f"       {str(self.tower3.data):10}  "

    def move_tower(self, height, source, destination, tmp):
        if height >= 1:
            self.move_tower(height - 1, source, tmp, destination)
            self.move_disk(source, destination)
            self.move_tower(height - 1, tmp, destination, source)

    def move_disk(self, source, destination):
        tmp = source.data.pop()
        destination.data.append(tmp)
        print(f"\nmoving disk from {source.name} to {destination.name}")
        print(self)


p = TowerOfHanoi(3)  # number of disks
print(p)
p.move_tower(p.height, p.tower1, p.tower2, p.tower3)

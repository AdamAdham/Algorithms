class RandomizedSet:

    def __init__(self):
        self.list = [] # Needed due to getRandom(self):, no way to get O(1) with map only, since accessing map using index needs turing the keys into a list O(1)
        self.map = {} # Dict of indices, for access of list in O(1)

    def search(self, val):
        return val in self.map

    def insert(self, val):
        if self.search(val):
            return False

        self.list.append(val)
        self.map[val] = len(self.list) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        # Swapping the last element of the array with the one getting deleted, to keep the length of the array to O(n) not the O(i) i: number of inserts
        index = self.map[val]
        self.list[index] = self.list[-1]
        self.map[self.list[-1]] = index
        self.list.pop()
        self.map.pop(val)
        return True

    def getRandom(self):
        return random.choice(self.list)
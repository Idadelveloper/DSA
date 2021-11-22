# Python Implementation of hash table

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][index] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


my_hash = HashTable()
my_hash['march 1'] = 40
my_hash['march 2'] = 7
my_hash['march 3'] = 29
my_hash['march 4'] = 18
my_hash['march 5'] = 30
my_hash['march 6'] = 60
my_hash['march 8'] = 78
my_hash['march 9'] = 67
my_hash['march 10'] = 25
my_hash['march 11'] = 86
my_hash['march 12'] = 44
my_hash['march 13'] = 90
my_hash['march 14'] = 33
my_hash['march 15'] = 56
my_hash['march 16'] = 75
my_hash['march 17'] = 34
my_hash['march 18'] = 99
my_hash['march 19'] = 62
my_hash['march 20'] = 37
my_hash['march 21'] = 50
my_hash['march 22'] = 76
my_hash['march 23'] = 91
my_hash['march 24'] = 84
my_hash['march 25'] = 69
my_hash['march 26'] = 52
my_hash['march 27'] = 5
my_hash['march 28'] = 17
my_hash['march 29'] = 47
my_hash['march 30'] = 83
print(my_hash['march 21'])
del my_hash['march 17']
print(my_hash.arr)

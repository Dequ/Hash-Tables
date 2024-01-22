class HashTable:
    def __init__(self):
        self.MAX = 10     # I am keeping size very low to demonstrate linear probing easily but usually the size should be high
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        # print(self.arr)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:              # to update existing key,val with new val
                return prob_index
        raise Exception("Hashmap full")

    def backwards_mover_range(self, index_of_deletion, prob_index_bm):
        x = self.get_prob_range(index_of_deletion)
        i = x.index(prob_index_bm)
        return x[i+1:] + [index_of_deletion]

    def backwards_mover(self, index_of_deletion):
        prob_range_bm = self.get_prob_range(index_of_deletion + 1)
        for prob_index_bm in prob_range_bm:
            if self.arr[prob_index_bm] is None:
                return
            if self.arr[prob_index_bm]:
                h = self.get_hash(self.arr[prob_index_bm][0])
                if h in self.backwards_mover_range(index_of_deletion, prob_index_bm):
                    self.arr[index_of_deletion] = self.arr[prob_index_bm]
                    self.arr[prob_index_bm] = None
                    # print(t.arr)
                    return self.backwards_mover(prob_index_bm)

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return  # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
                self.backwards_mover(prob_index)



# Driver code
t = HashTable()
t["march 0"] = 34
t["march 1"] = 34
t["march 2"] = 34
t["march 3"] = 34
t["march 4"] = 34
t["march 5"] = 34
t["march 6"] = 34
t["march 7"] = 34
t["march 8"] = 34
t["march 26"] = 34
print(t.arr)
del t["march 6"]
print(t.arr)

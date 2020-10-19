import random


class Element:
    def __init__(self, key, value=None):
        self.__key = key
        self.__value = value

    def get_key(self):
        return self.__key


def division_method(k, m):
    hash_key = k % m
    return hash_key


class HashTable:
    def __init__(self, hash_type, hash_length):
        self.__hash_table = []
        self.__hash_type = hash_type
        self.__hash_length = hash_length
        self.collision = 0
        self.failed_insert = 0
        if hash_type == 0:
            for i in range(0, hash_length):
                self.__hash_table.append([])
            '''
            for i in range(0, len(elements)):
                self.insert(elements[i], division_element)
            '''
        elif hash_type == 1:
            for i in range(0, hash_length):
                self.__hash_table.append(None)
            '''
            i = 0
            available_space = True
            while i < len(elements) and available_space:
                collision = self.insert(elements[i], division_element)
                if collision == division_element:
                    available_space = False
                i += 1
            '''

    def insert(self, element):
        hash_key = division_method(element.get_key(), self.__hash_length)
        collision = 0
        if self.__hash_type == 0:
            if len(self.__hash_table[hash_key]):
                collision += 1
            self.__hash_table[hash_key].insert(0, element)
        elif self.__hash_type == 1:
            i = 0
            insert = False
            while i < self.__hash_length and not insert:
                actual_key = division_method(hash_key + i, self.__hash_length)
                if self.__hash_table[actual_key] is None or self.__hash_table[actual_key] == "Deleted":
                    self.__hash_table[actual_key] = element
                    insert = True
                if not insert:
                    collision += 1
                i += 1
            if collision == i:
                self.failed_insert += 1
                #print("La tabella hash è piena!!! Non è stato possibile inserire l'elemento con chiave " + str(element.get_key()))
        return collision

    def delete(self, element_key):
        hash_key = division_method(element_key, self.__hash_length)
        find = False
        i = 0
        if self.__hash_type == 0:
            if len(self.__hash_table[hash_key]) != 0:
                while i < len(self.__hash_table[hash_key]) and not find:
                    if ((self.__hash_table[hash_key])[i]).get_key() == element_key:
                        self.__hash_table[hash_key].remove((self.__hash_table[hash_key])[i])
                        find = True
                    i += 1
        elif self.__hash_type == 1:
            while i < self.__hash_length and not find:
                actual_key = division_method(hash_key + i, self.__hash_length)
                if (self.__hash_table[actual_key]).get_key() == element_key:
                    self.__hash_table[actual_key] = "Deleted"
                    find = True
                i += 1
        '''
        if not find:
            print("Valore da cancellare non presente nella tabella hash!!!")
        '''

    def search(self, element_key):
        hash_key = division_method(element_key, self.__hash_length)
        i = 0
        if self.__hash_type == 0:
            if len(self.__hash_table[hash_key]) != 0:
                while i < len(self.__hash_table[hash_key]):
                    if ((self.__hash_table[hash_key])[i]).get_key() == element_key:
                        return (self.__hash_table[hash_key])[i]
                    i += 1
        elif self.__hash_type == 1:
            while i < self.__hash_length:
                actual_key = division_method(hash_key + i, self.__hash_length)
                if self.__hash_table[actual_key] is not None:
                    if (self.__hash_table[actual_key]).get_key() == element_key:
                        return self.__hash_table[actual_key]
                i += 1
        #print("L'elemento non è presente nella tabella hash!!! ")
        return None

    def get_cell(self, pos):
        return self.__hash_table[pos]

    def add_collision(self, coll):
        self.collision += coll

    def get_collision(self):
        return self.collision

    def get_failed_insert(self):
        return self.failed_insert

hType = int(input("Inserisci 0 per hash con concatenamento e 1 per ash ad indirizzamento diretto:"))
keys1 = []
while len(keys1) < 16:
    key = random.randint(0, 1000)
    if key not in keys1:
        keys1.append(key)
objects1 = []
for it in range(0, len(keys1)):
    obj = Element(keys1[it])
    objects1.append(obj)
ht1 = HashTable(hType, 8)
coll1 = 0
for it in range(0, len(objects1)):
    coll1 += ht1.insert(objects1[it])
    if it == 1:
        print("m=8:\n", coll1)
    elif it == 3 or it == 5 or it == 7 or it == 9 or it == 11 or it == 13 or it == 15:
        print(coll1)

keys2 = []
while len(keys2) < 24:
    key = random.randint(0, 1000)
    if key not in keys2:
        keys2.append(key)
objects2 = []
for it in range(0, len(keys2)):
    obj = Element(keys2[it])
    objects2.append(obj)
ht2 = HashTable(hType, 12)
coll2 = 0
for it in range(0, len(objects2)):
    coll2 += ht2.insert(objects2[it])
    if it == 2:
        print("m=12:\n", coll2)
    elif it == 5 or it == 8 or it == 11 or it == 14 or it == 17 or it == 20 or it == 23:
        print(coll2)

keys3 = []
while len(keys3) < 32:
    key = random.randint(0, 1000)
    if key not in keys3:
        keys3.append(key)
objects3 = []
for it in range(0, len(keys3)):
    obj = Element(keys3[it])
    objects3.append(obj)
ht3 = HashTable(hType, 16)
coll3 = 0
for it in range(0, len(objects3)):
    coll3 += ht3.insert(objects3[it])
    if it == 3:
        print("m=16:\n", coll3)
    elif it == 7 or it == 11 or it == 15 or it == 19 or it == 23 or it == 27 or it == 31:
        print(coll3)

keys4 = []
while len(keys4) < 40:
    key = random.randint(0, 1000)
    if key not in keys4:
        keys4.append(key)
objects4 = []
for it in range(0, len(keys4)):
    obj = Element(keys4[it])
    objects4.append(obj)
ht4 = HashTable(hType, 20)
coll4 = 0
for it in range(0, len(objects4)):
    coll4 += ht4.insert(objects4[it])
    if it == 4:
        print("m=20:\n", coll4)
    elif it == 9 or it == 14 or it == 19 or it == 24 or it == 29 or it == 34 or it == 39:
        print(coll4)

'''
hType = int(input("Inserisci 0 per hash con concatenamento e 1 per ash ad indirizzamento diretto:"))
hash_length = int(input("Inserisci la grandezza della tabella hash:"))
keys1 = []
while len(keys1) < hash_length/4:
    key = random.randint(0, 1000)
    if key not in keys1:
        keys1.append(key)
objects1 = []
for it in range(0, len(keys1)):
    obj = Element(keys1[it])
    objects1.append(obj)
ht1 = HashTable(hType, hash_length)
coll1 = 0
for it in range(0, len(objects1)):
    coll1 += ht1.insert(objects1[it])
print("1/4: ", coll1)

keys2 = []
while len(keys2) < hash_length/2:
    key = random.randint(0, 1000)
    if key not in keys2:
        keys2.append(key)
objects2 = []
for it in range(0, len(keys2)):
    obj = Element(keys2[it])
    objects2.append(obj)
ht2 = HashTable(hType, hash_length)
coll2 = 0
for it in range(0, len(objects2)):
    coll2 += ht2.insert(objects2[it])
print("1/2: ", coll2)

keys3 = []
while len(keys3) < hash_length*(3/4):
    key = random.randint(0, 1000)
    if key not in keys3:
        keys3.append(key)
objects3 = []
for it in range(0, len(keys3)):
    obj = Element(keys3[it])
    objects3.append(obj)
ht3 = HashTable(hType, hash_length)
coll3 = 0
for it in range(0, len(objects3)):
    coll3 += ht3.insert(objects3[it])
print("3/4: ", coll3)

keys4 = []
while len(keys4) < hash_length:
    key = random.randint(0, 1000)
    if key not in keys4:
        keys4.append(key)
objects4 = []
for it in range(0, len(keys4)):
    obj = Element(keys4[it])
    objects4.append(obj)
ht4 = HashTable(hType, hash_length)
coll4 = 0
for it in range(0, len(objects4)):
    coll4 += ht4.insert(objects4[it])
print("1: ", coll4)

keys5 = []
while len(keys5) < hash_length*(5/4):
    key = random.randint(0, 1000)
    if key not in keys5:
        keys5.append(key)
objects5 = []
for it in range(0, len(keys5)):
    obj = Element(keys5[it])
    objects5.append(obj)
ht5 = HashTable(hType, hash_length)
coll5 = 0
for it in range(0, len(objects5)):
    coll5 += ht5.insert(objects5[it])
print("5/4: ", coll5)

keys6 = []
while len(keys6) < hash_length*(3/2):
    key = random.randint(0, 1000)
    if key not in keys6:
        keys6.append(key)
objects6 = []
for it in range(0, len(keys6)):
    obj = Element(keys6[it])
    objects6.append(obj)
ht6 = HashTable(hType, hash_length)
coll6 = 0
for it in range(0, len(objects6)):
    coll6 += ht6.insert(objects6[it])
print("3/2: ", coll6)

keys7 = []
while len(keys7) < hash_length*(7/4):
    key = random.randint(0, 1000)
    if key not in keys7:
        keys7.append(key)
objects7 = []
for it in range(0, len(keys7)):
    obj = Element(keys7[it])
    objects7.append(obj)
ht7 = HashTable(hType, hash_length)
coll7 = 0
for it in range(0, len(objects7)):
    coll7 += ht7.insert(objects7[it])
print("7/4: ", coll7)

keys8 = []
while len(keys8) < hash_length*2:
    key = random.randint(0, 1000)
    if key not in keys8:
        keys8.append(key)
objects8 = []
for it in range(0, len(keys8)):
    obj = Element(keys8[it])
    objects8.append(obj)
ht8 = HashTable(hType, hash_length)
coll8 = 0
for it in range(0, len(objects8)):
    coll8 += ht8.insert(objects8[it])
print("2: ", coll8)
'''

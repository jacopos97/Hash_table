import unittest
from hash_table import HashTable
from hash_table import Element


class TestHashTable(unittest.TestCase):

    def setUp(self):
        kc1 = [702, 375, 73, 5, 99]
        self.htc1 = HashTable(0, 20)
        for i in range(0, len(kc1)):
            self.htc1.add_collision(self.htc1.insert(Element(kc1[i])))
        kc2 = [321, 436, 776, 255, 700, 433, 862, 925, 649, 388]
        self.htc2 = HashTable(0, 20)
        for i in range(0, len(kc2)):
            self.htc2.add_collision(self.htc2.insert(Element(kc2[i])))
        kc3 = [244, 563, 829, 124, 242, 200, 663, 734, 514, 943, 655, 823, 946, 88, 89]
        self.htc3 = HashTable(0, 20)
        for i in range(0, len(kc3)):
            self.htc3.add_collision(self.htc3.insert(Element(kc3[i])))
        kc4 = [15, 32, 501, 816, 865, 909, 482, 650, 173, 490, 366, 146, 893, 962, 201, 444, 484, 737, 706, 991]
        self.htc4 = HashTable(0, 20)
        for i in range(0, len(kc4)):
            self.htc4.add_collision(self.htc4.insert(Element(kc4[i])))
        kc5 = [356, 948, 840, 755, 335, 256, 1000, 834, 48, 126, 889, 618, 92, 84, 699, 55, 424, 431, 230, 613]
        self.htc5 = HashTable(0, 15)
        for i in range(0, len(kc5)):
            self.htc5.add_collision(self.htc5.insert(Element(kc5[i])))
        kc6 = [364, 736, 874, 391, 345, 357, 523, 968, 712, 472, 942, 146, 930, 761, 729, 991, 635, 517, 27, 329]
        self.htc6 = HashTable(0, 10)
        for i in range(0, len(kc6)):
            self.htc6.add_collision(self.htc6.insert(Element(kc6[i])))
        kc7 = [166, 91, 14, 677, 525, 718, 587, 950, 482, 638, 88, 412, 592, 806, 127, 834, 903, 326, 597, 4]
        self.htc7 = HashTable(0, 5)
        for i in range(0, len(kc7)):
            self.htc7.add_collision(self.htc7.insert(Element(kc7[i])))

        kid1 = [921, 119, 684, 371, 804]
        self.htid1 = HashTable(1, 20)
        for i in range(0, len(kid1)):
            self.htid1.add_collision(self.htid1.insert(Element(kid1[i])))
        kid2 = [233, 6, 407, 135, 899, 187, 645, 40, 98, 853]
        self.htid2 = HashTable(1, 20)
        for i in range(0, len(kid2)):
            self.htid2.add_collision(self.htid2.insert(Element(kid2[i])))
        kid3 = [276, 311, 957, 133, 404, 233, 301, 254, 619, 965, 430, 369, 272, 294, 378]
        self.htid3 = HashTable(1, 20)
        for i in range(0, len(kid3)):
            self.htid3.add_collision(self.htid3.insert(Element(kid3[i])))
        kid4 = [451, 738, 330, 216, 127, 31, 610, 161, 770, 346, 404, 151, 822, 598, 880, 376, 95, 660, 283, 362]
        self.htid4 = HashTable(1, 20)
        for i in range(0, len(kid4)):
            self.htid4.add_collision(self.htid4.insert(Element(kid4[i])))
        kid5 = [859, 422, 322, 496, 694, 212, 241, 4, 964, 379, 327, 862, 736, 539, 979, 714, 784, 430, 983, 435]
        self.htid5 = HashTable(1, 15)
        for i in range(0, len(kid5)):
            self.htid5.add_collision(self.htid5.insert(Element(kid5[i])))
        kid6 = [239, 701, 798, 416, 922, 232, 929, 788, 349, 344, 975, 73, 941, 208, 768, 287, 600, 55, 78, 782]
        self.htid6 = HashTable(1, 10)
        for i in range(0, len(kid6)):
            self.htid6.add_collision(self.htid6.insert(Element(kid6[i])))
        kid7 = [240, 475, 964, 740, 178, 265, 135, 680, 990, 548, 810, 983, 155, 282, 684, 184, 941, 985, 361, 339]
        self.htid7 = HashTable(1, 5)
        for i in range(0, len(kid7)):
            self.htid7.add_collision(self.htid7.insert(Element(kid7[i])))

    def test_init_hash_table(self):
        self.assertEqual(self.htc1.get_collision(), 0)
        self.assertEqual(self.htc2.get_collision(), 1)
        self.assertEqual(self.htc3.get_collision(), 6)
        self.assertEqual(self.htc4.get_collision(), 7)
        self.assertEqual(self.htc5.get_collision(), 9)
        self.assertEqual(self.htc6.get_collision(), 10)
        self.assertEqual(self.htc7.get_collision(), 15)

        self.assertEqual(self.htid1.get_collision(), 1)
        self.assertEqual(self.htid1.get_failed_insert(), 0)
        self.assertEqual(self.htid2.get_collision(), 2)
        self.assertEqual(self.htid2.get_failed_insert(), 0)
        self.assertEqual(self.htid3.get_collision(), 8)
        self.assertEqual(self.htid3.get_failed_insert(), 0)
        self.assertEqual(self.htid4.get_collision(), 39)
        self.assertEqual(self.htid4.get_failed_insert(), 0)
        self.assertEqual(self.htid5.get_collision(), 124)
        self.assertEqual(self.htid5.get_failed_insert(), 5)
        self.assertEqual(self.htid6.get_collision(), 117)
        self.assertEqual(self.htid6.get_failed_insert(), 10)
        self.assertEqual(self.htid7.get_collision(), 78)
        self.assertEqual(self.htid7.get_failed_insert(), 15)

    def test_search(self):
        self.assertEqual(self.htc1.search(5), (self.htc1.get_cell(5))[0])
        self.assertEqual(self.htc2.search(405), None)
        self.assertEqual(self.htc3.search(734), (self.htc3.get_cell(14))[1])
        self.assertEqual(self.htc4.search(32), (self.htc4.get_cell(12))[0])
        self.assertEqual(self.htc5.search(46), None)
        self.assertEqual(self.htc6.search(635), (self.htc6.get_cell(5))[0])
        self.assertEqual(self.htc7.search(91), (self.htc7.get_cell(1))[2])

        self.assertEqual(self.htid1.search(143), None)
        self.assertEqual(self.htid2.search(6), self.htid2.get_cell(6))
        self.assertEqual(self.htid3.search(276), self.htid3.get_cell(16))
        self.assertEqual(self.htid4.search(770), self.htid4.get_cell(14))
        self.assertEqual(self.htid5.search(4), self.htid5.get_cell(8))
        self.assertEqual(self.htid6.search(768), None)
        self.assertEqual(self.htid7.search(964), self.htid7.get_cell(4))

    def test_delete(self):
        elc1 = self.htc1.search(5)
        self.assertEqual(len(self.htc1.get_cell(5)), 1)
        self.htc1.delete(elc1.get_key())
        self.assertEqual(len(self.htc1.get_cell(5)), 0)
        elc2 = self.htc2.search(388)
        self.assertEqual(len(self.htc2.get_cell(8)), 1)
        self.htc2.delete(elc2.get_key())
        self.assertEqual(len(self.htc2.get_cell(8)), 0)
        elc3 = self.htc3.search(734)
        self.assertEqual(len(self.htc3.get_cell(14)), 2)
        self.htc3.delete(elc3.get_key())
        self.assertEqual(len(self.htc3.get_cell(14)), 1)
        elc4 = self.htc4.search(32)
        self.assertEqual(len(self.htc4.get_cell(12)), 1)
        self.htc4.delete(elc4.get_key())
        self.assertEqual(len(self.htc4.get_cell(12)), 0)
        elc5 = self.htc5.search(948)
        self.assertEqual(len(self.htc5.get_cell(3)), 3)
        self.htc5.delete(elc5.get_key())
        self.assertEqual(len(self.htc5.get_cell(3)), 2)
        elc6 = self.htc6.search(635)
        self.assertEqual(len(self.htc6.get_cell(5)), 2)
        self.htc6.delete(elc6.get_key())
        self.assertEqual(len(self.htc6.get_cell(5)), 1)
        elc7 = self.htc7.search(91)
        self.assertEqual(len(self.htc7.get_cell(1)), 4)
        self.htc7.delete(elc7.get_key())
        self.assertEqual(len(self.htc7.get_cell(1)), 3)

        elid1 = self.htid1.search(684)
        self.htid1.delete(elid1.get_key())
        self.assertEqual(self.htid1.get_cell(4), "Deleted")
        elid2 = self.htid2.search(6)
        self.htid2.delete(elid2.get_key())
        self.assertEqual(self.htid2.get_cell(6), "Deleted")
        elid3 = self.htid3.search(276)
        self.htid3.delete(elid3.get_key())
        self.assertEqual(self.htid3.get_cell(16), "Deleted")
        elid4 = self.htid4.search(770)
        self.htid4.delete(elid4.get_key())
        self.assertEqual(self.htid4.get_cell(14), "Deleted")
        elid5 = self.htid5.search(4)
        self.htid5.delete(elid5.get_key())
        self.assertEqual(self.htid5.get_cell(8), "Deleted")
        elid6 = self.htid6.search(344)
        self.htid6.delete(elid6.get_key())
        self.assertEqual(self.htid6.get_cell(7), "Deleted")
        elid7 = self.htid7.search(964)
        self.htid7.delete(elid7.get_key())
        self.assertEqual(self.htid7.get_cell(4), "Deleted")

    def test_insert(self):
        self.assertEqual(len(self.htc1.get_cell(3)), 0)
        self.htc1.insert(Element(23))
        self.assertEqual(len(self.htc1.get_cell(3)), 1)
        self.assertEqual(len(self.htc2.get_cell(16)), 2)
        self.htc2.insert(Element(276))
        self.assertEqual(len(self.htc2.get_cell(16)), 3)
        self.assertEqual(len(self.htc3.get_cell(19)), 0)
        self.htc3.insert(Element(19))
        self.assertEqual(len(self.htc3.get_cell(19)), 1)
        self.assertEqual(len(self.htc4.get_cell(11)), 1)
        self.htc4.insert(Element(331))
        self.assertEqual(len(self.htc4.get_cell(11)), 2)
        self.assertEqual(len(self.htc5.get_cell(2)), 1)
        self.htc5.insert(Element(827))
        self.assertEqual(len(self.htc5.get_cell(2)), 2)
        self.assertEqual(len(self.htc6.get_cell(8)), 1)
        self.htc6.insert(Element(688))
        self.assertEqual(len(self.htc6.get_cell(8)), 2)
        self.assertEqual(len(self.htc7.get_cell(3)), 4)
        self.htc7.insert(Element(33))
        self.assertEqual(len(self.htc7.get_cell(3)), 5)

        elid1 = Element(18)
        self.htid1.insert(elid1)
        self.assertEqual(elid1, self.htid1.get_cell(18))
        elid2 = Element(222)
        self.htid2.insert(elid2)
        self.assertEqual(elid2, self.htid2.get_cell(2))
        elid3 = Element(711)
        self.htid3.insert(elid3)
        self.assertEqual(elid3, self.htid3.get_cell(2))
        self.htid4.delete(346)
        elid4 = Element(52)
        self.htid4.insert(elid4)
        self.assertEqual(elid4, self.htid4.get_cell(6))
        self.htid5.delete(4)
        elid5 = Element(784)
        self.htid5.insert(elid5)
        self.assertEqual(elid5, self.htid5.get_cell(8))
        self.htid6.delete(701)
        elid6 = Element(78)
        self.htid6.insert(elid6)
        self.assertEqual(elid6, self.htid6.get_cell(1))
        self.htid7.delete(475)
        elid7 = Element(684)
        self.htid7.insert(elid7)
        self.assertEqual(elid7, self.htid7.get_cell(1))


if __name__ == '__main__':
    unittest.main()

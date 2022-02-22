import random
from datetime import datetime

class zetafloat:
    random = random.seed(datetime.now())
    def __init__(self):
        self.start = datetime.now()
    
    def operation(self):
        num = random.randrange(0, 75)
        if num < 25:
            return "+"
        if num < 50:
            return "-"
        return "*"
        # return "/"
    
    def gen_nums(self, op):
        small = self.truncate(random.random(), 2)
        large = self.truncate(random.random(), 2)
        while large < small:
            large = self.truncate(random.random(), 2)
        large2 = self.truncate(random.random(), 2)

        if op == "+":
            return [large, large2]
        if op == "-":
            pick = random.randrange(0, 2)
            if pick:
                return[self.truncate(large + large2, 2), large2]
            return [self.truncate(large + large2, 2), large]
        
        return [small, large]
        # return [large * small, small]

    def ans(self, op, nums):
        l = [str(nums[0]) + " " + op + " " + str(nums[1])]
        l.append(self.floatarith(nums[0], nums[1], op))
        return l
    
    def truncate(self, num, dp):
        m = 10 ** dp
        num = int(num * m) / m
        return num

    def shift(self, num):
        return num * 100

    def floatarith(self, num1, num2, op):
        new1 = self.shift(num1)
        new2 = self.shift(num2)
        if op == "+":
            res = (new1 + new2) / 100
        if op == "-":
            res = (new1 - new2) / 100
        if op == "*":
            res = new1 * new2 / 10000
        return res
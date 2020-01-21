def add_two_num(a, b):
    c = a+b
    return c

class Stats():
    def __init__(self, array):
        self.array = array

    def mean(self):
        return sum(self.array) / len(self.array)
    
    def median(self):
        arr_sorted = sorted(self.array)
        middle = float(len(arr_sorted))/2
        if len(arr_sorted) % 2 != 0:
            return arr_sorted[int(middle - 0.5)]
        else:
            return (arr_sorted[int(middle)] + arr_sorted[int(middle - 1)]) / 2
    
    def mode(self):
        if self.array==[]:
            print('No mode found')
        else:
            return max(set(self.array), key=self.array.count)

    def range(self):
        return max(self.array) - min(self.array)
    
class Calculations(Stats()):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
    
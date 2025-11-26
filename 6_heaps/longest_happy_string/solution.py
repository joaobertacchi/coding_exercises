import heapq

class Element:
    def __init__(self, value, letter):
        self.letter = letter
        self.value = -1*value
    def __gt__(self, element):
        if self.value == element.value:
            return self.letter > element.letter
        return self.value > element.value
    def __eq__(self, element):
        return self.value == element.value and self.letter == element.letter
    def __lt__(self, element):
        if self.value == element.value:
            return self.letter < element.letter
        return self.value < element.value
    def get_value(self):
        return self.value * -1
    def set_value(self, value):
        self.value = value * -1

def longest_diverse_string(a, b, c):
    heap = []
    substring = ""
    elem_a = Element(value=a, letter="a")
    elem_b = Element(value=b, letter="b")
    elem_c = Element(value=c, letter="c")
    
    if (elem_a.get_value() > 0):
        heapq.heappush(heap, elem_a)
    if (elem_b.get_value() > 0):
        heapq.heappush(heap, elem_b)
    if (elem_c.get_value() > 0):
        heapq.heappush(heap, elem_c)
    
    stack = []
    last = None
    count = 0
    while len(heap) > 0:
        elem = heapq.heappop(heap)
        if last == elem.letter:
            count += 1
        else:
            last = elem.letter
            count = 1
        if count > 2:
            if len(heap) == 0:
                break
            stack.append(elem)
            elem = heapq.heappop(heap)
            last = elem.letter
            count = 1
        substring = substring + elem.letter
        elem.set_value(elem.get_value() - 1)
        if elem.get_value() > 0:
            heapq.heappush(heap, elem)
        while len(stack) > 0:
            elem = stack.pop()
            heapq.heappush(heap, elem)
        
    return substring

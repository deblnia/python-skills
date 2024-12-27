from functools import total_ordering

# this allows me to only provide an equality and other relation operator 
# and get all the other comparisons for free
@total_ordering
class MutInt:
    __slots__ = ['value']
    
    def __init__(self, value):
        self.value = value 
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"MutInt({self.value!r})"
    def __format__(self, format_spec):
        # format spec = *^10d 
        # * is fill char
        # ^ is center align 
        # 10 is the total width 
        # d is the format type eg. decimal 
        return format(self.value, format_spec)
    def __add__(self, other): 
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        elif isinstance(other, float): 
            return MutInt(other + self.value)
        else: 
            return NotImplemented
    __radd__ = __add__ # reversed operands 
    def __iadd__(self, other): 
        if isinstance(other, MutInt): 
            self.value += other.value 
            return self 
        elif isinstance(other, int):
            self.value += other 
            return self 
        else: 
            return NotImplemented
    # kinda annoying that you need to hand code all the operators 
    # __lt__(), __le__(), __gt__(), __ge__()
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
# python is pass by object reference 
# so assignment (=) creates a reference to the same object in memory 
# need to use copy.deepcopy to have truly separate copies 

    # enabling some conversions 
    def __int__(self): 
        return self.value
    def __float__(self):
        return float(self.value)
    # this doesn't actually work for indexing though 
    __index__ = __int__
    
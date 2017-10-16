a = 5 # Bits = 101
b = 4 # Bits = 100

def print_dec_and_bits(value):
        print('Decimal {:d} | Bits {:b}'.format(value,value))

print_dec_and_bits(a)
print_dec_and_bits(b)

c= a&b

print_dec_and_bits(c)

c = a|b

print_dec_and_bits(c)

print('User rights -----------------')

view = 1 # Bits 001
edit = 2 # Bits 010
create = 4 #Bits 100

print_dec_and_bits(create| edit)

class User:
    def __init__(self,rights):
        self.rights = rights

    def can_view(self):
        return view & self.rights

    def can_edit(self):
        return edit & self.rights

    def can_create(self):
        return create & self.rights
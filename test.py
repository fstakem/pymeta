
class BaseField(object):
    count = 0
    char = 'f'

    def __init__(self, pos):
        self.initial_value = 0
        self.pos = pos
        self.name = self.get_name()
        self.type = str
        self.__class__.count += 1
        
    def __get__(self, instance, owner):
        try:
            attr = getattr(instance, self.name)
        except AttributeError as ae:
            setattr(instance, self.name, self.initial_value)

        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != self.type:
            raise ValueError('WRONG')

        setattr(instance, self.name, value)

    def get_name(self):
        tokens = self.__class__.__name__.lower().split(IntField.char)
        tokens[-1] = IntField.char + tokens[-1]
        tokens.append(str(self.__class__.count))
        
        return '_'.join(tokens)


class IntField(BaseField):

    def __init__(self, pos):
        super().__init__(pos)
        self.type = int


class CompanyBase(object):

    def __init_subclass__(cls):
        print(cls)


class Company(CompanyBase):
    x = IntField(1)


class DerivedCompany(Company):
    y = IntField(2)
    z = IntField(3)


c1 = Company()
c2 = Company()

d1 = DerivedCompany()
d2 = DerivedCompany()

print()
c1.x
c1.x = 5

print()
c1.x

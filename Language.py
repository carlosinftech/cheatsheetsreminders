class Language:
    def __init__(self, name, romance):
        self.__name = name
        self.__romance = romance

    def get_description(self):
        result = self.__name + ' is '
        if self.__romance:
            result += 'a romance language'
        else:
            result += 'not a romance language'
        return result

    def is_romance(self):
        return self.__romance

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if self.__name != name:
            self.__name = name


language = Language('English', False)
language.set_name('French')
# print(language.get_name())
print(language.get_description())

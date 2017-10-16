import Language

class SpanishLanguage(Language):
    def __init__(self):
        Language.__init__('Spanish', True)

class FinsishLanguage(Language):
    def __init__(self):
        Language.__init__(self, 'Finnish', False)

spanish = SpanishLanguage()
print(spanish.getDescription())
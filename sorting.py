from operator import attrgetter
import sys
print(sys.path)
numbers = [1, 7, 42, 25]

sorted_numbers = sorted(numbers)

for number in sorted_numbers:
    print(number)


class Language:
    def __init__(self, name, lang_id):
        self.lang_id = lang_id
        self.name = name

    # object representation the toString in java
    def __repr__(self):
        return '{} : {}'.format(self.lang_id, self.name)


languages = [
    Language('Spanish', 1),
    Language('French', 3),
    Language('English', 2)
]

for language in languages:
    print(language)

sorted_languages = sorted(languages, key=attrgetter('name'))

for sorted_language in sorted_languages:
    print(sorted_language)

sorted_languages_by_id = sorted(languages, key=attrgetter('lang_id'))

for sorted_language_by_id in sorted_languages_by_id:
    print(sorted_language_by_id)
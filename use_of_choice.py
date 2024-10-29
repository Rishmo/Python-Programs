from random import choice
def make_greeting_func(person):
    def get_greet():
        ch=choice(("Good Morning ","Good Evening ","Good Night"))
    return ch+person
    return get_greet
greet=make_greeting_func("Moon")
print(greet())
print(greet())
print(greet())


''' output can be Good Moring Moon
    Good Evening Moon
    Good Night Moon
    or any statement randomly'''

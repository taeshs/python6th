class Mobile:
    fp = 'yes'


realme = Mobile()
readme = Mobile()
geek = Mobile()

print(Mobile.fp)
print(realme.fp)
print(readme.fp)
print(geek.fp)
print('-------------')

Mobile.fp = 'no'

print(Mobile.fp)
print(realme.fp)
print(readme.fp)
print(geek.fp)
print('-------------')

realme.fp = 'Not Working'

print(Mobile.fp)
print(realme.fp)
print(readme.fp)
print(geek.fp)
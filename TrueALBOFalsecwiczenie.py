
'''
maszyny = ['ROWER', 'TrakTOR']
maszyna = 'RoWeR'

print(f'czy w zmiennej znajduje się  rower? TAK')
print(f"{'rower' in {maszyna.lower()}}")

print(f'\nCzy w zmiennej maszyna znajduje się traktor? NIE')
print('traktor' in maszyna)

print(f'\nw Liście maszyna znajduje się RoWeR? TAK')
print('RoWeR' in maszyna)

print(f'\nCzy w zmiennej jest napisane dużymi literami ROWER? TAK')
print('ROWER' in maszyna.upper())

print(f'\nCzy w zmiennej jest napisane małymi literami rower? TAK')
print('rower' in maszyna.lower())





liczba = 10
print(liczba == 10,'TAk')

print(f'\nLiczba jest mniejsza od 10, FAŁSZ: {liczba < 2}')
print(f'\nLiczba jest mniejsza od 6, FAŁSZ: {liczba < 6}')
print(f'\nLiczba jest większa od 5, TAK: {liczba > 5}')
print(f'\nLiczba jest równy bądź mniejszy TAK: {liczba <= 10} ')
print(f'\nLiczba nie jest to 200, PRAWDA: {liczba != 101}')



pizza = ['pieczarki', 'cebula', 'czosnek']

print('pasztet' not in pizza)



restaurant = "światło"
print(restaurant.upper() == 'ŚWIATŁO')
'''

meble1 = 'krzesło'
meble2 = 'KRZESŁO'

print('Krzesło' in meble1.title() == 'Krzesło' in meble2.title())
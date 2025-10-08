"""
3️⃣ Szó keresése a szövegben – tartalom ellenőrzés
Feladat: Kérj be egy bejegyzést a közösségi oldalra,
 majd ellenőrizd, hogy szerepel-e benne a „Python” szó.
"""

bejegyzes = input('Add meg a bejegyzésed!: ')
#keresett_szo = input('Keresett szó: ')
x = bejegyzes.count('Python')
print(f'A keresett szavad ennyiszer szerepel benne: {x}.')


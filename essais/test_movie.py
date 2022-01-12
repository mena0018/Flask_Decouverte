# essais/test_movie.py
from movie import Movie

m1 = Movie('Les évadés', 1, 9.5)

print("\nDurationToString")
print("----------------")

print(m1.durationToString(512))
print(m1.durationToString(4096))
print(m1.durationToString(32768))

print("\nratingToStars")
print("--------------")
print(m1.ratingToStars(0))
print(m1.ratingToStars(2))
print(m1.ratingToStars(4))
print(m1.ratingToStars(8))
print(m1.ratingToStars(100), "\n")

print(vars(m1))
print(dir(m1), "\n")

try:
    m2: Movie = Movie('Les évadés', 122, 5.5)
    print('Tout est OK.')
except:
    print('Les lignes précédentes n’auraient pas dû lancer d’exception !!')
try:
    m2 = Movie('Les évadés', 122, -0.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")
try:
    m2 = Movie('Les évadés', 122, 10.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!? \n")

print("\nLe titre est    : ", m1.title)
print("La durée est de : ", m1.duration, "min")
print("La note est de  : ", m1.rating)
m1.rating = 9
print("La nouvelle note est de ", m1.rating)

m1 = Movie('\nLes évadés', 122, 9.0)
print(m1)

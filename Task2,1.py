# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


newlist = [0,1]
for x in newlist:
    for y in newlist:
        for z in newlist:
            f = not (x or y or z) == (not x and not y and not z)
            print(x,y,z,f)
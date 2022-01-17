
t1 = (1,2,3, 'a', 'Maria Eduarda')

print(type(t1))

print(t1[4])

for v in t1:
    print(v)

# Podemos criar tuplas sem parenteses também, ou com apenas um elemento, porém é necessária a virgula.

t2 = 2,3,'João'
t3 = 1,

# Alterar uma tupla.

p1 = (1,2,3,4,5)
p1 = list(p1)
p1[1] = 3000
p1 = tuple(p1)
print(p1)  #[1, 3000, 3, 4, 5]
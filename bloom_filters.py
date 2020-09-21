import pyhash
bit_vector = [0]*20
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

fnv_pika = fnv('Pikachu') % 20
fnv_char = fnv('Charmander') % 20
murmur_pika = murmur('Pikachu') % 20
murmur_char = murmur('Charmander') % 20

bit_vector[fnv_pika] = 1
bit_vector[murmur_pika] = 1
bit_vector[fnv_char] = 1
bit_vector[murmur_char] = 1


print(bit_vector)

fnv_bulb = fnv('Bulbasaur') % 20
murmur_bulb = murmur('Bulbasaur') % 20
bit_vector[fnv_bulb] = 0
bit_vector[murmur_bulb] = 0

print(bit_vector[fnv_char])
print(bit_vector[murmur_bulb])

fnv_man = fnv('Manan') % 20
murmur_man = murmur('Manan') % 20

print(fnv('Popla')%45)
print(bit_vector[fnv_man])
print(bit_vector[murmur_man])

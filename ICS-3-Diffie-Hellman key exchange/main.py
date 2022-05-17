# Alice and Bob both use public numbers p, and g.
p = 23
g = 9

# Alice, and bob selects private keys.
a = 4
b = 3

# Both Alice and bob now calculate the value of x and y as follows.
x = int(pow(g, a, p)) # Calculated by Alice
y = int(pow(g, b, p)) # Calculated by Bob

# Now both Alice and Bob exchange their calculated keys.

# Alice and Bob now calculate the symmetric keys
#   Alice's calculation: y^a mod p
#   Bob's calculation: x^b mod p
ka = int(pow(y, a, p))
kb = int(pow(x, b, p))

print('Alice\'s key:', ka)
print('Bob\'s key:', kb)
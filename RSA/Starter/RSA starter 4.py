p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi = (p-1)*(q-1)
d = pow(e, -1, phi) 
print(d)
# We know p and q and e, 
# and we are asked to retrieve d. 
# To do so we need to do the modular invert of e like so:
# d = e^(-1) MOD phi
import string

ciphertext = "KSVVWBGSJDSVSISVXBMNYQUUKBNWCUANMJS"

modified_freq = "EQTSORINHCLDUPMFWGYBKVXQJZ"
ciphert_freq = "SQJUBNCGDZVWMYTXKELAFIOHRP"

cleartext = ''
for l in ciphertext:
    i = ciphert_freq.index(l)
    cleartext += modified_freq[i]

print(cleartext)
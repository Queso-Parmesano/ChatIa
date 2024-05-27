from hashlib import sha256

passw ='1324enano'

print(sha256(passw.encode('utf-8')).hexdigest())

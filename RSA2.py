import Crypto.Util.number
import hashlib

bits = 1024

pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

nA = pA * qA

phiA = (pA - 1) * (qA - 1)

e = 65537

dA = Crypto.Util.number.inverse(e, phiA)

msg = "Hola mundo"

hashed_msg = int.from_bytes(hashlib.sha256(msg.encode("utf-8")).digest(), byteorder="big")

print(hashed_msg)
signature = pow(hashed_msg, dA, nA)
print("Firma creada por Alice: ", signature, "\n")

hashed_msg_received = pow(signature, e, nA)
print("Hash del mensaje recibido por Bob: ", hashed_msg_received, "\n")

if hashed_msg_received == hashed_msg:
    print("El mensaje fue firmado por Alice.")
else:
    print("El mensaje no fue firmado por Alice.")

import os
import sys

import scrypt

envkey_var = "ENVKEY"
key = os.environ[envkey_var].encode("utf-8")
cmd = sys.argv[1]
assert cmd in ("dec", "enc")

for fn in sys.argv[2:]:
    cipher_fn = f"{fn}.secret"
    if cmd == "enc":
        print(f"encrypting {fn}...")
        with open(fn, "rb") as inf, open(cipher_fn, "wb") as outf:
            outf.write(scrypt.encrypt(inf.read(), key, maxtime=1))
    elif cmd == "dec":
        print(f"decrypting {cipher_fn}...")
        with open(cipher_fn, "rb") as inf, open(fn, "wb") as outf:
            tmp = scrypt.decrypt(inf.read(), key, encoding=None)
            outf.write(tmp)

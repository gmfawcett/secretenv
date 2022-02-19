"""Support for storing environment (key/value) data in an encrypted file.

Decryption is done with `scrypt`. The symmetric key is expected to be
in an environment variable, called `ENVKEY` by default.

Example of use:

    from collections import ChainMap
    import os
    import secretenv

    env : dict[str,str] = ChainMap(
        os.environ,
        secretenv.open("local.env.secret"),
        secretenv.open("main.env.secret"),
    )
    secretenv.wipe()

You can also use the module as a tool for encrypting and decrypting files:

    python -m secretenv enc myenv.txt   # encrypts   to myenv.txt.secret
    python -m secretenv dec myenv.txt   # decrypts from myenv.txt.secret
"""

import io
import os
import sys
from subprocess import PIPE, Popen
from typing import Callable

SCRYPT = "scrypt"


def decrypt_file(
    filename: str, envkey_var: str = "ENVKEY", encoding: str = "utf-8"
) -> str:
    """Helper function. Decrypts the given file with the given key, and returns the
    string value."""
    with io.open(filename) as f:
        p = Popen(
            f"{SCRYPT} dec --passphrase env:{envkey_var} -",
            shell=True,
            stdin=PIPE,
            stdout=PIPE,
        )
        s = p.communicate(f.buffer.read())[0].decode(encoding)
        if p.returncode:
            raise Exception("scrypt failed", ((filename, envkey_var)))
        return s


def simple_parse(input: str) -> dict[str, str]:
    """A basic environment parser: splits key from value at the first equals sign."""
    return dict(
        line.strip().split("=", 1)
        for line in input.split("\n")
        if line.strip() and not line.startswith("#")
    )


def open(
    filename: str,
    envkey_var: str = "ENVKEY",
    encoding: str = "utf-8",
    parser: (Callable[[str], dict[str, str]]) = simple_parse,
) -> dict[str, str]:
    """Given the name of an encrypted environment file, decrypt it with a key stored
    in an environment variable (default "ENVKEY"), and parse it into a
    dictionary with the provided parser function (defaults to `simple_parse`).
    """
    return parser(decrypt_file(filename, envkey_var, encoding))


def wipe(envkey_var: str = "ENVKEY") -> None:
    """If the environment variable with the key is set, wipe it."""
    if envkey_var in os.environ:
        del os.environ[envkey_var]


if __name__ == "__main__":
    envkey_var = "ENVKEY"
    cmd = sys.argv[1]
    assert cmd in ("dec", "enc")

    for fn in sys.argv[2:]:
        cipher_fn = f"{fn}.secret"
        if cmd == "enc":
            print(f"encrypting {fn}...")
            with io.open(fn, "rb") as inf, io.open(cipher_fn, "wb") as outf:
                p = Popen(
                    f"{SCRYPT} enc --passphrase env:{envkey_var} -t 1 -",
                    shell=True,
                    stdin=inf,
                    stdout=outf,
                )
                if p.wait():
                    raise Exception("scrypt failed", ((fn, envkey_var)))
        elif cmd == "dec":
            print(f"decrypting {cipher_fn}...")
            with io.open(cipher_fn, "rb") as inf, io.open(fn, "wb") as outf:
                p = Popen(
                    f"{SCRYPT} dec --passphrase env:{envkey_var} -",
                    shell=True,
                    stdin=inf,
                    stdout=outf,
                )
                if p.wait():
                    raise Exception("scrypt failed", ((cipher_fn, envkey_var)))

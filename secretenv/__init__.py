"""Support for storing environment (key/value) data in an encrypted file.

Decryption is done with `scrypt`. The symmetric key is expected to be
in an environment variable, called `ENVKEY` by default.

Example of use:

    from collections import ChainMap
    import os
    import secretenv

    env : dict = ChainMap(
        os.environ,
        secretenv.load("local.env.secret"),
        secretenv.load("main.env.secret"),
    )
    secretenv.wipe()

You can also use the module as a tool for encrypting and decrypting files:

    python -m secretenv enc myenv.txt   # encrypts   to myenv.txt.secret
    python -m secretenv dec myenv.txt   # decrypts from myenv.txt.secret
"""

import os
from typing import Callable

import scrypt


def decrypt_file(filename: str, envkey_var: str = "ENVKEY") -> str:
    """Helper function. Decrypts the given file with the given key, and returns the
    string value."""
    with open(filename, "rb") as f:
        data = f.read()
        key = os.environ[envkey_var].encode("ascii")
        return scrypt.decrypt(data, key)


def simple_parse(input: str) -> dict:
    """A basic environment parser: splits key from value at the first equals sign."""
    return dict(
        line.strip().split("=", 1)
        for line in input.split("\n")
        if line.strip() and not line.startswith("#")
    )


def load(
    filename: str,
    envkey_var: str = "ENVKEY",
    parser: (Callable[[str], dict]) = simple_parse,
) -> dict:
    """Given the name of an encrypted environment file, decrypt it with a key stored
    in an environment variable (default "ENVKEY"), and parse it into a
    dictionary with the provided parser function (defaults to `simple_parse`).
    """
    return parser(decrypt_file(filename, envkey_var))


def wipe(envkey_var: str = "ENVKEY") -> None:
    """If the environment variable with the key is set, wipe it."""
    if envkey_var in os.environ:
        del os.environ[envkey_var]

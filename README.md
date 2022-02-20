# secretenv

Just playing with an idea re: storing config information in a git repo along
with the code, but needing a secret key (in an environment variable) to decrypt
it. Think, `git-secret`, but `scrypt` / symmetric keys instead of GPG. 

## Usage

Decryption is done with `scrypt`. The symmetric key is expected to be
in an environment variable, called `ENVKEY` by default.

    from collections import ChainMap
    import os
    import secretenv

    env : dict = ChainMap(
        os.environ,
        secretenv.load("local.env.secret"),
        secretenv.load("main.env.secret"),
    )
    secretenv.wipe()  # clear the env. variable

You can also use the module as a tool for encrypting and decrypting files:

    python -m secretenv enc myenv.txt   # encrypts   to myenv.txt.secret
    python -m secretenv dec myenv.txt   # decrypts from myenv.txt.secret

## Change log

- v0.1.5: Relaxed return-type of `secretenv.load` (formerly `open`), to allow
  Python 3.8 compatibility.

- v0.1.4: first decent version. Requires Python 3.9.

Just playing with an idea re: storing config information in a git repo along
with the code, but needing a secret key (in an environment variable) to decrypt
it. Think, `git-secret`, but scrypt / symmetric keys instead of GPG. 

Version 0.1.1 depended on the `scrypt` command line tool being available on the
path. Version 0.1.2 uses the Python
[`scrypt`](https://pypi.org/project/scrypt/0.8.18/) package instead.

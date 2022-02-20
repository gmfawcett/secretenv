# secretenv

Just playing with an idea re: storing config information in a git repo along
with the code, but needing a secret key (in an environment variable) to decrypt
it. Think, `git-secret`, but `scrypt` / symmetric keys instead of GPG. 

## Change log

- v0.1.5: Relaxed return-type of `secretenv.load` (formerly `open`), to allow
  Python 3.8 compatibility.

- v0.1.4: first decent version. Requires Python 3.9.

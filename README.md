Just playing with an idea re: storing config information in a git repo along
with the code, but needing a secret key (in an environment variable) to decrypt
it. Think, `git-secret`, but scrypt / symmetric keys instead of GPG. Depends on the `script` command line tool being available on the path.

#!/usr/bin/env python3

import os
from collections import ChainMap

import secretenv

cm = ChainMap(
    os.environ,
    secretenv.open("local.env.secret"),
    secretenv.open("main.env.secret"),
)
secretenv.wipe()

for k in sorted(cm):
    print((k, cm[k]))

#!/usr/bin/env python3

import os
from collections import ChainMap

import secretenv

cm = ChainMap(
    os.environ,
    secretenv.load("local.env.secret"),
    secretenv.load("main.env.secret"),
)
secretenv.wipe()

for k in sorted(cm):
    print((k, cm[k]))

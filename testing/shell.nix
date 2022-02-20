{ pkgs ? import <nixpkgs> { } }:

with pkgs;

mkShell { buildInputs = [ (python3.withPackages (ps: [ ps.py_scrypt ])) ]; }

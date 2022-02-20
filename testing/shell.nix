{ pkgs ? import <nixpkgs> { } }:

with pkgs;

mkShell { buildInputs = [ (python38.withPackages (ps: [ ps.py_scrypt ])) ]; }

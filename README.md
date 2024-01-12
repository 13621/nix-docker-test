# flake.nix Test mit poetry und docker
## Docker-Image bauen
Wenn nix installiert ist:
``nix build flake.nix#dockerImage --extra-experimental-features 'nix-command flakes'``

Wenn nix nicht installiert ist, ist das halb so schlimm: 

``docker run -it --rm -v C:\path\to\project:/workdir nixos/nix:latest``

``bash-5.2# nix build /workdir/flake.nix#dockerImage --extra-experimental-features 'nix-command flakes'``

``bash-5.2# cp -R $(nix-store -qR result) /workdir/``

😎😎😎😎
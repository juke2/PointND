# PointND

## Setup

To build the dependencies for this repository locally, run the following command in nixOS

```
sudo nixos-rebuild switch -I nixos-config=configuration.nix
```

## Usage

To run the project, use the following command (in your nixos shell):

```
poetry run python main.py
```

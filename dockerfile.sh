#! /usr/bin/env nix-shell
#! nix-shell -i bash -p bash

if [[ $1 == 'a' || $1 == 'all' ]]; then
	podman build -t stepbot-os -f dockerfile-os
	podman build -t stepbot-packages -f dockerfile-packages
	podman build -t stepbot -f dockerfile-requirements
fi

if [[ $1 == 'os' ]]; then
	podman build -t stepbot-os -f dockerfile-os
fi

if [[ $1 == 'p' ]]; then
	podman build -t stepbot-packages -f dockerfile-packages
fi

if [[ $1 == 'pip' || $1 == 'python' ]]; then
	podman build -t stepbot -f dockerfile-requirements
fi

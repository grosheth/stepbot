#! /usr/bin/bash

if [[ $1 == 'a' || $1 == 'all' ]]; then
	docker build -t stepbot-os -f dockerfile-os
	docker build -t stepbot-packages -f dockerfile-packages
	docker build -t stepbot -f dockerfile-requirements
fi

if [[ $1 == 'os' ]]; then
	docker build -t stepbot-os -f dockerfile-os
fi

if [[ $1 == 'p' ]]; then
	docker build -t stepbot-packages -f dockerfile-packages
fi

if [[ $1 == 'pip' || $1 == 'python' ]]; then
	docker build -t stepbot -f dockerfile-requirements
fi

#! /usr/bin/bash

if [[ $1 == 'a' || $1 == 'all' ]]; then
	docker build -t stepbot-os -f dockerfile-os .
	docker build -t stepbot -f dockerfile-stepbot .
fi

if [[ $1 == 'os' ]]; then
	docker build -t stepbot-os -f dockerfile-os .
fi

if [[ $1 == 'p' ]]; then
	docker build -t stepbot -f dockerfile-stebot .
fi

if [[ -z $1 ]]; then
	docker build -t stepbot -f dockerfile-stepbot .
fi

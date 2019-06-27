#!/bin/bash

seq 10 | while read l
do
	curl localhost:8080 &
done

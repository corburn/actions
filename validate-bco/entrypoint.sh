#!/bin/sh -l

time=$(date)
echo ::set-output name=time::$time

/validate_bco.py $1 $2

#!/bin/bash

cat historico_temperaturas.csv | awk 'BEGIN{FS=","} {print $NF}' | sort | uniq > 00_ciudades_unicas.csv


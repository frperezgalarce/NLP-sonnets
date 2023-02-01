#!/bin/bash

awk 'BEGIN{FS="\""}{print $2}' output_v6_20_versos_potenciales_con_terminacion.csv > 00_obtener_terminaciones.tmp_0.csv
awk 'BEGIN{FS=","}{print $NF}' 00_obtener_terminaciones.tmp_0.csv > 00_obtener_terminaciones.tmp_1.csv
#awk 'BEGIN{FS="'"}{print $NF}' 00_obtener_terminaciones.tmp_1.csv > 00_obtener_terminaciones.tmp_2.csv


awk 'BEGIN{FS="\""}{print $1}' output_v6_20_versos_potenciales_con_terminacion.csv > 00_obtener_terminaciones.tmp_100.csv


while IFS= read -r line
do
  mkdir "$line"
done < 00_ciudades_unicas.csv

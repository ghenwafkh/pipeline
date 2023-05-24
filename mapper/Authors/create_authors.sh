#!/bin/bash

clara_path=$(pwd)
input_Authors=$(ls $clara_path/json/Authors/)

for file in $input_Authors; do
	echo
	echo $clara_path/json/Authors/$file
	echo $clara_path/rdf/Authors/${file%.json}.nt

    echo "[CONFIGURATION]" > config.ini
    echo "output_file: $clara_path/rdf/Authors/${file%.json}.nt" >> config.ini
    echo "output_format: N-TRIPLES" >> config.ini
    echo "[X5GON]" >> config.ini
    echo "mappings: $clara_path/mapper/Authors/authors_rules.ttl" >> config.ini
    echo "file_path: $clara_path/json/Authors/$file" >> config.ini

    python3 -m morph_kgc config.ini

done
rm config.ini
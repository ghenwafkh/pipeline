#!/bin/bash

clara_path=$(pwd)
input_ER=$(ls $clara_path/json/ER/)

for file in $input_ER; do
	echo
	echo $clara_path/json/ER/$file
	echo $clara_path/rdf/ER-star/${file%.json}.nt

    echo "[CONFIGURATION]" > config.ini
    echo "output_file: $clara_path/rdf/ER-star/${file%.json}.nt" >> config.ini
    echo "output_format: N-TRIPLES" >> config.ini
    echo "[X5GON]" >> config.ini
    echo "mappings: $clara_path/mapper/ER-star/ER-star_rules.ttl" >> config.ini
    echo "file_path: $clara_path/json/ER/$file" >> config.ini

    python3 -m morph_kgc config.ini

done
rm config.ini
#!/bin/bash

unknown_path=$(pwd)
input_Authors=$(ls $unknown_path/json/Authors/)

for file in $input_Authors; do
	echo
	echo $unknown_path/json/Authors/$file
	echo $unknown_path/rdf/Authors/${file%.json}.nt

    echo "[CONFIGURATION]" > config.ini
    echo "output_file: $unknown_path/rdf/Authors/${file%.json}.nt" >> config.ini
    echo "output_format: N-TRIPLES" >> config.ini
    echo "[X5GON]" >> config.ini
    echo "mappings: $unknown_path/mapper/Authors/authors_rules.ttl" >> config.ini
    echo "file_path: $unknown_path/json/Authors/$file" >> config.ini

    python3 -m morph_kgc config.ini

done
rm config.ini
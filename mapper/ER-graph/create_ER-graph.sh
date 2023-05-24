#!/bin/bash

unknown_path=$(pwd)
input_ER=$(ls $unknown_path/json/ER/)

for file in $input_ER; do
	echo
	echo $unknown_path/json/ER/$file
	echo $unknown_path/rdf/ER-graph/${file%.json}.nt

    echo "[CONFIGURATION]" > config.ini
    echo "output_file: $unknown_path/rdf/ER-graph/${file%.json}.nq" >> config.ini
    echo "output_format: N-QUADS" >> config.ini
    echo "[X5GON]" >> config.ini
    echo "mappings: $unknown_path/mapper/ER-graph/ER-graph_rules.ttl" >> config.ini
    echo "file_path: $unknown_path/json/ER/$file" >> config.ini

    python3 -m morph_kgc config.ini

done
rm config.ini
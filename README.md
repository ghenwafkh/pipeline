### Data Transformation Pipeline 
This pipeline describes the data transformation process to build four versions of a Knowledge Graph (KG) of educational resources (ER). ERs are described by their title, creator, language, license, etc., as well as the subjects they cover. ERs' subjects can be numerous but not equally relevant for the ER. Statement-based RDF reification is used to describe the subjects treated in each ER. 

This pipeline involves three main phases: extraction, transformation, and loading. The extraction phase involves collecting data from a Postgres database. In the transformation phase, JSON files are converted into semantic RDF triples. To compare different RDF reification models, we created four RML mappings to obtain 1) standard reification, 2) RML-star, 3) named graphs, and 4) singleton properties. 

![Alt Text](https://github.com/ghenwafkh/pipeline/blob/ff5e40b5c16eb1b074650744f38f5f87fbbd0660/pipeline.png)

## Requirements
In order to use the four different mapping for RDF and RDF-star, we need python and [morphKGC](https://github.com/morph-kgc/morph-kgc) to be installed.

In order to use SHACL, the python library [pyshacl](https://github.com/RDFLib/pySHACL) is used.

The past two can be installed using `pip install -r requirements.txt`.

## RML mappings
`mapper` contains a folders for all four different reification types and a mapper in the form of a .jar file. Each folder contains a mapping as well as a script to apply this mapping over all json files.

`Authors` contains the mapping responsible for creating the triple relating to the authors of the different educational resources. This part of the graph is generated a single time and the files are then shared between the four different reification models.

In order to use a specific mapping, execute the corresponding script from the main folder of the repository like so `sh mapper/ER-std/create_ER-std.sh`.
Swap both `-std` for either `-singleton` `-graph` `-star` for the other reification types.
This step only require java.

`json` and `rdf` are folders used to store the json and rdf files used as input and ouput of the mapper.
Output of each reification type will go in the corresponding folder, e.g, `ER-std` for standard reification.

Input files follow a specific naming conventions. For that reason, a small sample of data can be found in both folders `json` and `rdf`.

## SHACL shapes
The `SHACL` folder contains the SHACL shapes to verify standard reification, named graph, and singleton property.

Using the python library pyshacl, the data with standard reification can be validated using the script `python3 shacl/validate-std.py` from the root of the repository. Similarly the data with singleton property can be validated by running the command `python3 shacl/validate-singleton.py`.

Our SHACL shape for the Named Graph approach cannot be used with pyshacl.
We would require a way to validate a SHACL shape over multiple named graphs at once, and we have yet to find an implementation of SHACL allowing it.

Additionaly it is important to point out how slow the validation for singleton property is, further improvement needs to be made in that regard.


## License
This work is licensed under a
Creative Commons Attribution 4.0 International License.

See <http://creativecommons.org/licenses/by/4.0/>.


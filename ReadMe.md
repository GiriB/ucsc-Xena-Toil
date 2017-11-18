ReadMe.md

get_all_tar_gz.py - to get all the tar files 
samples.txt - output of get_all_tar_gz.py
downloadSamples.py - reads samples.txt and downloads to /output dir
extract.py - downloadSample.py + extract
MakeMatrix/makematrix.cfg - 'param_name	param_file'
MakeMatrix/createMatrix.py - read from ./makematrix.cfg and creates a matrix file
mappings.py - Extracts FileID,gnosID,SpecimenID values from manifest downloaded from file-browser 
manifest.tsv - Downloaded from file browser
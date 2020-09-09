for phase in train valid test
do
curl -O -C - https://zenodo.org/record/2546921/files/camelyonpatch_level_2_split_${phase}_x.h5.gz
gunzip camelyonpatch_level_2_split_${phase}_x.h5.gz
curl -O -C - https://zenodo.org/record/2546921/files/camelyonpatch_level_2_split_${phase}_y.h5.gz
gunzip camelyonpatch_level_2_split_${phase}_y.h5.gz
curl -O -C - https://zenodo.org/record/2546921/files/camelyonpatch_level_2_split_${phase}_meta.csv
done

for phase in train valid test
do
    echo "Checking hash"
    md5sum -c sums.txt
done
# PatchCamelyon_h5ToImage
Convert PatchCamelyon dataset to png images.

# Usage
```
python patch2img.py
```

# Dataset
- https://github.com/basveeling/pcam
- download script
	- `./download.sh`
- check hash
	- `md5sum -c sums.txt`

# Requirements
```
pip install -r requirements.txt
```

# Troubleshoot
- If you have troubles in files, please try to chech hashes by `md5sum -c sums.txt`.

# Notice
- Now (Aug.31.2019) the MD5 Checksum in the dataset page is not correct. "camelyonpatch_level_2_split_valid_x.h5.gz" and "camelyonpatch_level_2_split_test_x.h5.gz" is replaced.

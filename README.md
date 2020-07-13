### 1. Calculating Wavelengths falling under Bad-Columns of 6k CCD

<img src="images\bad_cols.jpg" style="zoom: 67%;"/>

```she
python calc_wasted_waves.py
```

This will generate file `/output/wavelengths_wasted.txt` 



### 2. Generating features using G2 Sophie Mask

```shell
python generate_features.py
```

This will generate file `/output/features.txt`
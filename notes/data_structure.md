# Data Structure Notes

## Local data location

The MentalPong reposiutory and data files are stored locally under:

```text
data/external/MentalPong/
```

This directory is excluded from version control through `.gitignore`.

## Initial file groups
|Group|Path|Notes|
|---|---|---|
|Repository README|`data/external/MentalPong/`README.md|Original project description|
|Figure code|`data/external/MentalPong/code/`|Figure-level notebooks and scripts|
|Analysis utilities|`data/external/MentalPong/analyses/`|Behaviral, decoding, RNN, and single-neuron analysis code|
|Shared utilities|`data/extenal/MentalPong/utils/`|Helper functions used across scripts|
|Data files|`data/external/MentalPong/data/`|Raw/processed data files, not tracked by Git|

## Initial observation
The dataset contains both small metadata/source files and large `.pkl` / `.mat` files.
For the next step, I will first inspect lightweight metadata and figure-level code before loading large neural response files.

## Next step
- Map paper figures to correwsponding notebooks/scripts.
- Inspect `Source_Data.xlsx` and `valid_meta__sample_full.pkl`.
- Identify which data files are required for the first reconstruction target.
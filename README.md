# temporal-lags

This repository includes Jupyter notebooks and data for reproducing figures anlyzing the effect of temporal lags in CDR. A paper with these figures is currently posted as a preprint:

B. Cabiyo, F. Chay, C. Field, K. Fingerman, Z. Hausfather, K. Hemes, and C. M. Zarakas. Consistent temporal accounting supports credible CDR use. Preprint DOI: [10.70212/cdrxiv.2026302v1](https://doi.org/10.70212/cdrxiv.2026302v1)

## system requirements

### software dependencies

- Python ≥ 3.13
- Key packages: `fair` (>2.2.3), `numpy` (>2.3.4), `pandas` (>2.3.3), `matplotlib` (>3.10.7), `seaborn` (>0.13.2), `jupyter` (>1.1.1)
- See `pyproject.toml` for the full dependency list

### operating systems

The code has been tested on macOS 26.2 (Tahoe). It should work on any system that supports Python ≥ 3.13.

### hardware

No non-standard hardware is required. All notebooks run on a standard personal computer.

## installation guide

**Clone the repo**:

`git clone https://github.com/carbonplan/carbonplan-srm.git`

**Install uv**:

This package uses `uv` for environment management.

`curl -LsSf https://astral.sh/uv/install.sh | sh`

[Installation info](https://docs.astral.sh/uv/getting-started/installation/)

**Install the dependencies**:

`uv sync --all-groups`

Typical install time is about 1 minute on a normal desktop computer. You can alternatively install dependencies manually and then install the package:
```cd temporal-lags
pip install -e .
```

## demo

### instructions

Run the notebooks in the `nbs/` directory in numbered order. The `0_` prefixed notebooks generate input data, and the `1_` prefixed notebooks run the FaIR model simulations:

1. `0_Generate_data_for_figures_1_and_2.ipynb`: constructs the stylized CDR lag profiles
2. `0_Modify_emissions_input_files.ipynb`: prepares modified SSP1-2.6 emissions inputs
3. `1_Run_FaIR_for_figure_3.ipynb`: runs FaIR for the 20-year pulse experiments
4. `1_Run_FaIR_for_figure_4.ipynb`: runs FaIR for the continuous deployment experiments
5. `Figure_1.ipynb` through `Figure_4.ipynb`: generates the manuscript figures

### expected output

Running the notebooks reproduces Figures 1–4 and Table S1 from the manuscript. Figures are rendered inline in the notebooks and saved in `/temporal-lags/figures/`

### expected run time

The full analysis should take less than 15 minutes on a normal desktop computer, depending on hardware. The FaIR ensemble simulations (841 ensemble members × multiple scenarios) account for most of the run time.

## instructions for use

### running on your own data

To apply different lag profiles or emissions scenarios, modify the parameters in `0_Generate_data_for_figures_1_and_2.ipynb` (lag duration, functional form, emissions fraction) or replace the SSP pathway in `0_Modify_emissions_input_files.ipynb`. The FaIR notebooks can then be re-run with the updated inputs.

### reproduction

To reproduce all quantitative results in the manuscript, run the notebooks in `nbs/` sequentially as described above. Input data are provided in `data/` and model outputs are written to `data/outputs/`.

## data

- `data/CDR_1.5deg_Fuhrman.csv` — CDR deployment time series from Fuhrman et al. (2024)
- `data/original/` — original SSP1-2.6 emissions input files for FaIR
- `data/modified/` — modified emissions inputs with lagged CDR profiles applied
- `data/outputs/` — FaIR model output data

## license

All the code in this repository is [MIT-licensed](https://choosealicense.com/licenses/mit/), meaning you are free to use, modify, and redistribute it, provided you include the original license and copyright notice.

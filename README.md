# eikon.playground
WIP: This is a very small repo with some useful functions and workflows to do small tasks in Eikon. 

## Dependencies

- Local python version can be found in the file `./python-version`
- Use your favorite python virtual environment (I use `penv-virtualenv`, other examples are `conda`, etc.) to  activate a python environment.
- Install dependencies with `pip3 install -r requirements.txt` 

## Running the functions

- Create a `.env` file in the root of this project, with your eikon app key: `EIKON_APP_KEY=********`
- Input files containing a list of ISINs in `data-raw/isins.csv`
- Run `pull_bond_ownership.py`. Outputs will be saved as `data/holding_companies.csv` and `data/bad_isins.csv`

More documentation coming...

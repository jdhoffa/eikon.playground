#eikon.playground
- Create a `.env` file in the root of this project, with your eikon app key: `EIKON_APP_KEY=********`
- Input a file containing a list of ISINs in `data-raw/isins.csv`
- Run `pull_bond_ownership.py`. Outputs will be saved as `data/holding_companies.csv` and `data/bad_isins.csv`

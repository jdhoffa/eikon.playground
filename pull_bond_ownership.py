from dotenv import load_dotenv
import eikon as ek
import os
import pandas as pd
import time

# EIKON_APP_KEY must be set in .env file in same directory
load_dotenv()
app_key = os.getenv('EIKON_APP_KEY')
ek.set_app_key(app_key)

# load and format input isins
isins = pd.read_csv('./data-raw/isins.csv')
isins = isins.dropna(subset=['ISIN'])
isins = isins['ISIN'].astype(str).tolist()

# define fields to pull, holding companies
holdings_fields = [
        ek.TR_Field('TR.H.HoldingCompanyName'),
        ek.TR_Field('TR.H.REPORTDATE'),
        ek.TR_Field('TR.H.PARHELD')
          ]

out = []
bad_isins = []

for idx, isin in enumerate(isins):
    print(idx)
    try:
        data = ek.get_data(isin, holdings_fields)
        out.append(data[0])
        time.sleep(3)
    except ek.eikonError.EikonError:
        # manually inspect the output bad_isins and re-run the script
        bad_isins.append(isin)
        print('The following ISIN failed: ' + isin)
        continue

out = pd.concat(out)
out.to_csv('./data/holding_companies.csv')

bad_isins = pd.DataFrame(bad_isins, columns=['ISIN'])
bad_isins.to_csv('./data/bad_isins.csv')

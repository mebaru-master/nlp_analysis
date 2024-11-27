import os
import sys
from dotenv import load_dotenv

# .envを読み込む
load_dotenv()
print(os.getenv('email'))

# iCloud driveにあるcsvファイルを読み込む
import pandas as pd
try:
    df = pd.read_csv('data/Raw_Data.csv')
except FileNotFoundError:
    print('File not found')
    sys.exit(1)

print(df)



import os
import sys
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px

# .envを読み込む
load_dotenv()
print(os.getenv('email'))

# パスを追加する
sys.path.append('../data')
# ファイルパスを作成する
file_path = os.path.join(os.path.dirname(__file__), 'data/Raw_Data.csv')
# iCloud driveにあるcsvファイルを読み込む
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print('File not found')
    sys.exit(1)

print(df)
print(df.columns)

# プロットする
fig = px.scatter(df, x='Linear Acceleration x (m/s^2)', y='Linear Acceleration y (m/s^2)')
fig.show()

import pandas as pd

df1 = pd.read_csv('./data/E2023-2024.csv')
df2 = pd.read_csv('./data/E2022-2023.csv')
df3 = pd.read_csv('./data/E2021-2022.csv')
df4 = pd.read_csv('./data/E2020-2021.csv')
df5 = pd.read_csv('./data/E2019-2020.csv')

all_df = pd.concat([df1, df2, df3, df4, df5])


features = {
     'Date': 'Match Date (dd/mm/yy)',   # merge
     'Time': 'Time of match kick off',  # merge
        
     'HomeTeam': 'Home Team',
     'AwayTeam': 'Away Team',
     # 'Referee': 'Match Referee',
        
     'FTR': 'Full Time Result (H=Home Win, D=Draw, A=Away Win)',  # Y
        
     # 'FTHG': 'Full Time Home Team Goals', # y
     # 'FTAG': 'Full Time Away Team Goals', # y
     # 'HTHG': 'Half Time Home Team Goals',  # y
     # 'HTAG': 'Half Time Away Team Goals',  # y
     # 'HTR': 'Half Time Result (H=Home Win, D=Draw, A=Away Win)',  # y
        
     'B365H': 'Bet365 home win odds',
     'B365D': 'Bet365 draw odds',
     'B365A': 'Bet365 away win odds',
    
}

# has no missing values
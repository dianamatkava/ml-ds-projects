from sklearn.metrics import mean_absolute_error, accuracy_score
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt


def score_model(X_train, X_valid, y_train, y_valid, preprocesor, model=DecisionTreeRegressor, flush=True, **kwargs):
    random_state = kwargs.get('random_state', 42)
    model_tree = model(random_state=random_state, **kwargs)
    
    tree_pipeline = Pipeline(steps=[
        ('preprocesor', preprocesor),
        ('model', model_tree),
    ])
    
    tree_pipeline.fit(X_train, y_train)
    preds = tree_pipeline.predict(X_valid)
    
    mae = mean_absolute_error([round(i) for i in preds], y_valid)
    acc = accuracy_score([round(i) for i in preds], y_valid)
    if flush:
        print(f'\rMAE: {mae} | Acc Score: {acc}| {kwargs=}', end='', flush=True)
    return mae, preds


def display_plot(x_values, y_values, xlabel: str = '', ylabel: str = '', title: str = '', label: str = 'x'):

    plt.figure(figsize=(6, 3))
    plt.plot(x_values, y_values, linestyle='-', color='b', label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    
    plt.show()


def add_wldha(X):
    X['WSH'] = 0
    X['DSH'] = 0
    X['LSH'] = 0
    X['WSA'] = 0
    X['DSA'] = 0
    X['LSA'] = 0
    
    for index, row in X.iterrows():
        
        home_team = row['HomeTeam']
        away_team = row['AwayTeam']
        current_datetime = row['Date']
        
        last_home_matches = X[(X['HomeTeam'] == home_team) | (X['AwayTeam'] == home_team)]
        last_home_matches = last_home_matches[last_home_matches['Date'] < current_datetime].tail(5)
        
        last_away_matches = X[(X['HomeTeam'] == away_team) | (X['AwayTeam'] == away_team)]
        last_away_matches = last_away_matches[last_away_matches['Date'] < current_datetime].tail(5)
    
        
        wsh = len(last_home_matches[(last_home_matches['HomeTeam'] == home_team) & (last_home_matches['FTR'] == 'H')]) + \
              len(last_home_matches[(last_home_matches['AwayTeam'] == home_team) & (last_home_matches['FTR'] == 'A')])
        dsh = len(last_home_matches[last_home_matches['FTR'] == 'D'])
        lsh = len(last_home_matches[(last_home_matches['HomeTeam'] == home_team) & (last_home_matches['FTR'] != 'H')]) + \
              len(last_home_matches[(last_home_matches['AwayTeam'] == home_team) & (last_home_matches['FTR'] != 'A')])
    
        wsa = len(last_away_matches[(last_away_matches['AwayTeam'] == away_team) & (last_away_matches['FTR'] == 'A')]) + \
              len(last_away_matches[(last_away_matches['HomeTeam'] == away_team) & (last_away_matches['FTR'] == 'H')])
        
        dsa = len(last_away_matches[last_away_matches['FTR'] == 'D'])
        lsa = len(last_away_matches[(last_away_matches['AwayTeam'] == away_team) & (last_away_matches['FTR'] != 'A')]) + \
              len(last_away_matches[(last_away_matches['HomeTeam'] == away_team) & (last_away_matches['FTR'] != 'H')])
        
        X.at[index, 'WSH'] = wsh
        X.at[index, 'DSH'] = dsh
        X.at[index, 'LSH'] = lsh
        
        X.at[index, 'WSA'] = wsa
        X.at[index, 'DSA'] = dsa
        X.at[index, 'LSA'] = lsa
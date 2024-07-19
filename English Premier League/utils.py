from sklearn.tree import DecisionTreeRegressor


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


def foo():
    import numpy as np

    # Assume prices are linearly related to the size of the house
    house_size = np.array([[1200], [1500], [1000]])  # Square feet
    prices = np.array([240000, 300000, 200000])  # Price in dollars
    theta = np.array([100000, 100])  # Initial guess for parameters [b, a]

    # Perform one iteration of gradient descent to update the parameters
    learning_rate = 0.01
    m = len(prices)
    X_b = np.c_[np.ones((3, 1)), house_size]  # Adding bias term


    # TODO: Update the theta parameters using the gradient descent rule
    for _ in range(100):
        gradients = 2 / len(prices) + X_b.T.dot(X_b.dot(theta) - prices)
        print(theta - (learning_rate * gradients))
        theta = theta - (learning_rate * gradients)

    print(f"Updated parameters: {theta}")


if __name__ == "__main__":
    foo()
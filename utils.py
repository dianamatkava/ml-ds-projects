from copy import deepcopy

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


def score_model(x_train, x_test, y_train, y_val, model=DecisionTreeRegressor):
    model = model(random_state=0)
    model.fit(x_train, y_train)

    preds = model.predict(x_test)
    return mean_absolute_error(y_val, preds)


def split_test_dataset(data, types='numerical'):
    df_copy = {}
    if types == 'all':
        df_copy = deepcopy(data)
    elif types == 'numerical':
        df_copy = deepcopy(data[data.describe().columns])
    elif types == 'categorical':
        df_copy = deepcopy(data[data.describe().columns])

    X_train = df_copy.drop(columns=['Price'])
    y_train = df_copy.Price

    return train_test_split(X_train, y_train, random_state=1)

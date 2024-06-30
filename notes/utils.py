from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor


def score_model(x_train, x_test, y_train, y_val, model=DecisionTreeRegressor):
    model = model(random_state=0)
    model.fit(x_train, y_train)

    preds = model.predict(x_test)
    return mean_absolute_error(y_val, preds)

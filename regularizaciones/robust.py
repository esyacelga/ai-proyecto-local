import pandas as pd
from sklearn.linear_model import (
    RANSACRegressor, HuberRegressor
)
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

if __name__ == "main":
    dataset = pd.read_csv("./data/felicidad_corrupt.csv")
    print(dataset.head(5))

    X = dataset.drop(['country','score'])
    y = dataset[['score']]

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    estimatores = {
        'SVR':SVR(gamma='auto',C=1.0,epsilon=0.1),
        'RANSAC':RANSACRegressor(),
        'HUBER':HuberRegressor(epsilon=1.35)
    }

    for name, estimator in estimatores.items():
        estimator.fit(x_train,y_train)
        predictions = estimator.predict(x_test)
        print("="*64)
        print(name)
        print("MSE: ", mean_squared_error(y_test,predictions))














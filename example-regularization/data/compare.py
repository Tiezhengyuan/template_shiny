import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression, Ridge


# define functions
def simulate_data(n=1000):
    # Real Variables
    real_var = np.random.normal(size=(n, 7))
    # coefficients
    coef = [12.34, 8.23, 7.83, 5.12, 3.48, 2.97, 1.38]

    # normalized 
    X = np.sum(real_var * coef, axis=1)
    X = (100 + X + np.random.normal(0, 15, n))
    # z-score
    X = (X - np.mean(X)) / np.std(X)
    X = X.reshape(n, 1) 
    
    # Unrelated Variables
    unrelated_var = np.random.normal(size=(n, 7))
    
    d = np.concatenate([real_var, unrelated_var, X], axis=1)
    df = pd.DataFrame(d, columns=list('AEIOUBCDGHJKYWX'))
    return df

def compare(df, alpha=1):
    features = list("ABCDEGHIOUJKYW")
    Y, X = df[features], df["X"]

    # linear regression
    lr = LinearRegression()
    lr.fit(Y, X)
    lr_co = lr.coef_

    # lasso regression
    lasso = Lasso(
        alpha=alpha,
        fit_intercept=True,
        tol=0.0000001,
        max_iter=100000
    )
    lasso.fit(Y, X)
    lasso_co = lasso.coef_

    # ridge regression
    ridge = Ridge(
        alpha=df.shape[0] * alpha,
        fit_intercept=True,
        tol=0.0000001,
        max_iter=100000
    )
    ridge.fit(Y, X)
    ridge_co = ridge.coef_

    df = pd.DataFrame({
        "conames": features * 3,
        "coefs": np.concatenate([lr_co, lasso_co, ridge_co]),
        "model": np.repeat(["Linear", "LASSO", "Ridge"], len(features))
    })
    return df
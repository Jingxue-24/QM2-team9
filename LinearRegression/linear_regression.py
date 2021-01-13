def LinearRegression():
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    name_of_csv="cluster_all.csv"
    df = pd.read_csv(name_of_csv)
    df.to_numpy()
    X = df['Popular_date']
    y = df['Loudness']
    X_np=X.to_numpy()
    y_np=y.to_numpy()
    X_np=X_np.reshape(-1, 1)
    y_np=y_np.reshape(-1, 1)
    LinearRegression().fit(X_np, y_np).coef_
    LinearRegression().fit(X_np, y_np).intercept_
    plt.plot(X_np, y_np)
    plt.scatter(X_np, y_np)
    R_squared= LinearRegression().fit(X_np, y_np).score(X_np, y_np)
    print(R_squared)
    
    return plt.plot(X_np, LinearRegression().fit(X_np, y_np).coef_*X_np + LinearRegression().fit(X_np, y_np).intercept_)
"""KPI pipeline shared by Part A (League of Legends) and Part B (rugby).

Steps, following Hojaji et al.:
1. differenced team features (team minus opponent)
2. leakage safe split (by game or match, and by patch, league or season where possible)
3. models: logistic regression, Random Forest, XGBoost, small neural network
4. feature selection: correlation (Pearson, Spearman) plus model importance
5. explanations: SHAP; stability of KPI ranks across bootstrap samples
Fill in the functions below; keep them small and tested in the notebooks.
"""


def make_differenced_features(df, team_cols, id_col, team_col):
    raise NotImplementedError


def grouped_split(df, group_col, test_size=0.2, seed=0):
    raise NotImplementedError


def fit_models(X_train, y_train, seed=0):
    raise NotImplementedError


def evaluate(models, X_test, y_test):
    raise NotImplementedError


def kpi_ranking(models, X, y, method="shap"):
    raise NotImplementedError


def rank_stability(df, n_boot=100, seed=0):
    raise NotImplementedError

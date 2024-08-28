from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier

X, y = fetch_openml("mnist_784", version=1, return_X_y=True, parser="pandas")

X = X / 255
X_treino, X_teste = X[:60000], X[60000:]

y_treino, y_teste = y[:60000], y[60000:]

redeNeural = MLPClassifier(verbose=True, max_iter=30)

redeNeural.fit(X_treino, y_treino)

print("Treino:", redeNeural.score(X_treino, y_treino))

print("Teste:", redeNeural.score(X_teste, y_teste))

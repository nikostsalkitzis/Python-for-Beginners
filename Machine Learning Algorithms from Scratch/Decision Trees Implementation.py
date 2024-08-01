import numpy as np

class DecisionTreeClassifier:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        self.tree = self._fit(X, y, depth=0)

    def _fit(self, X, y, depth):
        n_samples, n_features = X.shape
        unique_classes = np.unique(y)

        # If only one class or no features, return a leaf node
        if len(unique_classes) == 1:
            return unique_classes[0]
        if self.max_depth is not None and depth >= self.max_depth:
            return self._most_common_class(y)

        # Find the best split
        best_feature, best_threshold = self._best_split(X, y)
        if best_feature is None:
            return self._most_common_class(y)

        # Split the data
        left_indices = X[:, best_feature] <= best_threshold
        right_indices = X[:, best_feature] > best_threshold
        left_tree = self._fit(X[left_indices], y[left_indices], depth + 1)
        right_tree = self._fit(X[right_indices], y[right_indices], depth + 1)

        return (best_feature, best_threshold, left_tree, right_tree)

    def _best_split(self, X, y):
        best_gini = float('inf')
        best_feature, best_threshold = None, None
        n_features = X.shape[1]

        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                left_indices = X[:, feature] <= threshold
                right_indices = X[:, feature] > threshold

                if len(y[left_indices]) == 0 or len(y[right_indices]) == 0:
                    continue

                gini = self._calculate_gini(y[left_indices], y[right_indices])
                if gini < best_gini:
                    best_gini = gini
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold

    def _calculate_gini(self, left_y, right_y):
        n_left = len(left_y)
        n_right = len(right_y)
        n_total = n_left + n_right

        def gini_impurity(y):
            classes, counts = np.unique(y, return_counts=True)
            probabilities = counts / len(y)
            return 1 - np.sum(probabilities ** 2)

        gini_left = gini_impurity(left_y)
        gini_right = gini_impurity(right_y)

        return (n_left / n_total) * gini_left + (n_right / n_total) * gini_right

    def _most_common_class(self, y):
        return np.bincount(y).argmax()

    def predict(self, X):
        return np.array([self._predict(x, self.tree) for x in X])

    def _predict(self, x, tree):
        if isinstance(tree, int):
            return tree

        feature, threshold, left_tree, right_tree = tree
        if x[feature] <= threshold:
            return self._predict(x, left_tree)
        else:
            return self._predict(x, right_tree)

# Example usage
if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    # Load and prepare the data
    data = load_iris()
    X = data.data
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize and train the Decision Tree classifier
    dt = DecisionTreeClassifier(max_depth=3)
    dt.fit(X_train, y_train)

    # Make predictions
    y_pred = dt.predict(X_test)

    # Evaluate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')

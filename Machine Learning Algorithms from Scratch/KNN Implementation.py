import numpy as np

class KNN:
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        """Store the training dataset."""
        self.X_train = np.array(X_train)
        self.y_train = np.array(y_train)

    def predict(self, X_test):
        """Predict the class for each data point in the test set."""
        X_test = np.array(X_test)
        predictions = [self._predict(x) for x in X_test]
        return np.array(predictions)

    def _predict(self, x):
        """Predict the class for a single test point."""
        # Calculate the Euclidean distance from x to all training points
        distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))
        # Find the k nearest neighbors
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = self.y_train[k_indices]
        # Majority vote
        most_common = np.bincount(k_nearest_labels).argmax()
        return most_common

# Example usage:
X_train = [[1, 2], [2, 3], [3, 4], [6, 7], [7, 8]]
y_train = [0, 0, 0, 1, 1]
knn = KNN(k=3)
knn.fit(X_train, y_train)
X_test = [[4, 5], [6, 6]]
print(knn.predict(X_test))  # Output: [0 1]

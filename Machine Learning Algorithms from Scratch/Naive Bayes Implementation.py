import numpy as np

class NaiveBayesClassifier:
    def __init__(self):
        self.class_probs = {}
        self.feature_probs = {}
        self.classes = []

    def fit(self, X, y):
        self.classes = np.unique(y)
        n_samples, n_features = X.shape

        # Calculate class probabilities
        self.class_probs = {cls: np.mean(y == cls) for cls in self.classes}

        # Calculate feature probabilities for each class
        self.feature_probs = {cls: np.zeros(n_features) for cls in self.classes}
        for cls in self.classes:
            X_cls = X[y == cls]
            feature_counts = np.sum(X_cls, axis=0) + 1  # Adding 1 for Laplace smoothing
            total_count = X_cls.shape[0] + len(self.classes)  # Total count + number of classes for smoothing
            self.feature_probs[cls] = feature_counts / total_count

    def predict(self, X):
        predictions = []
        for sample in X:
            probs = {}
            for cls in self.classes:
                class_prob = np.log(self.class_probs[cls])
                feature_prob = np.sum(np.log(self.feature_probs[cls]) * sample)
                probs[cls] = class_prob + feature_prob
            predictions.append(max(probs, key=probs.get))
        return np.array(predictions)

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

    # Initialize and train the Naive Bayes classifier
    nb = NaiveBayesClassifier()
    nb.fit(X_train, y_train)

    # Make predictions
    y_pred = nb.predict(X_test)

    # Evaluate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')

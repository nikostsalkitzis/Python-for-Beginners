import numpy as np

class PCA:
    def __init__(self, n_components=None):
        self.n_components = n_components
        self.mean = None
        self.components = None
        self.explained_variance = None

    def fit(self, X):
        # Standardize the data
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean

        # Compute the covariance matrix
        covariance_matrix = np.cov(X_centered, rowvar=False)

        # Eigenvalue decomposition
        eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

        # Sort eigenvectors by eigenvalues in descending order
        sorted_indices = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[sorted_indices]
        eigenvectors = eigenvectors[:, sorted_indices]

        # Select the top n_components eigenvectors
        if self.n_components is not None:
            eigenvectors = eigenvectors[:, :self.n_components]
        
        self.components = eigenvectors
        self.explained_variance = eigenvalues[:self.n_components] if self.n_components is not None else eigenvalues

    def transform(self, X):
        # Center the data
        X_centered = X - self.mean
        # Project data onto principal components
        return np.dot(X_centered, self.components)

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

# Example usage
if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler
    import matplotlib.pyplot as plt

    # Load and standardize the data
    data = load_iris()
    X = data.data
    y = data.target

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    # Plot the results
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
    plt.colorbar(scatter, label='Target label')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA of Iris Dataset')
    plt.show()

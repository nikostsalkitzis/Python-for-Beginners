import numpy as np

class SVM:
    def __init__(self, C=1.0, tol=1e-3, max_passes=5):
        self.C = C
        self.tol = tol
        self.max_passes = max_passes

    def fit(self, X, y):
        self.X = X
        self.y = y
        self.m, self.n = X.shape
        
        # Initialize alpha and b
        self.alpha = np.zeros(self.m)
        self.b = 0
        
        passes = 0
        while passes < self.max_passes:
            num_changed_alphas = 0
            for i in range(self.m):
                E_i = self._predict(self.X[i]) - self.y[i]
                
                if (self.y[i] * E_i < -self.tol and self.alpha[i] < self.C) or (self.y[i] * E_i > self.tol and self.alpha[i] > 0):
                    j = self._select_j(i)
                    E_j = self._predict(self.X[j]) - self.y[j]
                    
                    alpha_i_old = self.alpha[i]
                    alpha_j_old = self.alpha[j]
                    
                    if self.y[i] != self.y[j]:
                        L = max(0, self.alpha[j] - self.alpha[i])
                        H = min(self.C, self.C + self.alpha[j] - self.alpha[i])
                    else:
                        L = max(0, self.alpha[i] + self.alpha[j] - self.C)
                        H = min(self.C, self.alpha[i] + self.alpha[j])
                    
                    if L == H:
                        continue
                    
                    eta = 2.0 * self._kernel(self.X[i], self.X[j]) - self._kernel(self.X[i], self.X[i]) - self._kernel(self.X[j], self.X[j])
                    if eta >= 0:
                        continue
                    
                    self.alpha[j] -= self.y[j] * (E_i - E_j) / eta
                    self.alpha[j] = np.clip(self.alpha[j], L, H)
                    
                    if abs(self.alpha[j] - alpha_j_old) < 1e-5:
                        self.alpha[j] = alpha_j_old
                        continue
                    
                    self.alpha[i] += self.y[i] * self.y[j] * (alpha_j_old - self.alpha[j])
                    
                    b1 = self.b - E_i - self.y[i] * (self.alpha[i] - alpha_i_old) * self._kernel(self.X[i], self.X[i]) - self.y[j] * (self.alpha[j] - alpha_j_old) * self._kernel(self.X[i], self.X[j])
                    b2 = self.b - E_j - self.y[i] * (self.alpha[i] - alpha_i_old) * self._kernel(self.X[i], self.X[j]) - self.y[j] * (self.alpha[j] - alpha_j_old) * self._kernel(self.X[j], self.X[j])
                    
                    if 0 < self.alpha[i] < self.C:
                        self.b = b1
                    elif 0 < self.alpha[j] < self.C:
                        self.b = b2
                    else:
                        self.b = (b1 + b2) / 2.0
                    
                    num_changed_alphas += 1
            
            if num_changed_alphas == 0:
                passes += 1
            else:
                passes = 0
        
        self.w = np.sum(self.alpha[:, np.newaxis] * self.y[:, np.newaxis] * self.X, axis=0)
        
    def _predict(self, X):
        return np.dot(X, self.w) + self.b
    
    def _kernel(self, x1, x2):
        return np.dot(x1, x2)
    
    def decision_function(self, X):
        return self._predict(X)
    
    def predict(self, X):
        return np.sign(self.decision_function(X))

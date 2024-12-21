from sklearn.decomposition import PCA
import numpy as np

def apply_pca(df, columns, n_components=2):
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(df[columns])
    explained_variance = np.sum(pca.explained_variance_ratio_)
    return principal_components, explained_variance

def interpret_pca(pca_results, explained_variance):
    print(f"Explained variance by principal components: {explained_variance}")
    print(f"First component contributes {pca_results[0,0]:.2f}, second component contributes {pca_results[0,1]:.2f}")

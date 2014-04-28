'''Implement feature selection/dimensionality reduction algorithms'''

from sklearn.decomposition import PCA

'''Principal Component Analysis (PCA)
Adapted from: http://scikit-learn.org/stable/_downloads/plot_pca_vs_lda.py
Args:
	- data_matrix: a matrix-like object containing the data, columns
	for features and rows for an item (developer in this case)
	- n_components: the number of principal components to be extracted
	(0 < n_components <= #features)
Return:
	- a matrix-like object contained the transformed data with n_components
	columns
'''
def pca(data_matrix, n_components):
	pca_obj = PCA(n_components=n_components)
	transformed_matrix = pca_obj.fit(data_matrix).transform(data_matrix)
	return transformed_matrix
	
'''Linear Discriminant Analysis (LDA)
Adapted from: http://scikit-learn.org/stable/_downloads/plot_pca_vs_lda.py
Args:
	- data_matrix: a matrix-like object containing the data, columns
	for features and rows for an item (developer in this case)
	- target: an array-like object contaning the class of the data item
	(developer) at the respective row
	- n_components: the number of principal components to be extracted
	(0 < n_components <= #features)
Return:
	- a matrix-like object contained the transformed data with n_components
	columns
'''
def lda(data_matrix, target, n_components):
	lda_obj = LDA(n_components=n_components)
	transformed_matrix = lda_obj.fit(data_matrix, target).transform(data_matrix)
	return transformed_matrix

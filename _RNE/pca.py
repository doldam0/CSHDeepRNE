from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from csv_to_list import get_data


X, y = get_data('data_classify.csv', 1)

standardizedData = StandardScaler().fit_transform(X, y)

pca = PCA(n_components=2)

principalComponents = pca.fit_transform(X = standardizedData)

# to get how much variance was retained
print(pca.explained_variance_ratio_.sum())
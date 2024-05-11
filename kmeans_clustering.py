from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.datasets import fetch_20newsgroups
import joblib

# Load sample dataset (20 newsgroups)
dataset = fetch_20newsgroups(subset='all', shuffle=True, random_state=42)

# Preprocess the text data
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(dataset.data)

# Choose the number of clusters (K)
num_clusters = 20  # Example: clustering into 20 categories (20 newsgroups)

# Initialize K-means clustering algorithm
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

# Fit K-means to the TF-IDF vectors
kmeans.fit(X)

# Get the cluster labels and assign them to each document
cluster_labels = kmeans.labels_

# Evaluate clustering using silhouette score
silhouette_avg = silhouette_score(X, cluster_labels)
print(f"Silhouette Score: {silhouette_avg}")

# Print the top terms per cluster
order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names_out()

for i in range(num_clusters):
    print(f"Cluster {i+1}:")
    top_terms = [terms[ind] for ind in order_centroids[i, :10]]
    print(top_terms)

# Save the trained K-means model
joblib.dump(kmeans, 'kmeans_model.pkl')

# Save the TF-IDF vectorizer
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

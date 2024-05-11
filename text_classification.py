from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Step 1: Load the 20 newsgroups dataset
data = fetch_20newsgroups()

# Step 2: Preprocess the data (not shown for brevity)

# Step 3: Feature extraction using TF-IDF
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(data.data)
y = data.target

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Step 6: Evaluate the classifier
predicted = classifier.predict(X_test)
accuracy = metrics.accuracy_score(y_test, predicted)
precision = metrics.precision_score(y_test, predicted, average='weighted')
recall = metrics.recall_score(y_test, predicted, average='weighted')
f1_score = metrics.f1_score(y_test, predicted, average='weighted')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1_score)

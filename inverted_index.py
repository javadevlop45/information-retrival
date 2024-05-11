class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_document(self, doc_id, text):
        words = text.lower().split()  # Convert text to lowercase for case-insensitive search
        for word in words:
            if word not in self.index:
                self.index[word] = set()
            self.index[word].add(doc_id)

    def search(self, query):
        words = query.lower().split()  # Convert query to lowercase for case-insensitive search
        result = None
        for word in words:
            if word in self.index:
                if result is None:
                    result = self.index[word]
                else:
                    result = result.intersection(self.index[word])
        return result if result is not None else set()


# Example usage:
index = InvertedIndex()
index.add_document(1, "This is a sample document")
index.add_document(2, "Another document for testing")
index.add_document(3, "Sample text for testing")

query = "sample testing"
result = index.search(query)
print("Documents containing the words 'sample' and 'testing':", result)

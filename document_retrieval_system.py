from inverted_index import InvertedIndex

class DocumentRetrievalSystem:
    def __init__(self, index):
        self.index = index

    def search_documents(self, query):
        result = self.index.search(query)
        return result


# Example usage:
index = InvertedIndex()
index.add_document(1, "This is a sample document")
index.add_document(2, "Another document for testing")
index.add_document(3, "Sample text for testing")

retrieval_system = DocumentRetrievalSystem(index)
query = "sample testing"
result = retrieval_system.search_documents(query)
print("Documents containing the words 'sample' and 'testing':", result)

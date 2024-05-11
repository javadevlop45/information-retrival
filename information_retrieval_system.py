class InformationRetrievalSystem:
    def __init__(self, index, spelling_corrector):
        self.index = index
        self.spelling_corrector = spelling_corrector

    def search_documents(self, query):
        corrected_query = ' '.join([self.spelling_corrector.correct_spelling(word) for word in query.split()])
        result = self.index.search(corrected_query)
        return result


# Example usage:
index = InvertedIndex()  # Assume InvertedIndex class from previous example
retrieval_system = InformationRetrievalSystem(index, corrector)

query = "aple orenge"
result = retrieval_system.search_documents(query)
print("Documents containing the corrected words:", result)

class SpellingCorrector:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def levenshtein_distance(self, word1, word2):
        # Initialize a matrix to store distances
        distances = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # Initialize first row and column
        for i in range(len(word1) + 1):
            distances[i][0] = i
        for j in range(len(word2) + 1):
            distances[0][j] = j

        # Fill the matrix
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                cost = 0 if word1[i - 1] == word2[j - 1] else 1
                distances[i][j] = min(
                    distances[i - 1][j] + 1,  # deletion
                    distances[i][j - 1] + 1,  # insertion
                    distances[i - 1][j - 1] + cost  # substitution
                )

        return distances[len(word1)][len(word2)]

    def correct_spelling(self, word):
        min_distance = float('inf')
        corrected_word = word

        for candidate in self.dictionary:
            distance = self.levenshtein_distance(word, candidate)
            if distance < min_distance:
                min_distance = distance
                corrected_word = candidate

        return corrected_word


# Example usage:
dictionary = ['apple', 'banana', 'orange', 'pear', 'peach']
corrector = SpellingCorrector(dictionary)
word = 'aple'
corrected_word = corrector.correct_spelling(word)
print("Original word:", word)
print("Corrected word:", corrected_word)

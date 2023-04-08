from scipy.sparse import vstack
from chatterbot.logic import LogicAdapter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.language = kwargs.get('language', 'fr')
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None
        self.conversation = []

    def can_process(self, statement):
        return True

    def process(self, statement, additional_response_selection_parameters=None):
        self.conversation.append(statement)
        sentences = [conv.text for conv in self.conversation]
        prompt_tfidf = self.vectorizer.transform([statement.text])
        if self.tfidf_matrix is None:
            self.tfidf_matrix = prompt_tfidf
            similarity_list = [0]
        else:
            self.tfidf_matrix = vstack([self.tfidf_matrix, prompt_tfidf])
            similarity_matrix = cosine_similarity(self.tfidf_matrix)
            similarity_list = list(similarity_matrix[-1, :-1])
        response = self.conversation[similarity_list.index(max(similarity_list))]
        return response.text

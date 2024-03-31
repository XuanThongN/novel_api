# ml_model.py
import pickle


class ToxicCommentClassifier:
    def __init__(self):
        with open('novel_api/backend/toxic_detect_model.pkl', 'rb') as moddel_file:
            self.model = pickle.load(moddel_file)
        with open('novel_api/backend/vectorizer.pkl', 'rb') as vectorizer_file:
            self.vectorizer = pickle.load(vectorizer_file)

    def predict(self, comment_text):
        preprocessed_text = self.vectorizer.transform([comment_text])
        prediction = self.model.predict(preprocessed_text)
        is_toxic = prediction[0] == 'Toxic'
        return is_toxic

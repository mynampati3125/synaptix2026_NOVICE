from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(industry_text, startup_text):
    documents = [industry_text, startup_text]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)


def risk_analysis(startup_stage):
    risk_map = {
        "Idea": 70,
        "Prototype": 50,
        "MVP": 30,
        "Scaling": 10
    }
    return risk_map.get(startup_stage, 50)


def collaboration_score(match_percentage, risk_score):
    final_score = match_percentage - (risk_score * 0.2)
    return round(final_score, 2)

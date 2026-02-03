from sklearn.metrics.pairwise import cosine_similarity

def user_based_recommendation(user_item_matrix):
    similarity = cosine_similarity(user_item_matrix)
    return similarity

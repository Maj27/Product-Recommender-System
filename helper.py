import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re
from camel_tools.utils.normalize import normalize_unicode
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import scipy.sparse as sp
from sklearn.metrics.pairwise import cosine_similarity


file_path ='./csv_for_case_study_V1.csv'
df = pd.read_csv(file_path)

sample_size = 50000  
df_sampled = df.sample(n=sample_size, random_state=42)



# Function to remove non-Arabic characters (keeping only Arabic letters and whitespace)
def remove_non_arabic(text):
    # This regex keeps only characters in the Arabic Unicode block (\u0600-\u06FF) and spaces
    arabic_text = re.sub(r'[^\u0600-\u06FF\s]', '', text)
    return arabic_text.strip()

# Initialize the built-in ar2bw mapper from Camel Tools
#ar2bw_mapper = CharMapper.builtin_mapper('ar2bw')

# Define the preprocessing function that applies non-Arabic removal and then converts text using ar2bw
def preprocess_arabic_text(text):
    # Remove non-Arabic characters
    text_arabic = remove_non_arabic(text)
    # Map the Arabic text to its Buckwalter representation using ar2bw
    text_bw = normalize_unicode(text_arabic)
    return text_bw


df_sampled['preprocessed_text'] = df_sampled['product_name'].apply(preprocess_arabic_text)

# Drop duplicates and handle missing values
df_sampled.drop_duplicates(subset=['product_id'], inplace=True) 
df_sampled = df_sampled[df_sampled['preprocessed_text'].notna()]

# Encode categorical event types
df_sampled['Event_encoded'] = df_sampled['Event'].astype('category').cat.codes


# Create a TF-IDF vectorizer instance (you can adjust parameters like ngram_range if needed)
vectorizer = TfidfVectorizer(ngram_range=(1,2))  # using unigrams and bigrams can capture some context
tfidf_matrix = vectorizer.fit_transform(df_sampled['preprocessed_text'])


svd = TruncatedSVD(n_components=300, random_state=42)
reduced_matrix = svd.fit_transform(tfidf_matrix)


# Compute the cosine similarity matrix for all products
cosine_sim = cosine_similarity(reduced_matrix, reduced_matrix)


def get_recommendations(product_index, top_n=10, sim_threshold=0.6):
    # Get pairwise similarity scores for the given product
    sim_scores = list(enumerate(cosine_sim[product_index]))
    # Filter products with similarity above threshold and not the same product
    filtered_scores = [score for score in sim_scores if score[1] > sim_threshold and score[0] != product_index]
    # Sort products based on similarity score
    filtered_scores = sorted(filtered_scores, key=lambda x: x[1], reverse=True)
    # Select top_n recommendations
    product_indices = [i[0] for i in filtered_scores[:top_n]]
    return df_sampled.iloc[product_indices][['product_id', 'product_name']]

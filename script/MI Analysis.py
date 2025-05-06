import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import mutual_info_classif
import pandas as pd
import numpy as np

def extract_last_teacher_questions(data):
    # Initialize lists to store questions by category
    least_questions = []
    more_questions = []
    most_questions = []
    
    # Process the data
    for obj in data:
        for problem_id, problem_data in obj.items():
            # Extract from each category if available
            for category, questions_list in [("least", least_questions), 
                                            ("more", more_questions), 
                                            ("most", most_questions)]:
                if category in problem_data:
                    dialogue = problem_data[category]
                    
                    # Find the last teacher's question
                    lines = dialogue.split('\n')
                    teacher_lines = [line for line in lines if line.startswith('Teacher: ')]
                    
                    if teacher_lines:
                        questions_list.append(teacher_lines[-1])
    
    # Return the grouped questions
    return {
        "least": least_questions,
        "more": more_questions,
        "most": most_questions
    }

# Load the JSON data
with open('full_question_solution_latest.json', 'r') as f:
    data = json.load(f)

# Extract and group the questions
grouped_questions = extract_last_teacher_questions(data)

# Strip the words "Teacher: " from the questions
for category in grouped_questions:
    grouped_questions[category] = [question.replace('Teacher: ', '') for question in grouped_questions[category]]

# # Print sample questions from each category
# for category, questions in grouped_questions.items():
#     print(f"Sample questions from '{category}' category:")
#     for question in questions[:5]:  # Print first 5 questions from each category
#         print(question)
#     print("\n")

# Prepare corpus and labels
def prepare_corpus_and_labels(data):
    corpus = []
    labels = []
    for label, texts in data.items():
        corpus.extend(texts)
        labels.extend([label] * len(texts))
    
    # Vectorize the corpus
    vectorizer = CountVectorizer(lowercase=True, stop_words='english', min_df=1)
    X = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names_out()

    # Compute the mutual information scores
    results = {}
    for cls in data:
        y_bin = np.array([1 if lbl == cls else 0 for lbl in labels])
        mi_scores = mutual_info_classif(X, y_bin, discrete_features=True)
        freq_pos = X[y_bin == 1].sum(axis=0).A1 / y_bin.sum()
        freq_neg = X[y_bin == 0].sum(axis=0).A1 / (len(labels) - y_bin.sum())
        df = pd.DataFrame({
            'feature': feature_names,
            'mi': mi_scores,
            'freq_in_pos': freq_pos,
            'freq_in_neg': freq_neg
        })

        # Keep only those present in-class
        # To see how "explain" is contrastive to "most", remove this line
        df = df[df['freq_in_pos'] > 0].copy()
        df.sort_values('mi', ascending=False, inplace=True)
        results[cls] = df

    # 4. Print top 10 per class
    for cls, df in results.items():
        print(f"\nTop 10 features for '{cls}' (occurring in class):")
        print(df[['feature','mi','freq_in_pos']].head(10).to_string(index=False))

prepare_corpus_and_labels(grouped_questions)

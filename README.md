This repository contains code and data for paper "IndirectScore: An Automatic Evaluation Metric for Socratic AI Tutor’s Responses"

## Project Structure
Socratic questions are meant to be "indirect", not revealing the answers to the students and instead offer only small assistance and allow them to explore the concept by themselves. How can we actually measure this? Current standard relies on expert annotation, which is time-consuming and resource intensive, and thus, limits the scalability of effective AI tutor development. To our knowledge, this study offers the first automatic metric that can capture the nuanced questioninig of a Socratic prompt and advances the field of educational NLP research and application. We also provided augmented datasets for future research in this direction. Our approach utilises theories from multiple discipline including education and linguistic, and focuses on the impact of advancement of NLP techniques beyond the machine learning community. This multi-facet approach yielded strong performance, despite the lack of high quality dataset.

Furthermore, the analysis shows statistical differences between the log probability scores for different levels of question directness, with p-values indicating significant effects between "least" and "most" direct questioning styles. However, confound factors such as Relevance must be controlled beforehand for correct interpretability. In this study, we controlled for this noise through careful data curation, manual inspection, and a baseline of BERTScore and ROUGE-L for simple semantic overlaps.

### Dataset/
- full_question_solution_latest.json: Contains a collection of programming problems, their solutions, and dialogue examples with varying levels of directness (least, more, most) for tutor questions.

### Result/
- log_prob_score_codellama.json: Log probability scores calculated using the CodeLlama model.
- `log_prob_score_qwen.json`: Log probability scores calculated using the Qwen model.
- `log_probability_boxplot.png`: Visualization showing the distribution of log probability scores.
- `log_probability_boxplot_no_outliers.png`: Visualization with outliers removed for clearer comparison.

### script/
- MainMethod.ipynb: The primary notebook that:
  - Loads the dataset of programming problems and solutions
  - Implements the log probability calculation method using language models
  - Computes log probabilities for different levels of question directness

- ResultAnalysis.py
  - Calculates accuracy metrics
  - Performs statistical analysis using Wilcoxon tests
  - Sorts and compares the effectiveness of different question styles

- `Data Visualisation.ipynb`: Creates visualizations of the results including:
  - Boxplot comparisons between different models and question directness levels
  - Summary statistics for each dataset
  - Outlier removal for clearer visualization

## How It Works

The project calculates an "IndirectScore" by measuring how well language models can predict a correct solution to a programming problem based on questions with varying levels of directness.
The methodology includes:
1. Loading programming problems with tutor questions of varying directness
2. Using language models to calculate log probabilities of generating correct solutions
3. Comparing log probabilities across different directness levels
4. Statistical analysis to determine significance of the results
5. Visualization to present findings

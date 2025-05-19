This repository contains code and data for paper "Towards Automated Evaluation of Socratic Tutoring: Introducing IndirectScore for Programming Education."

## Outputs
We propose IndirectScore, a preliminary automated metric that uses language-model surprisal to estimate the indirectness of Socratic tutor questions while controlling for topical relevance. To support evaluation, we build and release a small benchmark of 168 programming-education dialogues labelled at three indirectness levels (BEST, MEDIUM, WORST). On this set, IndirectScore aligns with expert judgements in about 71 % of pairwise comparisons and exceeds ROUGE-L and BERTScore, suggesting that answer-predictability offers a useful signal beyond surface overlap. Although the study is limited by dataset size and domain scope, IndirectScore provides an initial, scalable tool for analysing question quality in AI tutoring and related dialogue settings.

## Project Structure

### Dataset/
- full_context_processed.json: Contains a collection of programming problems, their solutions, and dialogue examples with varying levels of directness (least, more, most) for tutor questions.
- OnlyNextQ_processed.json: Ablation dataset with conversation removed, keeping only NextQ

### Result/
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
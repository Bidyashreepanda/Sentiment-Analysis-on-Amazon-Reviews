# 🍎 Amazon Fine Food Reviews – Sentiment Analysis

<h1 align="center">📊 Amazon Review Sentiment Analysis</h1>

<h3 align="center">Turning Customer Reviews into Meaningful Insights Using NLP & Machine Learning</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Machine_Learning-FF6F00?style=for-the-badge" />
  <img src="https://img.shields.io/badge/NLP-8A2BE2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
</p>

---

## 🌟 Project Overview

**Amazon Review Sentiment Analysis** is an NLP and Machine Learning project designed to understand customer opinions from Amazon Fine Food product reviews.

The project uses Natural Language Processing techniques and multiple Machine Learning algorithms to predict customer ratings based on review text.

It also classifies customer feedback into three sentiment categories:

- 🟢 **Positive** – Ratings 4 and 5
- 🟡 **Neutral** – Rating 3
- 🔴 **Negative** – Ratings 1 and 2

The project covers the complete Machine Learning workflow, from data exploration and preprocessing to model development, optimization, and deployment using Streamlit.

## 🎯 Project Objectives

- Analyze customer feedback and review patterns.
- Perform text cleaning and preprocessing using NLP.
- Extract meaningful features using BoW and TF-IDF.
- Build and compare multiple Machine Learning models.
- Optimize model performance through hyperparameter tuning.
- Develop an interactive web application for sentiment prediction.

---

## 📂 Dataset Information

**Dataset:** Amazon Fine Food Reviews

**Source:** [Kaggle – Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)

| Dataset Statistics | Details |
|:---|---:|
| Total Reviews | 568,454 |
| Total Users | 256,059 |
| Total Products | 74,258 |
| Time Period | 1999–2012 |

### Dataset Features

| Feature | Description |
|:---|:---|
| Id | Unique review ID |
| ProductId | Product identifier |
| UserId | User identifier |
| ProfileName | Reviewer name |
| HelpfulnessNumerator | Helpful votes |
| HelpfulnessDenominator | Total votes |
| Score | Product rating (1–5) |
| Time | Review timestamp |
| Summary | Short review summary |
| Text | Complete review text |

---

## 🛠️ Tech Stack & Tools

| Category | Technologies |
|:---|:---|
| Programming | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| NLP | NLTK |
| Feature Engineering | CountVectorizer, TF-IDF |
| Machine Learning | Scikit-learn |
| Model Optimization | GridSearchCV |
| Model Serialization | Joblib |
| Web Application | Streamlit |
| Development Environment | Jupyter Notebook |

---

## 🔄 Project Workflow

The project is divided into four major sprints.

### 🔹 Sprint 1 – Exploratory Data Analysis & Text Preprocessing

**Data Cleaning**
- Handled missing values.
- Removed duplicate records.
- Analyzed rating distribution.
- Converted timestamps.
- Calculated helpfulness ratio.

**Text Preprocessing**
- Lowercase conversion.
- HTML tag removal.
- URL removal.
- Punctuation removal.
- Stopword removal.
- Tokenization.
- Stemming / Lemmatization.

**📊 Exploratory Data Analysis**
- Rating distribution and percentage.
- Positive and negative review word frequency.
- Positive and negative word clouds.
- Review length distribution.
- Average review length by rating.
- Helpfulness ratio analysis.
- Top reviewed products.
- Most active users.

### 🔹 Sprint 2 – Machine Learning Model Development

Implemented different text vectorization techniques:

**Feature Extraction**
- Bag of Words (BoW)
- TF-IDF Vectorizer

**Machine Learning Algorithms**

| Algorithm | Purpose |
|:---|:---|
| Naive Bayes | Probabilistic classification |
| Logistic Regression | Linear classification |
| Support Vector Machine | Maximum-margin classification |
| Decision Tree | Rule-based classification |
| Random Forest | Ensemble learning |
| K-Nearest Neighbors | Distance-based classification |

### 🔹 Sprint 3 – Hyperparameter Tuning & Optimization

- Selected the best-performing baseline model.
- Applied GridSearchCV.
- Optimized model hyperparameters.
- Compared baseline and tuned performance.
- Analyzed important words and model coefficients.
- Saved the final trained model using Joblib.

### 🔹 Sprint 4 – Streamlit Web Application

Developed an interactive web application that allows users to:

- ✍️ Enter a product review.
- 🚀 Click the Predict Sentiment button.
- ⭐ Get the predicted product rating.
- 💬 View the predicted sentiment category.

---

## 📈 Model Evaluation

The models are evaluated using the following metrics:

| Evaluation Metric | Purpose |
|:---|:---|
| Accuracy | Overall prediction correctness |
| Precision | Correct positive predictions |
| Recall | Ability to identify actual classes |
| F1-Score | Balance between precision and recall |
| Confusion Matrix | Visualize classification performance |
| Classification Report | Detailed class-wise performance |

### 🏆 Model Comparison

The performance of all six Machine Learning algorithms is compared to identify the most suitable model.

> Add your actual model comparison results here after running the experiments.

---

## 🖥️ Application Preview

### Amazon Review Sentiment Prediction

**Example Input:**

```text
This product is amazing! 
The quality is excellent and I really love it.
```

**Expected Output Format:**

| Prediction | Result |
|:---|:---|
| ⭐ Predicted Rating | 5 / 5 |
| 💬 Sentiment | Positive |

*Example output format only; actual predictions depend on the trained model.*

> 📸 Add a screenshot of your Streamlit application here.

---

## 📁 Project Structure

```text
Amazon-Review-Sentiment-Analysis/
│
├── 📓 EDA and Feature Engineering.ipynb
│
├── 📓 Model_Building and Evaluation.ipynb
│
├── 🤖 sentiment_model.pkl
│
├── 🌐 app.py
│
├── 📦 requirements.txt
│
└── 📄 README.md
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2️⃣ Navigate to Project Directory

```bash
cd Amazon-Review-Sentiment-Analysis
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv myenv
```

### 4️⃣ Activate Virtual Environment

```bash
myenv\Scripts\activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run Streamlit Application

```bash
python -m streamlit run app.py
```

🎉 The application will open in your browser:

`http://localhost:8501`

---

## 📦 Requirements

The project uses the following Python libraries:

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
nltk
streamlit
joblib
```

---

## 🚀 Future Enhancements

- Implement advanced NLP models such as BERT.
- Improve model prediction performance.
- Add interactive sentiment analytics dashboards.
- Deploy the application using Streamlit Community Cloud.
- Explore aspect-based sentiment analysis.
- Support larger review datasets.

---

## 🎓 Key Learnings

Through this project, I gained practical experience in:

- Exploratory Data Analysis and Data Cleaning.
- Natural Language Processing.
- Text Feature Engineering.
- Machine Learning Classification.
- Model Evaluation and Optimization.
- Model Deployment using Streamlit.
- End-to-end Data Science project development.

---

## 👩‍💻 About the Author

### Bidyashree Panda

Aspiring Data Analyst | Data Science & Machine Learning Enthusiast

Passionate about transforming raw data into meaningful insights using Python, Data Analytics, NLP, and Machine Learning.

<p>
  <a href="https://github.com/Bidyashreepanda">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://linkedin.com/in/bidyashree-panda">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
</p>

---

<p align="center">
  ⭐ If you find this project interesting, don't forget to star the repository!
</p>

<p align="center">
  <b>Made with ❤️ using Python, NLP & Machine Learning</b>
</p>

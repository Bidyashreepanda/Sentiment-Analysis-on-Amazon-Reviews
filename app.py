
import streamlit as st
import joblib
import re
import string

# Load saved model
artifact = joblib.load("sentiment_model.pkl")

vectorizer = artifact['vectorizer']
model = artifact['model']
stop_words = artifact['stop_words']


# Text preprocessing
def preprocess_text(text):

    text = text.lower()

    # Remove HTML tags
    text = re.sub(r'<.*?>', ' ', text)

    # Remove URLs
    text = re.sub(
        r'http\S+|www\S+|https\S+',
        ' ',
        text
    )

    # Remove punctuation
    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    # Remove stopwords
    words = text.split()

    words = [
        word for word in words
        if word not in stop_words
    ]

    return ' '.join(words)


# Streamlit UI
st.set_page_config(
    page_title="Amazon Review Sentiment Analysis",
    page_icon="⭐",
    layout="centered"
)

st.title("Amazon Review Sentiment Analysis")

st.write(
    "Enter a product review to predict its rating and sentiment."
)

review = st.text_area(
    "Enter Your Product Review",
    placeholder="Write your review here..."
)

if st.button("Predict Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a review.")

    else:

        cleaned_review = preprocess_text(review)

        review_vector = vectorizer.transform(
            [cleaned_review]
        )

        prediction = model.predict(review_vector)[0]

        # Convert rating to sentiment
        if prediction in [1, 2]:
            sentiment = "Negative"
        elif prediction == 3:
            sentiment = "Neutral"
        else:
            sentiment = "Positive"

        st.success("Prediction Completed!")

        st.subheader("Prediction Result")

        st.metric(
            "Predicted Rating",
            f"{prediction} / 5"
        )

        st.write("Sentiment:", sentiment)

        st.write("Original Review:", review)

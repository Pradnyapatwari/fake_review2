import streamlit as st

# Dictionary of known fake reviews and their associated patterns
fake_review_patterns = {
    "This product is amazing!": ["amazing", "life-changing", "best ever", "unbelievable"],
    "I got a free product for this review.": ["free product", "sponsored", "incentive", "gift"],
    "Don't waste your money.": ["scam", "ripoff", "don't buy", "waste of money"],
}

def detect_fake_review(review_text):
    for fake_review, patterns in fake_review_patterns.items():
        if any(pattern in review_text.lower() for pattern in patterns):
            return True
    return False

st.title("Fake Review Detector")
st.write("Enter a product review below:")

review_text = st.text_area("Review Text")

if st.button("Detect"):
    if review_text:
        if detect_fake_review(review_text):
            st.error("This review appears to be fake.")
        else:
            st.success("This review seems genuine.")
    else:
        st.warning("Please enter a review.")

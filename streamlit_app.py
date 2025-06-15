import streamlit as st

# Set page layout
st.set_page_config(page_title="Drug Vulnerability Quiz", layout="centered")

# Initialize session state
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

# Score mapping for each question
scoring = {
    "q1": {"Never": 0, "Rarely": 0, "Sometimes": 1, "Often": 2, "Very Often": 3},
    "q2": {
        "I seek help or talk to someone": 0,
        "I distract myself in healthy ways (exercise, hobbies)": 1,
        "I isolate myself or bottle it up": 2,
        "I rely on substances to manage my emotions": 4
    },
    "q3": {
        "Yes, I have strong and reliable support": 0,
        "Some support, but it’s inconsistent": 1,
        "Very limited or occasional support": 2,
        "No real support network": 4
    },
    "q4": {
        "No, and I’ve never been tempted": 0,
        "I've thought about it but never tried": 1,
        "I've experimented once or twice": 2,
        "I’ve used occasionally or regularly": 4
    },
    "q5": {"Never": 0, "Rarely": 0, "Sometimes": 1, "Often": 2, "Very Often": 3},
    "q6": {
        "I believe drugs are harmful and avoid them": 0,
        "They can be harmful, but some people use them socially": 1,
        "I don't think much about it either way": 2,
        "I believe they can be helpful or not dangerous": 3
    },
    "q7": {
        "Very satisfied and fulfilled": 0,
        "Generally satisfied with occasional stress": 1,
        "Often feel dissatisfied or directionless": 2,
        "Regularly overwhelmed or unhappy": 3
    }
}

# If already submitted, only show results
if st.session_state["submitted"]:
    st.title("📊 Your Drug Vulnerability Analysis")

    # Retrieve previous answers
    score = sum([
        scoring["q1"][st.session_state["q1"]],
        scoring["q2"][st.session_state["q2"]],
        scoring["q3"][st.session_state["q3"]],
        scoring["q4"][st.session_state["q4"]],
        scoring["q5"][st.session_state["q5"]],
        scoring["q6"][st.session_state["q6"]],
        scoring["q7"][st.session_state["q7"]],
    ])

    # Display results
    if score >= 12:
        st.error("⚠️ **High Vulnerability**\n\nYou may be at significant risk. Please consider speaking with a counselor, mental health professional, or trusted adult.")
    elif score >= 6:
        st.warning("⚠️ **Moderate Vulnerability**\n\nYou may be facing challenges that increase vulnerability. Focus on healthy coping, seek support, and be aware of potential triggers.")
    else:
        st.success("✅ **Low Vulnerability**\n\nYou seem to have protective factors in place. Continue maintaining a healthy lifestyle and support network.")

    st.markdown("---")
    st.info("This assessment is for self-awareness only. If you feel at risk, reach out to a trusted person or professional for guidance.")

else:
    # Quiz interface (only shown if not yet submitted)
    st.title("🚨 Drug Vulnerability Assessment")
    st.markdown("This quiz is for **self-reflection** only. Your answers will help you assess how certain factors may relate to potential vulnerability to drug use.")

    # Questions
    st.header("1. How often do you feel overwhelmed by stress or anxiety?")
    st.radio("Select one:", ["Never", "Rarely", "Sometimes", "Often", "Very Often"], key="q1")

    st.header("2. How do you usually cope with negative emotions or stress?")
    st.radio("Select one:", [
        "I seek help or talk to someone",
        "I distract myself in healthy ways (exercise, hobbies)",
        "I isolate myself or bottle it up",
        "I rely on substances to manage my emotions"
    ], key="q2")

    st.header("3. Do you feel you have a dependable support system?")
    st.radio("Select one:", [
        "Yes, I have strong and reliable support",
        "Some support, but it’s inconsistent",
        "Very limited or occasional support",
        "No real support network"
    ], key="q3")

    st.header("4. Have you ever experimented with or used drugs?")
    st.radio("Select one:", [
        "No, and I’ve never been tempted",
        "I've thought about it but never tried",
        "I've experimented once or twice",
        "I’ve used occasionally or regularly"
    ], key="q4")

    st.header("5. How often do you engage in risky behaviors (e.g., reckless driving, unsafe activities)?")
    st.radio("Select one:", ["Never", "Rarely", "Sometimes", "Often", "Very Often"], key="q5")

    st.header("6. What is your attitude toward drug use?")
    st.radio("Select one:", [
        "I believe drugs are harmful and avoid them",
        "They can be harmful, but some people use them socially",
        "I don't think much about it either way",
        "I believe they can be helpful or not dangerous"
    ], key="q6")

    st.header("7. How satisfied are you with your current lifestyle and well-being?")
    st.radio("Select one:", [
        "Very satisfied and fulfilled",
        "Generally satisfied with occasional stress",
        "Often feel dissatisfied or directionless",
        "Regularly overwhelmed or unhappy"
    ], key="q7")

    # Submit button
    if st.button("Get Your Result"):
        st.session_state["submitted"] = True
        st.experimental_rerun()

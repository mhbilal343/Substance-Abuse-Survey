import streamlit as st

# Set page layout and remove header/banner
st.set_page_config(page_title="Drug Risk Assessment", layout="centered")
st.markdown("""
    <style>
        .stApp {
            background-color: white;
            color: black;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            color: black;
        }
        label, h1, h2, h3, h4, h5, h6, p, span, div {
            color: black !important;
        }
        header, footer {display: none !important;}
        .st-emotion-cache-1avcm0n {display: none !important;}
        .stButton>button {
            background-color: #ff4d4d;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #ff6666;
        }
    </style>
""", unsafe_allow_html=True)

privacy_policy_text = """
By taking this assessment, you agree that the data collected will be used for educational purposes only. 
Your answers will be kept confidential and will not be shared with any third parties. 
This survey is designed to assess potential vulnerability to drug use and offer guidance based on your answers. 
The data will be used solely for statistical analysis and to raise awareness about substance use.
"""

# Session state initialization
if "accepted_policy" not in st.session_state:
    st.session_state.accepted_policy = False
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_survey" not in st.session_state:
    st.session_state.show_survey = False

# Privacy Policy Display
if not st.session_state.accepted_policy:
    st.title("Drug Risk Assessment")
    st.markdown("### **Privacy Policy**", unsafe_allow_html=True)
    st.write(privacy_policy_text)
    
    if st.button("I Accept and Begin the Survey"):
        st.session_state.accepted_policy = True
        st.session_state.submitted = False
        st.session_state.score = 0
        st.session_state.show_survey = True

questions = [
    {"text": "1. How often do you feel stressed?", "choices": {"Rarely": 0, "Sometimes": 1, "Often": 1, "Always": 2}, "feedback": "Consider stress management strategies like exercise or mindfulness."},
    {"text": "2. Do you have strong family support?", "choices": {"Yes": 0, "Some": 1, "Very little": 1, "None": 2}, "feedback": "Lack of family support can increase risk. Seek out mentors or trusted adults."},
    {"text": "3. Do your friends use drugs?", "choices": {"No": 0, "A few": 1, "Many": 1, "Most": 2}, "feedback": "Peer influence matters. Try to spend more time with friends who stay drug-free."},
    {"text": "4. How curious are you to try new substances?", "choices": {"Not at all": 0, "A little": 1, "Curious": 1, "Very curious": 2}, "feedback": "Curiosity can lead to experimentation. Stay informed and cautious."},
    {"text": "5. Do you drink alcohol regularly?", "choices": {"Never": 0, "Occasionally": 1, "Weekly": 1, "Daily": 2}, "feedback": "Regular alcohol use increases health risks. Consider cutting back."},
    {"text": "6. Do you feel lonely often?", "choices": {"Never": 0, "Sometimes": 1, "Often": 1, "Always": 2}, "feedback": "Loneliness can increase vulnerability. Try social activities or talking to someone you trust."},
    {"text": "7. Do you have anxiety or depression?", "choices": {"No": 0, "Mild": 1, "Moderate": 1, "Severe": 2}, "feedback": "Mental health is important. Don't hesitate to talk to a counselor or professional."},
    {"text": "8. Do you find it easy to talk about problems?", "choices": {"Yes": 0, "Sometimes": 1, "Rarely": 1, "Never": 2}, "feedback": "Talking about problems helps. Build communication skills and support systems."},
    {"text": "9. Have you ever tried vaping?", "choices": {"Never": 0, "Once": 1, "Sometimes": 1, "Often": 2}, "feedback": "Vaping can be addictive. Try to avoid making it a habit."},
    {"text": "10. Do you often feel bored or unmotivated?", "choices": {"No": 0, "Sometimes": 1, "Often": 1, "Always": 2}, "feedback": "Boredom can lead to risk-taking. Explore hobbies or creative outlets."},
    {"text": "11. How often are you unsupervised by adults?", "choices": {"Rarely": 0, "Sometimes": 1, "Often": 1, "Always": 2}, "feedback": "Time alone is fine, but frequent lack of supervision can increase risk."},
    {"text": "12. Do you skip school or lie to teachers/parents?", "choices": {"Never": 0, "Occasionally": 1, "Often": 1, "Always": 2}, "feedback": "Skipping school or lying can be signs of deeper issues. Reflect on your motivations."},
    {"text": "13. Do you struggle with low self-esteem?", "choices": {"No": 0, "Sometimes": 1, "Often": 1, "Always": 2}, "feedback": "Working on self-esteem can help protect against risky behavior."},
    {"text": "14. Do you find school stressful?", "choices": {"No": 0, "A bit": 1, "Quite": 1, "Extremely": 2}, "feedback": "School stress is common—learn techniques to cope like time management or breathing exercises."},
    {"text": "15. Have you been exposed to drug use in your family?", "choices": {"No": 0, "Once": 1, "Sometimes": 1, "Often": 2}, "feedback": "Family exposure can increase risk. Awareness is the first step toward prevention."},
    {"text": "16. Do you use drugs to cope?", "choices": {"Never": 0, "Rarely": 1, "Sometimes": 1, "Often": 2}, "feedback": "Using drugs to cope can lead to addiction. Seek healthy coping strategies instead."},
    {"text": "17. Do you have healthy hobbies?", "choices": {"Many": 0, "Some": 1, "Few": 1, "None": 2}, "feedback": "Hobbies build resilience. Try art, sports, or volunteering."},
    {"text": "18. How much do you value your health?", "choices": {"A lot": 0, "Some": 1, "Little": 1, "None": 2}, "feedback": "Valuing your health is key. Focus on decisions that support well-being."},
    {"text": "19. Are you easily influenced by peers?", "choices": {"No": 0, "A little": 1, "Sometimes": 1, "Always": 2}, "feedback": "Peer pressure is powerful—practice saying no and thinking independently."},
    {"text": "20. How often do you feel hopeless?", "choices": {"Never": 0, "Sometimes": 1, "Often": 1, "Always": 2}, "feedback": "Hopelessness is serious. Talk to someone—a counselor, teacher, or trusted adult."}
]

# Survey display
if st.session_state.show_survey:
    st.title("Drug Vulnerability Survey")
    st.session_state.answers = []
    st.session_state.score = 0  # Reset score

    for i, q in enumerate(questions):
        answer = st.radio(q["text"], list(q["choices"].keys()), key=f"q{i}")
        score = q["choices"][answer]
        st.session_state.score += score
        st.session_state.answers.append(score)

    if st.button("Submit"):
        st.session_state.submitted = True
        st.session_state.show_survey = False

# Results + Feedback
if st.session_state.submitted:
    user_score = st.session_state.score
    if 0 <= user_score <= 7:
        level = "Low Vulnerability"
    elif 8 <= user_score <= 15:
        level = "Medium Vulnerability"
    elif 16 <= user_score <= 70:
        level = "High Vulnerability"
    else:
        level = "Severe Vulnerability"

    st.title(f"Your Risk Level: **{level}**")
    st.progress(min(user_score / 75, 1.0))

    feedback_list = []
    for i, answer_score in enumerate(st.session_state.answers):
        if answer_score >= 1:
            feedback_list.append(f"- {questions[i]['feedback']}")

    if feedback_list:
        st.subheader("Personal Feedback")
        for f in feedback_list:
            st.write(f)
    else:
        st.write("There is no personal feedback for you.")

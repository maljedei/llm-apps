
import streamlit as st
import json
from pathlib import Path

# ------- CONFIGURATION FILE LOAD --------
def load_recommendations():
    config_path = Path(__file__).parent / "models.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

recommendations = load_recommendations()

# ------- PAGE CONFIG & RTL STYLING --------
st.set_page_config(page_title="لوحة اختيار أفضل النماذج الذكية", layout="wide")
st.markdown(
    """
    <style>
    body, .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
        font-size: 1.1rem;
        background: #fafbfc;
        color: #222 !important;
    }
    label[data-testid="stWidgetLabel"] {
        text-align: right !important;
        display: block;
        font-weight: bold;
        color: #222 !important;
    }
    div[data-baseweb="select"] {
        direction: rtl;
        text-align: right;
        width: 320px !important;
        margin-left: auto !important;
        margin-right: 0 !important;
        color: #222 !important;
    }
    .css-1j6rxnh.e1tzin5v1, .css-1wa3eu0-placeholder {
        direction: rtl;
        text-align: right;
        color: #222 !important;
    }
    .stMarkdown, .stExpanderContent {
        color: #222 !important;
    }
    @media (max-width: 600px) {
        .stApp, body {
            font-size: 1.4rem !important;
        }
        .stSelectbox {
            width: 100vw !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------- MAIN UI --------
st.title("🧠 لوحة اختيار أفضل النماذج الذكية 🧠")
st.markdown("اختر نوع المهمة، وسأرشح لك أفضل نموذج ذكاء اصطناعي لأدائها.")

task_options = [r["task"] for r in recommendations]
task = st.selectbox("🎯 اختر المهمة", task_options)

# ------- RECOMMENDATION SECTION --------
selected = next((r for r in recommendations if r["task"] == task), None)

if selected:
    st.subheader("🔍 النموذج المقترح:")
    st.markdown(f"**{selected['model']}**")

    st.subheader("📌 سبب الترشيح:")
    st.markdown(selected["reason"])

    if "details" in selected:
        with st.expander("📖 تفاصيل إضافية عن النموذج"):
            st.markdown(selected["details"])
    if "docs" in selected:
        st.markdown(f"[مزيد من المعلومات]({selected['docs']})", unsafe_allow_html=True)
else:
    st.warning("لم يتم العثور على ترشيح لهذه المهمة. يرجى المحاولة بمهمة أخرى أو التواصل مع الدعم.")

# ------- FOOTER --------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray; font-size:0.9rem'>"
    "تطوير: فريق الذكاء الاصطناعي | آخر تحديث 2025"
    "</div>",
    unsafe_allow_html=True
)

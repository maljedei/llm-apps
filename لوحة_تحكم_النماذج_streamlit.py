import streamlit as st

st.set_page_config(page_title="لوحة تحكم النماذج", layout="wide")
st.markdown(
    """
    <style>
    /* ضبط كامل الصفحة على RTL */
    body, .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
    }

    /* ضبط عنوان selectbox */
    label[data-testid="stWidgetLabel"] {
        text-align: right !important;
        display: block;
    }

    /* ضبط محتوى selectbox */
    div[data-baseweb="select"] {
        direction: rtl;
        text-align: right;
        width: 300px !important;
        margin-left: auto !important;
        margin-right: 0 !important;
    }

    /* عناصر الاختيار */
    .css-1j6rxnh.e1tzin5v1, .css-1wa3eu0-placeholder {
        direction: rtl;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 لوحة تحكم النماذج الذكية - المساعد الشخصي")
st.markdown("اختر نوع المهمة، وسأرشح لك أفضل نموذج ذكاء اصطناعي لأدائها.")

task = st.selectbox(
    "🎯 اختر المهمة",
    [
        "تحليل كود برمجي",
        "تلخيص ملف PDF طويل",
        "بحث موثق مع مصادر",
        "دردشة دعم نفسي",
        "إنتاج محتوى سريع (تويتر/سوشيال)",
        "تحليل تقارير Excel",
        "تلخيص فيديو / صوت",
        "شرح دروس أو تعلم ذاتي",
        "تلخيصات خفيفة بالعربي"
    ]
)

recommendations = {
    "تحليل كود برمجي": ("DeepSeek-V2 / GPT-4o", "منطقي، دقيق، متمكن في فهم الكود"),
    "تلخيص ملف PDF طويل": ("Claude 3 Sonnet / Command R+", "يستوعب 200K+ توكن ويعطي تلخيص منطقي"),
    "بحث موثق مع مصادر": ("Perplexity AI", "بحث سريع ودقيق مع مصادر فورية"),
    "دردشة دعم نفسي": ("Claude 3 Opus / Pi", "أسلوب إنساني وداعم نفسيًا"),
    "إنتاج محتوى سريع (تويتر/سوشيال)": ("Grok / Claude Haiku", "ساخر وخفيف وسريع التجاوب"),
    "تحليل تقارير Excel": ("M365 Copilot / GPT-4o", "مدمج مع أدوات مايكروسوفت"),
    "تلخيص فيديو / صوت": ("Gemini 1.5 / GPT-4o", "يفهم وسائط متعددة ويعالجها"),
    "شرح دروس أو تعلم ذاتي": ("Gemini 1.5 / Phi-2", "يوضّح المفاهيم ويعلّم ببساطة"),
    "تلخيصات خفيفة بالعربي": ("Manus / ChatGPT 3.5", "تفاعلي وسريع بالعربية")
}

model, reason = recommendations.get(task, ("-", "-"))

st.subheader("🔍 النموذج المقترح:")
st.markdown(f"**{model}**")

st.subheader("📌 سبب الترشيح:")
st.markdown(reason)

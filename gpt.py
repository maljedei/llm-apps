import streamlit as st

# Create a basic Streamlit app layout as a string
app_code = """
import streamlit as st

st.set_page_config(page_title="لوحة تحكم النماذج", layout="wide")
st.markdown(
    """
<style >
body, .stApp {
    direction: rtl
    text-align: right
    font-family: 'Arial', sans-serif
}

    .css-18ni7ap.e8zbici2 { / * عنوان المهمة * /
                           text-align: right !important
                           }

    .css-1cpxqw2.edgvbvh3 { / * الصندوق * /
                           text-align: right !important
                           }

    .stSelectbox > div > div {
        direction: rtl !important
        text-align: right !important
    }

    </style >
    """,
    unsafe_allow_html=True
)


st.title("🧠 لوحة تحكم النماذج الذكية - المساعد الشخصي ")
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
"""

# Save the Streamlit app to a Python file
app_path = "لوحة_تحكم_النماذج_streamlit.py"
with open(app_path, "w", encoding="utf-8") as f:
    f.write(app_code)

app_path

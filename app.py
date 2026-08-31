import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(
    page_title="Smart Study Assistant | مساعد المنهج الذكي",
    page_icon="🎓",
    layout="centered"
)

# Language Selection in Sidebar
st.sidebar.title("🌍 Language / اللغة")
lang = st.sidebar.selectbox("Choose Language / اختر اللغة", ["English", "العربية"])

# Dictionary for multi-language text
if lang == "English":
    title = "🎓 Smart Study Assistant"
    subtitle = "Empowering your study sessions with Google Gemini AI"
    about_title = "About the Developer"
    about_text = "👋 Welcome!\n\nI am **Saba**, a passionate student building AI solutions to help learners summarize complex study materials and ace their exams effortlessly."
    api_label = "Enter your Google Gemini API Key:"
    text_label = "Paste your lesson or article text here:"
    radio_label = "Choose what you want the AI to do:"
    options = ["Summarize Text", "Generate Exam Questions"]
    btn_text = "Run AI Assistant"
    spinner_text = "Processing with AI... Please wait."
    success_text = "✨ Done Successfully!"
    result_title = "Result:"
    warn_api = "⚠️ Please enter your Gemini API Key first."
    warn_text = "⚠️ Please paste some study text to process."
    prompt_summary = "Please provide a clean, structured, and professional summary of the following text (in English):"
    prompt_exam = "Please generate 3 to 5 smart exam practice questions with answers based on the following text (in English):"
else:
    title = "🎓 مساعد المنهج الذكي"
    subtitle = "مدعوم بواسطة ذكاء جوجل الاصطناعي (Gemini) لتسهيل دراستك"
    about_title = "عن المطور"
    about_text = "👋 أهلاً بك!\n\nأنا **سبأ**، طالب شغوف ببناء حلول الذكاء الاصطناعي لمساعدة الطلاب على تلخيص المواد الدراسية المعقدة واجتياز الامتحانات بكل سهولة."
    api_label = "أدخل مفتاح واجهة برمجة تطبيقات جوجل (Gemini API Key):"
    text_label = "الصق نص الدرس أو المقال هنا:"
    radio_label = "اختر ما ترغب أن يفعله الذكاء الاصطناعي:"
    options = ["تلخيص النص", "توليد أسئلة امتحانية"]
    btn_text = "تشغيل المساعد الذكي"
    spinner_text = "جاري المعالجة بواسطة الذكاء الاصطناعي... انتظر قليلاً."
    success_text = "✨ تم بنجاح!"
    result_title = "النتيجة:"
    warn_api = "⚠️ يرجى إدخال مفتاح الـ API الخاص بـ Gemini أولاً."
    warn_text = "⚠️ يرجى لصق نص دراسي لمعالجته."
    prompt_summary = "يرجى تقديم تلخيص نظيف ومنظم واحترافي للنص التالي (باللغة العربية):"
    prompt_exam = "يرجى توليد 3 إلى 5 أسئلة امتحانية ذكية مع أجوبتها بناءً على النص التالي (باللغة العربية):"

# Sidebar Branding
st.sidebar.title(about_title)
st.sidebar.info(about_text)

# Main Title and Description
st.title(title)
st.markdown(f"### {subtitle}")

# API Key & Inputs
api_key = st.text_input(api_label, type="password")
study_text = st.text_area(text_label, height=200)
task_option = st.radio(radio_label, options)

# Process Button
if st.button(btn_text):
    if not api_key:
        st.warning(warn_api)
    elif not study_text:
        st.warning(warn_text)
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            with st.spinner(spinner_text):
                if task_option in ["Summarize Text", "تلخيص النص"]:
                    prompt = f"{prompt_summary}\n\n{study_text}"
                else:
                    prompt = f"{prompt_exam}\n\n{study_text}"
                
                response = model.generate_content(prompt)
                
                st.success(success_text)
                st.markdown(f"### {result_title}")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"Error: {e}")
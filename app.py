import streamlit as st

st.title("🚀 AI Career Roadmap Generator")

skills = st.text_input("Enter your skills")
goal = st.text_input("Enter your career goal")

if st.button("Generate Roadmap"):

    st.subheader("📊 Your Personalized Career Roadmap")

    g = goal.lower()

    # 📊 DATA SCIENCE
    if "data" in g or "analyst" in g:

        st.markdown("## 📊 Data Science Roadmap")

        st.markdown("### 📌 What is this field?")
        st.write("Data Science helps you analyze data and find useful insights for business decisions.")

        st.markdown("### 📚 Skills You Need")
        st.write("• Python – for data handling")
        st.write("• SQL – for databases")
        st.write("• Statistics – for analysis")
        st.write("• Power BI / Tableau – for visualization")

        st.markdown("### 🛤️ Step-by-Step Learning Path")
        st.write("1. Learn Python basics")
        st.write("2. Learn SQL for data handling")
        st.write("3. Learn Statistics concepts")
        st.write("4. Practice data visualization tools")
        st.write("5. Build real-world projects")

    # 🌐 WEB DEVELOPMENT
    elif "web" in g:

        st.markdown("## 🌐 Web Development Roadmap")

        st.markdown("### 📌 What is this field?")
        st.write("Web development is about building websites and web applications.")

        st.markdown("### 📚 Skills You Need")
        st.write("• HTML – structure of website")
        st.write("• CSS – design and styling")
        st.write("• JavaScript – functionality")
        st.write("• React – advanced frontend development")

        st.markdown("### 🛤️ Step-by-Step Learning Path")
        st.write("1. Learn HTML basics")
        st.write("2. Learn CSS styling")
        st.write("3. Learn JavaScript")
        st.write("4. Learn React framework")
        st.write("5. Build real projects")

    # 📱 APP DEVELOPMENT
    elif "app" in g or "android" in g:

        st.markdown("## 📱 App Development Roadmap")

        st.markdown("### 📌 What is this field?")
        st.write("App development means creating mobile applications for Android or iOS devices.")

        st.markdown("### 📚 Skills You Need")
        st.write("• Kotlin or Dart – programming language")
        st.write("• Flutter – UI framework")
        st.write("• Firebase – backend and database")

        st.markdown("### 🛤️ Step-by-Step Learning Path")
        st.write("1. Learn programming basics")
        st.write("2. Learn Flutter UI development")
        st.write("3. Learn state management")
        st.write("4. Learn Firebase integration")
        st.write("5. Build apps and publish")

    # 🤖 DEFAULT
    else:

        st.markdown("## 📌 General Career Roadmap")

        st.markdown("### 📌 What is this?")
        st.write("This is a general roadmap for any career field.")

        st.markdown("### 🛤️ Steps")
        st.write("1. Learn basics")
        st.write("2. Choose your field")
        st.write("3. Practice skills")
        st.write("4. Build projects")
        st.write("5. Create portfolio")
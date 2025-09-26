# DreamWeaver AI – Sleep & Wellness Chatbot

Take a look at Live Website : https://dreamweaver-ai-chatbot.streamlit.app/

## 📌 Project Overview
**DreamWeaver AI** is an innovative AI/ML project that provides personalized recommendations and tools for sleep, wellness, and lifestyle improvement. The project features:

- A **Tkinter chatbot** that responds to user queries using a dataset of 100 unique AI tools.
- A **dataset (`dreamweaver_ai_100.csv`)** containing detailed descriptions, inputs, outputs, and categories for each AI tool.
- Optional **web pages** for each AI tool, providing a clear and interactive project presentation.

---

## 🗂 Project Structure

```
DreamWeaverAI_Project/
│
├── chatbot/
│ ├── chatbot.py # Tkinter chatbot code
│ ├── requirements.txt # Python dependencies
│
├── dataset/
│ └── dreamweaver_ai_100.csv # 100-row dataset
|
├── README.md # Project overview
├── LICENSE # Open source license
```

---

## 🛠 Features

1. **Chatbot Interface**
   - Users can interact with the chatbot using natural language.
   - The chatbot searches the dataset and returns relevant AI tools.
   - Example queries:
     - "I want a bedtime story"
     - "Make dream-inspired recipes"
     - "Generate dream art from my sleep stats"

2. **100-Row AI Tool Dataset**
   - Contains unique AI tools for sleep, wellness, health, lifestyle, productivity, and entertainment.
   - Fields include:
     - `id`, `name`, `category`, `description`, `input_data`, `output_data`, `open_source`, `api`, `website`

3. **Web Pages for Each Tool**
   - Optional static or dynamic HTML pages for each AI tool.
   - Includes description, inputs/outputs, screenshots, and demo links.
   - Improves presentation and clarity for project showcase.

---

## 💻 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/DreamWeaverAI_Project.git
cd DreamWeaverAI_Project/chatbot
```

2. Create a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the chatbot:

```bash
python chatbot.py
```

## ▶️ Example Execution

**User:** "I want a bedtime story"

**Bot:** ✨ DreamWeaver Core (Sleep & Wellness)
Generates bedtime stories based on sleep duration and stress level.
🔗 Website: https://example.com/dreamweaver/tool1

**User:** "Create dream-inspired recipes"

**Bot:** ✨ DreamChef AI (Lifestyle)
Suggests dream-inspired recipes for healthy nighttime snacks.
🔗 Website: https://example.com/dreamweaver/tool11

---

## 📊 Dataset

The dataset file `dreamweaver_ai_100.csv` contains 100 rows of AI tools.

You can expand, update, or use it to train ML models for:

- Tool recommendation
- Keyword matching
- Chatbot response optimization

---

## 📄 License

This project is licensed under the MIT License.

See LICENSE file for more details.

---

## 🌟 Future Improvements

- Add dynamic web pages using Flask or Django.
- Implement AI/ML NLP matching to improve chatbot responses.
- Include interactive demos for each AI tool.
- Add user accounts to save tool preferences and past interactions.


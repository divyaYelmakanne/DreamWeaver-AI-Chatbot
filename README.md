# 🌙 DreamWeaver AI – Sleep & Wellness Chatbot Ecosystem
**Live Demo:** [https://dreamweaver-ai-chatbot.streamlit.app/](https://dreamweaver-ai-chatbot.streamlit.app/)                                                                
**Main Repository:** [https://github.com/divyaYelmakanne/DreamWeaver-AI-Chatbot](https://github.com/divyaYelmakanne/DreamWeaver-AI-Chatbot)

## 🧠 Project Overview
DreamWeaver AI is an innovative AI/ML + Web Development project designed to enhance sleep, creativity, and wellness. It combines a Streamlit-based AI chatbot, a custom-built dataset of 100 dream tools, and 10 interactive web experiences that visualize and extend the chatbot’s recommendations.

This ecosystem demonstrates:
- Personalized AI-assisted sleep and mood wellness support
- Creative dream exploration via web-based AI applications
- Integration of ML datasets, chatbot logic, and full-stack web development

## 🚀 Project Highlights

### 💬 AI Chatbot (Main Hub)
- Built using Streamlit + Python (Tkinter backend).
- Responds intelligently to user prompts like:
  - “Tell me a bedtime story.”
  - “Turn my sleep stats into dream art.”
  - “Suggest calm sounds for my mood.”
- Fetches data from a 100-row AI tools dataset (CSV-based).
- Each chatbot response links to a unique interactive web project.

### 📊 Dataset (dreamweaver_ai_100.csv)
- 100 entries, representing 10 unique user statements, each expanded into 10 variations.
- Each entry contains:
  | Field | Description |
  |--------|-------------|
  | id | Unique tool ID |
  | name | Tool name |
  | category | Sleep, Wellness, Art, Mood, or Story |
  | description | What the tool does |
  | input_data | Example inputs |
  | output_data | Example outputs |
  | website | Live project/demo link |
  | open_source/api | Metadata for developer access |

This dataset forms the AI brain for chatbot responses.

### 🕸 Linked Web Projects (10 Dream Experiences)
Each user statement in the dataset is linked to a dedicated interactive web application, showcasing both web development and AI creativity.

| # | Project | GitHub Repo | Live Website |
|---|----------|--------------|---------------|
| 1️⃣ | DreamScope – Predict Your Vivid Dreams | [Repo](https://github.com/DIVYAYELMAKANNE2k5/DreamScope---Predict-Your-Vivid-Dreams) | [Live](https://dream-scope-predict-your-vivid-drea.vercel.app/) |
| 2️⃣ | Mood Sound Dream 05 | [Repo](https://github.com/DIVYAYELMAKANNE2k5/Mood-Sound-Dream-05) | [Live](https://mood-sound-dream-05.vercel.app/) |
| 3️⃣ | DreamWeaver – Sleep-Aware Bedtime Stories | [Repo](https://github.com/DIVYAYELMAKANNE2k5/DreamWeaver---Sleep-Aware-Bedtime-Stories) | [Live](https://dream-weaver-sleep-aware-bedtime-st.vercel.app/) |
| 4️⃣ | Dream Canvas Glow | [Repo](https://github.com/DIVYAYELMAKANNE2k5/Dream-Canvas-Glow) | [Live](https://dream-canvas-glow.vercel.app/) |
| 5️⃣ | Peaceful Dreams – Your Evening Sanctuary | [Repo](https://github.com/DIVYAYELMAKANNE2k5/Peaceful-Dreams---Your-Evening-Sanctuary) | [Live](https://peaceful-dreams-your-evening-sanctu.vercel.app/) |
| 6️⃣ | FictiDream Generator | [Repo](https://github.com/DIVYAYELMAKANNE2k5/Ficti-Dream-Generator) | [Live](https://ficti-dream-generator.vercel.app/) |
| 7️⃣ | MindMuse AI Companion 05 | [Repo](https://github.com/DIVYAYELMAKANNE2k5/MindMuse-AI-Companion-05) | [Live](https://mind-muse-ai-companion-05.vercel.app/) |
| 8️⃣ | DreamFusion – AI Dream Story Generator | [Repo](https://github.com/DIVYAYELMAKANNE2k5/DreamFusion---AI-Dream-Story-Generator) | [Live](https://dream-fusion-ai-dream-story-generat.vercel.app/) |
| 9️⃣ | Sleep-to-Art Generator | [Repo](https://github.com/DIVYAYELMAKANNE2k5/Sleep-to-Art-Generator) | [Live](https://sleep-to-art-generator-rek2.vercel.app/) |
| 🔟 | DreamEase – Calm Chat Companion | [Repo](https://github.com/DIVYAYELMAKANNE2k5/DreamEase) | [Live](https://dream-ease.vercel.app/) |

## 🗂 Project Structure
```
DreamWeaver-AI-Chatbot/
│
├── chatbot/
│   ├── chatbot.py                 # Streamlit / Tkinter chatbot logic
│   ├── requirements.txt           # Dependencies
│
├── dataset/
│   └── dreamweaver_ai_100.csv     # 100-row dataset of dream tools
│
├── assets/
│   └── images/, icons/, etc.      # Optional visuals for web integration
│
├── README.md                      # Project documentation
├── LICENSE                        # MIT license
```

## 🛠️ Features Summary
### 🌙 Intelligent Chatbot
- Personalized responses for sleep, creativity, and relaxation.
- Context-aware suggestions linked to the 10 dream web projects.
- Uses NLP-style keyword matching from the dataset.

### 🧾 Dream Dataset Integration
- 100 labeled tools categorized into Art, Mood, Sleep, Health, and Story.
- Supports search, recommendation, and visualization.

### 🌐 Web Integration
- Each chatbot recommendation links to a live, interactive project.
- Combines Streamlit (ML frontend) + Next.js/Vercel (Web experiences).

## 💻 Installation (for Chatbot)
```bash
git clone https://github.com/divyaYelmakanne/DreamWeaver-AI-Chatbot.git
cd DreamWeaver-AI-Chatbot/chatbot
python -m venv venv
source venv/bin/activate     # (Linux/Mac)
venv\Scripts\activate      # (Windows)
pip install -r requirements.txt
streamlit run chatbot.py
```

## ▶️ Example Interaction
**User:** "I want a bedtime story"
**Bot:** ✨ DreamWeaver – Sleep-Aware Bedtime Stories  
Generates bedtime stories based on your sleep data and stress level.  
🔗 [Try it Live](https://dream-weaver-sleep-aware-bedtime-st.vercel.app/)

**User:** "Make dream-inspired art from my sleep stats"  
**Bot:** 🎨 Sleep-to-Art Generator  
Transforms sleep duration and patterns into colorful dream-style visuals.  
🔗 [Try it Live](https://sleep-to-art-generator-rek2.vercel.app/)

## 🧩 Use Cases
- Sleep Wellness Assistance
- Dream-Inspired Art Generation
- Mood & Sound Therapy
- Bedtime Story Creation
- Dream Prediction & Imagination Exploration

## 🧱 Tech Stack
| Layer | Tools & Technologies |
|-------|----------------------|
| Frontend | Streamlit, HTML, CSS, JavaScript, React (Vercel projects) |
| Backend | Python, Pandas, CSV dataset |
| ML/AI | Keyword-based NLP matching (expandable to transformers) |
| Hosting | Streamlit Cloud, Vercel |
| Version Control | Git + GitHub |

## 🌟 Future Improvements
- Integrate NLP transformer (e.g., BERT) for semantic matching.  
- Add Firebase/DB for user sessions & favorites.  
- Combine visualizations from all dream web apps into a single dashboard.  
- Add voice-enabled bedtime companion mode.  
- Introduce light/dark mode across all web apps.

## 📄 License
This project is licensed under the MIT License.

## 👩‍💻 Author
**Divya Yelmakanne**  
AI & Web Developer | Passionate about DreamTech and Wellness AI  
🌐 GitHub: [@divyaYelmakanne](https://github.com/divyaYelmakanne)  
🔗 Project Network: [DreamWeaver Ecosystem on Vercel + Streamlit](https://dreamweaver-ai-chatbot.streamlit.app/)

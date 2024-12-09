# AI-Powered LinkedIn Post Generator App | Step-by-Step Guide 2025 🚀

[![LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-blue)](https://www.linkedin.com/in/seotanvirbd/)
[![Portfolio](https://img.shields.io/badge/Visit-Portfolio-green)](https://seotanvirbd.com/)
[![YouTube](https://img.shields.io/badge/Subscribe-YouTube-red)](https://www.youtube.com/@tanvirbinali2200)

## 🎯 Project Overview

An innovative AI-powered application that generates human-like LinkedIn posts using LLAMA 3.2 from Groq API. The app leverages machine learning and natural language processing to create engaging content based on successful LinkedIn posts from top content creators.

![LinkedIn Post Generator Interface](https://github.com/seotanvirbd/Linkedin-Post-Generator/blob/main/linkedin_post_generator_customtkinter.png)

## 🌟 Key Features

- **Customizable Post Generation**: Control topic, length, and language preferences
- **AI-Powered Content**: Utilizes LLAMA 3.2 model for human-like text generation
- **Bilingual Support**: Generate posts in English and Hinglish
- **User-Friendly Interface**: Built with CustomTkinter for a modern look
- **Data-Driven Approach**: Trained on real LinkedIn posts from successful content creators

## 🛠️ Technical Stack

- **AI/ML**: LLAMA 3.2 (Groq API)
- **Frontend**: CustomTkinter (Python GUI Framework)
- **Language Processing**: LangChain
- **Data Processing**: Python, JSON
- **Environment Management**: Python dotenv

## 📋 Installation & Setup

1. Clone the repository:
```bash
git clone [repository-url]
cd linkedin-post-generator
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create .env file and add your Groq API key
GROQ_API_KEY=your_api_key_here
```

4. Run the application:
```bash
python app.py
```

## 🎮 How to Use

1. **Select Topic**: Choose from various predefined topics
2. **Set Length**: Choose between Short (1-5 lines), Medium (6-10 lines), or Long (11-15 lines)
3. **Choose Language**: Select English or Hinglish
4. **Generate**: Click "Generate Post" to create your LinkedIn content
5. **Copy & Use**: Copy the generated post and share it on LinkedIn

## 🔍 Project Structure

```
linkedin-post-generator/
├── app.py                 # Main application file
├── llm_helper.py         # LLAMA model integration
├── post_generator.py     # Post generation logic
├── few_shot.py          # Example post management
├── data/
│   ├── raw_posts.json    # Training data
│   └── processed_posts.json # Processed posts
└── requirements.txt      # Project dependencies
```

## 🤖 How It Works

1. **Data Collection**: Gathered posts from successful LinkedIn content creators
2. **Data Processing**: Converted posts to structured JSON format
3. **AI Training**: Fine-tuned LLAMA 3.2 model on the collected data
4. **Post Generation**: Uses few-shot learning approach with custom prompts
5. **User Interface**: CustomTkinter for modern, user-friendly experience

## 🔮 Future Enhancements

- [ ] Add support for more languages
- [ ] Implement post scheduling features
- [ ] Add sentiment analysis for generated content
- [ ] Integrate with LinkedIn API for direct posting
- [ ] Add more customization options for post structure

## 👨‍💻 About the Developer

Hi! I'm Tanvir, a Python web scraper, data analyst, and AI enthusiast. I specialize in creating innovative solutions using AI and data analysis. Check out my other projects and connect with me:

- 🌐 Portfolio: [seotanvirbd.com](https://seotanvirbd.com/)
- 💼 LinkedIn: [linkedin.com/in/seotanvirbd](https://www.linkedin.com/in/seotanvirbd/)
- 📺 YouTube: [@tanvirbinali2200](https://www.youtube.com/@tanvirbinali2200)
- 📧 Email: tanvirafra1@gmail.com
- 💬 WhatsApp: [+8801687373830](https://api.whatsapp.com/send?phone=8801687373830)
- 📱 Facebook: [seotanvirbd](https://www.facebook.com/seotanvirbd)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to Groq for providing the LLAMA 3.2 API
- CustomTkinter community for the amazing GUI framework
- LinkedIn content creators whose posts helped train the model

---

If you find this project useful, please consider giving it a star ⭐ and sharing it with others!

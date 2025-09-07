# 🍵 TeaBuddy — Your Local Matcha & Healthy Drinks Assistant

**TeaBuddy** is a lightweight, fully offline AI chatbot built with **Streamlit** and powered by **Ollama** + **Gemma 1B**. It's your personal tea expert. This will help you to explore matcha, compare green teas, and answer any question about healthy drinks.

Designed for **fast local interaction**, TeaBuddy runs entirely on your machine. No OpenAI keys. No cloud APIs. Just our tea talk.

---

## Current Features

- Natural tea chat interface (matcha, green tea or any healthy drinks)
- Runs locally using [Ollama](https://ollama.com/) (without internet)
- Smart, themed replies + random emoji reactions
- Chat history + export to `.txt`
- Auto-clearing input after each question
- Lightweight UI with clean layout (used Streamlit)
- Tuned system prompt to stay helpful but flexible in diffrent version (not just matcha!)
- Works on any machine with Python + Ollama (mine is tested with Mac)

---

## Demo

![TeaBuddy Demo](demo.gif)

> You can also [watch this 15s demo](#) or check `/demo.gif` in this repo.

---

## Project Structure

```
TeaBuddy/
├── app.py                # app file for Streamlit
├── requirements.txt      # Python dependencies
├── README.md
└── data/
     └── tea_knowledge_base.md   # (reference contents for future versions)          
```

---

## Run TeaBuddy Locally

> Requires Python 3.10+ and [Ollama](https://ollama.com/) installed with a local model (e.g. `gemma:1b`).

### 1. Clone the repo

```bash
git clone https://github.com/saifar-tug/TeaBuddy.git
cd TeaBuddy
```

### 2. Set up your environment

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3. Pull a model with Ollama

```bash
ollama pull gemma:1b
```

### 4. Run TeaBuddy

```bash
streamlit run app.py
```

Visit: [http://localhost:8501](http://localhost:8501)

---

## Save Chat History

Click **"Save chat to file"** to export your conversation as a timestamped `.txt` file.

---

## Built With

- [Streamlit](https://streamlit.io/) — Python Web App Framework
- [Ollama](https://ollama.com/) — Local LLM AI Assistant
- `gemma:1b` — Lightweight local model (good balance of speed + size)
- by [@saifar-tug](https://github.com/saifar-tug)

---

## My Note

> As a tea lover and AI enthusiast, I wanted a **minimal, local-first AI assistant** that doesn’t need a cloud API key to chat. I like the way of learning and experimenting with local LLMs, Streamlit, and quick prototyping.

---

## For Reviewers

- built for portfolio
- fully runnable locally (offline!)
- see the demo and code
- reach out if you would like me to walk you through the project live

---

## Future Ideas

- Integrate more models (like LLaMA 3 or Mistral)
- Use embeddings + vector search for tea docs
- Test mode (funn quizzes on tea knowledge)
- Responsive layout for mobile use

---

## License

> This is one of my solo projects, fell free to use or adapt.

---

> Got a tea question for TeaBuddy or LLM idea? Feel free to collaborate via Issues or Pull Requests!
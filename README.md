# 🎥 YouTube Video Summarizer Agent

An AI-powered multi-agent application that transforms long YouTube videos into concise, structured summaries using autonomous agent collaboration.

This project was built with the idea that valuable information should be easier to consume. Instead of manually watching hours of content, users can provide a YouTube URL and receive organized insights generated through a coordinated AI workflow.

Unlike a traditional summarizer, this system separates **information extraction** from **reasoning and synthesis**, creating a cleaner and more scalable architecture.

---

## 🌱 Project Context

This project was built as one of my early hands-on explorations into AI Agents, LangChain, and LLM-powered automation.

The goal was not to create a production-scale system, but to understand how multi-agent workflows, transcript extraction, and AI-driven summarization work together in a real project environment.

This project reflects my learning journey in Generative AI and serves as a foundation for building more advanced AI applications in the future.

---

## 🚀 Project Vision

Modern content consumption is overloaded.

This project aims to reduce information fatigue by creating an intelligent pipeline capable of:

* Extracting transcript data from YouTube videos
* Processing large text efficiently
* Understanding semantic context
* Producing concise, readable summaries
* Supporting future expansion into web applications and APIs

The goal was not just summarization—but building a reusable AI workflow architecture.

---



## 🏗️ System Architecture

```text
User Input (YouTube URL)
          │
          ▼
┌──────────────────────────┐
│ Transcript Extractor     │
│ (CrewAI Agent + Tool)    │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ Content Synthesizer      │
│ (Gemini + CrewAI Agent)  │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ Structured Summary       │
│ (Title + Key Insights)   │
└──────────────────────────┘
```
---

# 🏗 Architecture Overview

The system uses a **multi-agent orchestration model** where each agent owns a specific responsibility.

### Agent 1 — Senior YouTube Data Extractor

Responsible for:

* Receiving YouTube video URLs
* Calling a custom LangChain transcript extraction tool
* Cleaning and isolating transcript content
* Handling payload processing efficiently

### Agent 2 — Executive summary synthesizer

Responsible for:

* Accepting extracted transcript data
* Applying semantic understanding
* Distilling information into structured summaries
* Generating readable outputs

This separation improves maintainability, scalability, and overall response quality.

---

# ⚙ Core Technologies & Tools

## AI & Orchestration

* CrewAI (Multi-Agent Workflow Orchestration)
* Google Gemini API
* Prompt Engineering

## Frameworks & Libraries

* LangChain
* LangChain Google GenAI
* LangChain Community

## Data Extraction

* YouTube Transcript API
* Custom LangChain Tool

## Runtime & Environment

* Python 3.10+
* Virtual Environments
* Async-ready Architecture

---

# ✨ Key Features

✅ Autonomous Multi-Agent Pipeline
✅ YouTube Transcript Extraction
✅ Intelligent Content Summarization
✅ Semantic Context Processing
✅ Secure Environment Variable Management
✅ Extensible Architecture for Future Integrations
✅ Lightweight Local Execution

---


# 📂 Project Structure

```plaintext
youtube-summarizer-agent/
│
├── main.py
├── tools.py
├── pyproject.toml
├── .env
├── .gitignore
├── README.md
│
└── __pycache__/
```

---

## Step 1 — Clone Repository

```bash
git clone https://github.com/Aayu4473/youtube-summarizer-agent.git

cd youtube-summarizer-agent
```

---

## Step 3 — Install Dependencies

```bash
pip install crewai
pip install langchain-google-genai
pip install langchain-community
pip install youtube-transcript-api
```

(Or install directly from your project configuration)

```bash
pip install .
```

---

# ▶ Running the Application

Execute:

```bash
python main.py
```

---

## Execution Flow

1. Launch the application
2. Enter a valid YouTube URL
3. Transcript extraction begins
4. AI agents process content
5. Gemini generates structured summary

---

 
# 🤝 Contributing

Contributions, ideas, and improvements are welcome.

If you'd like to improve summarization quality, optimize extraction pipelines, or extend deployment capabilities, feel free to open an issue or submit a pull request.

---

# 📬 Contact

If you found this project useful or want to discuss AI workflows, feel free to connect.

GitHub → https://github.com/Aayu4473
LinkedIn → https://linkedin.com/in/aayushi-tiwari-tech

---

### Built with curiosity, AI experimentation, and the goal of making knowledge easier to consume.

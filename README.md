# Emotional Plan Supporter (EPS)

### 📘 Overview
**EPS** is an AI-powered assistant designed to assist individuals facing challenges in long-term planning. It combines emotional support with actionable strategies to offer practical solutions and motivation.

### 💡 Motivation
This project was developed during the **first year, second semester** of a Master's program in Artificial Intelligence as part of a large language model term project. Inspired by personal challenges with ADHD, I combined my interest in **Emotional Support Conversations (ESC)** with practical planning tools to address the complexities of long-term goal-setting.

### 🧩 Components
The project consists of two main components:

1. **LLMTermProjEPS**: A module focused on empathetic planning support using OpenAI GPT.
2. **BlenderBot**: A conversational chatbot module based on Facebook’s Blenderbot.

---

## 🔧 Project Structure

```
LLMTermProjEPS/
├── EPS_MVP.py          # Empathetic Support Planner script
├── requirements.txt    # Python dependencies for this module

BlenderBot/
├── Blenderbot_model.py # Blenderbot-based chatbot implementation
├── environment.yml     # Conda environment configuration
├── version_check.py    # Python version and library check script
```

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Yerin99/Emotional-Plan-Supporter.git
cd Emotional-Plan-Supporter
```

### 2. Setting up the Environment

#### For `BlenderBot`:

1. Create a Conda environment using the provided `environment.yml`:
   ```bash
   conda env create -f BlenderBot/environment.yml
   conda activate blenderbot_env
   ```

#### For `LLMTermProjEPS`:

1. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r LLMTermProjEPS/requirements.txt
   ```

---

## ▶️ How to Run

### 1. Run the Empathetic Support Planner (EPS_MVP):

```bash
python LLMTermProjEPS/EPS_MVP.py
```

### 2. Run the BlenderBot Chatbot:

```bash
python BlenderBot/Blenderbot_model.py
```

---

## 🌟 Features

- **EPS_MVP**:
  - Provides detailed, empathetic, and actionable plans based on user input.
  - Supports SMART (Specific, Measurable, Achievable, Relevant, Time-bound) framework for task planning.
- **BlenderBot**:
  - Engages in natural and interactive conversations using the Blenderbot model.
  - Leverages Huggingface Transformers library and PyTorch.
  - Note: BlenderBot may not handle long instructions well. Keep inputs concise for optimal results.

---

## ⚠️ Limitations

- **BlenderBot**:
  - While effective for empathetic conversational support, BlenderBot was found unsuitable for planning tasks due to its difficulty in understanding and processing lengthy prompts effectively.

---

## 📋 Requirements

### LLMTermProjEPS

- Python 3.8+
- See `LLMTermProjEPS/requirements.txt` for details.

### BlenderBot

- Python 3.8+
- Conda environment (`environment.yml`) includes:
  - PyTorch
  - Transformers
  - Other required dependencies

---

## 📄 Documentation

For a detailed explanation of the project, including the following:

1. Project topic and problem statement
2. Challenges and methods to address them
3. Experimental results and analysis
4. Conclusion, limitations, and future directions
5. References

Please refer to the [Final Report: Emotional Plan Supporter](https://github.com/Yerin99/Emotional-Plan-Supporter/blob/main/Final%20Report%20EPS.pdf).

The report also includes appendices with real usage examples and illustrative images, along with details on the SMART framework.

---

## 📜 License

This project is licensed under the MIT License due to the usage of Facebook’s Blenderbot, which is distributed under an MIT license. See `LICENSE` for details.

---

## 🙏 Acknowledgments

- OpenAI for GPT API
- Facebook AI for Blenderbot
- Huggingface for the Transformers library

---


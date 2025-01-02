# Speech-to-Text and Gemini Integration

This project allows you to use voice commands with **Speech Recognition** and receive AI-generated responses via **Gemini** (Google's generative AI model). The responses are then spoken back to you using the **Termux TTS API**.

## Prerequisites

Before you begin, ensure you have the following:

- **Termux** installed on your device
- **Termux API** (for text-to-speech capabilities)
- **Python 3** environment set up
- **Node.js** environment set up
- Active **Internet Connection** (for API communication)
- **Gemini API key** (for AI responses)
- **Native Sound Package** (optional, for advanced text-to-speech capabilities)

## Installation

### 1. Install Node.js Dependencies

In the **Node.js** project directory, run the following commands to install the necessary dependencies:

```bash
npm install express
npm install cors
npm install @google/generative-ai
```

### 2. Install Python Dependencies

In the Python environment, install the following dependencies using pip:

```bash
pip install requests
pip install SpeechRecognition
pip install pyaudio
```

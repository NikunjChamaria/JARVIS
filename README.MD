# Jarvis AI Assistant

Jarvis is a personal AI assistant built using Python. This project integrates various functionalities like automation, voice recognition, and AI-based decision-making. It is designed to respond to user commands and perform actions such as controlling system volume, opening and closing applications, sending WhatsApp messages, and playing music.

## Features

- **Voice Interaction**: Jarvis listens to user commands and responds based on predefined functions.
- **System Automation**: Includes functionality for opening, closing, minimizing, and maximizing applications.
- **Volume Control**: Allows adjusting system volume with commands like "volume up" and "volume down."
- **WhatsApp Integration**: Send messages on WhatsApp using voice commands.
- **Music Control**: Play music on YouTube using voice commands.
- **Screenshot Capture**: Take screenshots upon request.
- **Battery Monitoring**: Get battery percentage on demand.
- **Random Advice**: Jarvis can offer random suggestions or advice.

## Setup

Before running the project, create an `.env` file in the root directory of your project and add the following environment variables:

- `DATASET_PATH`: Path to your dataset file.
- `GOOGLE_API_KEY`: Your Google API key for making API requests.
- `GOOGLE_CSE_ID`: Your Google Custom Search Engine ID.
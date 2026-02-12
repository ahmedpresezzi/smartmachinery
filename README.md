# Smart Machinery Lab 🚀

Full-stack application for managing industrial assets, PLC configurations, and AI-powered technical assistance.

## 🌐 Live Website
The application is hosted on **Render** (Frontend + Python Backend).
Check the live demo here: **[Link your Render URL here]**

## 🛠️ Tech Stack
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphic Design), JavaScript (ES6+).
- **Backend**: Python 3.11, `aiohttp` (Asynchronous Web Server).
- **Integrations**: Discord Bot (Management Hub), OpenRouter AI (GPT-4o Mini).

## 🚀 Deployment Instructions
The project is configured for a single-click deployment on **Render**:
1. Connect this GitHub repo to Render.
2. Use Build Command: `pip install -r requirements.txt`
3. Use Start Command: `python Backend/app.py`
4. Set the Environment Variables (`DISCORD_TOKEN`, `OPENROUTER_API_KEY`, etc.) in the Render dashboard.

## 📂 Structure
- `/Backend`: Python API, Discord Bot logic, and JSON storage.
- `/Frontend`: Interactive dashboard and styling.
- `/Rockwell` & `/simens`: Configuration templates.

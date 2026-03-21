# Swadesh Choudhary - AI/ML Engineer Portfolio

Welcome to the repository for my personal portfolio website! This project showcases my work as an AI/ML Engineer specializing in Agentic AI, LLMs, and Multi-Agent Orchestration. It features a modern, responsive design with an integrated AI chatbot (SC-01) for interactive exploration of my background and projects.

## Features

- **Modern & Responsive Design**: A dark-themed, sleek UI with smooth animations and responsive layouts engineered for perfect viewing on all devices.
- **Interactive AI Chatbot (SC-01)**: An integrated AI assistant powered by Groq and Llama models. Users can interact with the chatbot to ask questions about my experience, skills, and projects.
- **Skills & Projects Showcase**: A visual representation of my AI, Data Science, and Software Engineering skills, alongside detailed project cards.
- **Serverless Ready**: Fully configured for frictionless deployment on Vercel with serverless functions.

## Tech Stack

- **Frontend**: HTML5, Vanilla CSS, Vanilla JavaScript
- **Backend (Development)**: Python HTTP Server (`server.py`)
- **Backend (Production)**: Vercel Serverless Functions (`api/chat.js`)
- **AI Integration**: Groq API (OpenAI compatible endpoint)

## Running Locally

To run this portfolio locally, including the AI chatbot proxy, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Portfolio
   ```

2. **Set up environment variables:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Start the local server:**
   The project includes a lightweight Python proxy server to handle API requests locally without exposing your API key to the browser.
   ```bash
   python server.py
   ```
   *Note: Requires Python 3 to be installed.*

4. **View the website:**
   Open your browser and navigate to `http://localhost:3000/index.html`.

## Deployment

This portfolio is configured for immediate deployment on [Vercel](https://vercel.com). The `vercel.json` maps incoming requests correctly to static assets and routes `/api/chat` to the correct serverless edge function (`api/chat.js`).

1. Push your code to a GitHub repository.
2. Import the project into Vercel.
3. Add the `GROQ_API_KEY` to your Vercel Environment Variables.
4. Deploy!

## Project Structure

```text
├── index.html       # The main portfolio webpage
├── server.py        # Python proxy server for local development
├── vercel.json      # Vercel deployment configuration
├── .env             # Environment variables (create this locally)
├── api/
│   └── chat.js      # Serverless function for the chat endpoint
└── public/          # Static assets (images, icons, etc.)
```

## Contact

Feel free to reach out via the contact information provided within the portfolio to discuss AI/ML opportunities, agentic AI systems, or potential collaborations!

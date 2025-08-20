# News Aggregator

A desktop application built using `PyQt` that fetches and displays the latest news articles from [NewsAPI.org](newsapi.org).

The app lets you browse headlines from different sources and topics such as **Top US News**, **Tesla**, **Apple**, **Wall Street Journal**

# Features

* Browse news articles based on categories/topics.
* Refresh articles to get the latest information.
* Clean `PyQt5` interface designed with `Qt designer`.
* Links to source websites for full articles.

# Requirements

* Python 3.9+
* `PyQt5`
* Requests
* A news API key ([Available here](newsapi.org))

# Setup

1. Clone the repository:
```bash
git clone https://github.com/Akshaye-Sharma/news-aggregator
cd news-aggregator
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Set your News API key as your environment variable.
```bash
export API_KEY=your_api_key_here # Mac/Linux
setx API_KEY "your_api_key_here" # Windows (PowerShell)
```
4. Run the application
```bash
python main.py
```
For Mac:
```bash
python3 main.py
```
# Project Structure
```bash
├── main.py               # Start the application
├── api_return.py
├── views/
│   └── main_window.py    # Window logic handler
├── ui/
│   └── smallerUi.ui
│   └── ui_mainwindow.py  # PyQt generated file
│   └── updated.ui
├── icons/                # Images used
│   └── speaker.png
│   └── user.png
├── .gitignore
├── .env
├── requirements.txt
└── README.md
```
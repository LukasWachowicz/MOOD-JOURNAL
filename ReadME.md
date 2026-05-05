🧠 AI Mood Journal & Sentiment Analyzer
    A smart, interactive daily journal that not only records your thoughts but also learns your vocabulary to better understand your emotions.
🚀Key Features
    Real-time Sentiment Analysis: Automatically detects if your day was positive, negative, or neutral based on your description.Active Machine Learning: If the AI encounters a word it doesn't know, it asks for your input to categorize it, building a personalized emotional database.
    Dual-Storage System:journal.txt: A human-readable history of your daily entries with timestamps and AI interpretations.data.json: A structured database of positive and negative triggers used for the AI's learning process.Data Persistence: All learned words and entries are saved automatically upon exit.
🛠️ Technical Overview
    The application is built using Python 3.x and utilizes:JSON Processing: For managing the core emotional dictionary.Natural Language Heuristics: A custom-built scoring algorithm to determine the emotional weight of entries.File I/O: Robust handling of data streams for both structured (JSON) and unstructured (TXT) data.
📂 Project Structure
    -main.py: The primary engine containing the logic for       analysis, learning, and user interaction.
    -data.json: The "brain" of the AI, storing categorized vocabulary.
    -journal.txt: The chronological log of your emotional journey.
🔧 Installation & Usage
     Clone the repository to your local machine.Ensure you have data.json in the same directory (or the system will create a default one).
    Run the script:bashpython main.py
    Type quit to safely save all data and exit the session
📈 Future Roadmap
    Integration with "Hurtowniczka": Correlating business performance with personal well-being.Statistical Dashboard: Visualizing mood trends over months using Matplotlib.Advanced NLP: Implementing more complex sentence structure analysis.
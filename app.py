from flask import Flask, request, render_template
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

# Specify the path to the vader_lexicon folder
nltk.data.path.append('D:\projectt\sentiment')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(text)['compound']
        if score > 0:
            label = 'Positive'
            color = 'green'
        elif score == 0:
            label = 'Neutral'
            color = 'gray'
        else:
            label = 'Negative'
            color = 'red'
        return render_template('index.html', label=label, color=color)
    return render_template('index.html', label='', color='white')

if __name__ == '__main__':
    app.run(debug=True)

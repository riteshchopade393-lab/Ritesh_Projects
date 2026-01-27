from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Simple In-memory Database (Resets when server restarts)
# For a minor project, this avoids the complexity of SQL files
poll_data = {
    'question': 'Who is your favorite candidate?',
    'fields': ['Candidate A', 'Candidate B', 'Candidate C', 'Candidate D'],
    'votes': {'Candidate A': 0, 'Candidate B': 0, 'Candidate C': 0, 'Candidate D': 0}
}

# HTML Template with Internal CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minor Project: Voting System</title>
    <style>
        :root { --primary: #4a90e2; --bg: #f4f7f6; --text: #333; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: var(--bg); color: var(--text); display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); width: 100%; max-width: 400px; text-align: center; }
        h1 { color: var(--primary); margin-bottom: 1rem; font-size: 24px; }
        p { margin-bottom: 2rem; color: #666; }
        .option { display: block; width: 100%; padding: 12px; margin: 10px 0; border: 2px solid #ddd; border-radius: 8px; cursor: pointer; transition: all 0.3s ease; background: none; font-size: 16px; font-weight: 500; }
        .option:hover { border-color: var(--primary); color: var(--primary); background: #f0f7ff; }
        .results { margin-top: 2rem; text-align: left; }
        .result-bar { height: 20px; background: #eee; border-radius: 10px; overflow: hidden; margin-top: 5px; margin-bottom: 15px; }
        .fill { height: 100%; background: var(--primary); transition: width 0.5s ease-in-out; }
        .btn-back { display: inline-block; margin-top: 1rem; text-decoration: none; color: var(--primary); font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        {% if page == 'vote' %}
            <h1>Cast Your Vote</h1>
            <p>{{ data.question }}</p>
            <form action="/vote" method="POST">
                {% for field in data.fields %}
                    <button type="submit" name="vote" value="{{ field }}" class="option">{{ field }}</button>
                {% endfor %}
            </form>
        {% else %}
            <h1>Live Results</h1>
            <div class="results">
                {% for candidate, count in data.votes.items() %}
                    <div style="display:flex; justify-content: space-between;">
                        <span>{{ candidate }}</span>
                        <span>{{ count }} votes</span>
                    </div>
                    <div class="result-bar">
                        <div class="fill" style="width: {{ (count / total * 100) if total > 0 else 0 }}%;"></div>
                    </div>
                {% endfor %}
            </div>
            <a href="/" class="btn-back">← Vote Again</a>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, page='vote', data=poll_data)

@app.route('/vote', methods=['POST'])
def vote():
    vote_cast = request.form.get('vote')
    if vote_cast in poll_data['votes']:
        poll_data['votes'][vote_cast] += 1
    return redirect(url_for('results'))

@app.route('/results')
def results():
    total_votes = sum(poll_data['votes'].values())
    return render_template_string(HTML_TEMPLATE, page='results', data=poll_data, total=total_votes)

if __name__ == '__main__':
    app.run(debug=True)
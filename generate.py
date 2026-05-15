import yaml
from jinja2 import Template
import datetime
import webbrowser

# Load data
with open('resume.yml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

data['year'] = datetime.datetime.now().year

html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{{ name }} - Resume</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
        body { font-family: 'Inter', Arial, sans-serif; margin: 0; padding: 40px; line-height: 1.45; color: #222; max-width: 1000px; margin: 0 auto; }
        .header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 30px; }
        .header-left h1 { margin: 0 0 5px 0; font-size: 2.3em; }
        .header-left .title { color: #0d6efd; font-weight: 500; }
        .avatar { width: 130px; height: 130px; border-radius: 50%; object-fit: cover; border: 5px solid #0d6efd; }
        .contact { margin: 15px 0 25px; font-size: 1.1em; }
        h2 { color: #0d6efd; border-bottom: 3px solid #0d6efd; padding-bottom: 8px; margin-top: 40px; }
        ul { padding-left: 22px; }
        li { margin-bottom: 9px; }
        .section { margin-bottom: 35px; }
        .project { margin-bottom: 20px; }
        .footer { text-align: center; margin-top: 70px; font-size: 0.85em; color: #666; }
        @media print { body { padding: 30px; } .no-print { display: none; } }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-left">
            <h1>{{ name }}</h1>
            <div class="title">{{ title }}</div>
            <div class="contact">
                {{ email }} • {{ phone }} • 
                <a href="https://linkedin.com/in/{{ linkedin }}">LinkedIn</a> • 
                <a href="https://github.com/{{ github }}">GitHub</a>
            </div>
        </div>
        {% if avatar %}<img src="{{ avatar }}" alt="{{ name }}" class="avatar">{% endif %}
    </div>

    <h2>Career Profile</h2>
    <p>{{ summary }}</p>

    <h2>Experience</h2>
    {% for job in experience %}
    <div class="section">
        <strong>{{ job.role }}</strong> — {{ job.company }} ({{ job.dates }})
        <ul>
            {% for bullet in job.bullets %}<li>{{ bullet }}</li>{% endfor %}
        </ul>
    </div>
    {% endfor %}

    <h2>Projects</h2>
    {% for project in projects %}
    <div class="project">
        <strong>{{ project.title }}</strong><br>
        {{ project.description }}
        {% if project.link %}<br><a href="{{ project.link }}">View Project →</a>{% endif %}
    </div>
    {% endfor %}

    <h2>Education</h2>
    {% for edu in education %}
    <div class="section">
        <strong>{{ edu.degree }}</strong><br>
        {{ edu.school }} • {{ edu.dates }}
        {% if edu.extra %}<br><em>{{ edu.extra }}</em>{% endif %}
    </div>
    {% endfor %}

    <h2>Certifications</h2>
    <ul>{% for cert in certifications %}<li>{{ cert }}</li>{% endfor %}</ul>

    <h2>Skills</h2>
    <ul>{% for skill in skills %}<li>{{ skill }}</li>{% endfor %}</ul>

    <div class="footer no-print">
        Generated {{ year }} • Simple Python + YAML Resume Tool
    </div>
</body>
</html>
"""

template = Template(html_template)
output = template.render(data)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print("✅ index.html generated!")
webbrowser.open('index.html')
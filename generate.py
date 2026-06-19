import yaml
from jinja2 import Template
import datetime
from weasyprint import HTML, CSS

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
        
        body { 
            font-family: 'Inter', Arial, sans-serif; 
            margin: 0; 
            padding: 25px; 
            line-height: 1.35; 
            color: #222; 
            max-width: 1000px; 
            margin: 0 auto; 
            font-size: 15px; 
        }
        .header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; }
        .header-left h1 { margin: 0 0 4px 0; font-size: 2.1em; }
        .header-left .title { color: #0d6efd; font-weight: 500; }
        .avatar { width: 110px; height: 110px; border-radius: 50%; object-fit: cover; border: 4px solid #0d6efd; }
        .contact { margin: 12px 0 20px; font-size: 1.05em; }
        h2 { color: #0d6efd; border-bottom: 3px solid #0d6efd; padding-bottom: 6px; margin-top: 28px; margin-bottom: 12px; }
        ul { padding-left: 20px; }
        li { margin-bottom: 7px; }
        .section { margin-bottom: 22px; }
        .project { margin-bottom: 16px; }
        .footer { text-align: center; margin-top: 40px; font-size: 0.8em; color: #666; }
    </style>
</head>
<body>
    <!-- ... same HTML body as before ... -->
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
    </div>
    {% endfor %}

    <h2>Certifications</h2>
    <ul>{% for cert in certifications %}<li>{{ cert }}</li>{% endfor %}</ul>

    <h2>Skills</h2>
    <ul>{% for skill in skills %}<li>{{ skill }}</li>{% endfor %}</ul>

    <div class="footer">
        Generated {{ year }} • Simple Python + YAML Resume Tool
    </div>
</body>
</html>
"""

template = Template(html_template)
html_content = template.render(data)

# Generate PDF directly
HTML(string=html_content, base_url='.').write_pdf('Cameron_Paulk_Resume.pdf')

print("✅ PDF generated successfully with selectable text!")
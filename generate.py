#!/usr/bin/env python3
"""
Resume PDF Generator
Generates a professional PDF resume from resume.yml using Jinja2 + WeasyPrint.
"""

import yaml
import re
import datetime
from pathlib import Path
from jinja2 import Template
from weasyprint import HTML


def load_resume_data(yaml_path: str = "resume.yml") -> dict:
    """Load resume data from YAML file."""
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data


def generate_filename(name: str) -> str:
    """Create a clean, professional filename from the person's name."""
    if not name:
        name = "Resume"
    safe_name = re.sub(r"[^\w\-]", "_", name).strip("_")
    return f"{safe_name}_Resume.pdf"


def create_resume_pdf(
    yaml_path: str = "resume.yml",
    output_dir: str = "."
) -> str:
    """
    Generate a professional PDF resume.
    Returns the path to the generated PDF.
    """
    # Load data
    data = load_resume_data(yaml_path)
    data["year"] = datetime.datetime.now().year

    # Generate output filename dynamically
    name = data.get("name", "Resume")
    filename = generate_filename(name)
    output_path = Path(output_dir) / filename

    # HTML Template
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{ name }} - Resume</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Space+Grotesk:wght@500;600&amp;display=swap');

        body {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            font-size: 14.5px;
            line-height: 1.55;
            color: #1f2937;
            max-width: 860px;
            margin: 0 auto;
            padding: 32px 40px;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 24px;
        }

        .header-left h1 {
            margin: 0 0 6px 0;
            font-family: 'Space Grotesk', Inter, sans-serif;
            font-size: 2.25rem;
            font-weight: 600;
            color: #111827;
        }

        .title {
            color: #0d6efd;
            font-weight: 600;
            font-size: 1.05rem;
        }

        .contact {
            margin-top: 10px;
            font-size: 0.95rem;
            color: #4b5563;
        }

        .contact a {
            color: #0d6efd;
            text-decoration: none;
        }

        .avatar {
            width: 118px;
            height: 118px;
            border-radius: 9999px;
            object-fit: cover;
            border: 5px solid #0d6efd;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        }

        h2 {
            color: #0d6efd;
            font-size: 1.15rem;
            font-weight: 600;
            border-bottom: 2.5px solid #0d6efd;
            padding-bottom: 6px;
            margin-top: 28px;
            margin-bottom: 12px;
        }

        ul {
            padding-left: 18px;
            margin: 0;
        }

        li {
            margin-bottom: 6px;
        }

        .section {
            margin-bottom: 16px;
        }

        .project {
            margin-bottom: 14px;
        }

        @page {
            size: letter;
            margin: 0.6in 0.65in;
        }
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
        {% if avatar %}
        <img src="{{ avatar }}" alt="{{ name }}" class="avatar">
        {% endif %}
    </div>

    <h2>Career Profile</h2>
    <p>{{ summary }}</p>

    <h2>Experience</h2>
    {% for job in experience %}
    <div class="section">
        <strong>{{ job.role }}</strong> — {{ job.company }} ({{ job.dates }})
        <ul>
            {% for bullet in job.bullets %}
            <li>{{ bullet }}</li>
            {% endfor %}
        </ul>
    </div>
    {% endfor %}

    <h2>Projects</h2>
    {% for project in projects %}
    <div class="project">
        <strong>{{ project.title }}</strong><br>
        {{ project.description }}
        {% if project.link %}
        <br><a href="{{ project.link }}">View Project →</a>
        {% endif %}
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
    <ul>
        {% for cert in certifications %}
        <li>{{ cert }}</li>
        {% endfor %}
    </ul>

    <h2>Skills</h2>
    <ul>
        {% for skill in skills %}
        <li>{{ skill }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

    # Render HTML
    template = Template(html_template)
    html_content = template.render(data)

    # Generate PDF
    HTML(string=html_content, base_url=".").write_pdf(str(output_path))

    return str(output_path)


if __name__ == "__main__":
    try:
        output_file = create_resume_pdf()
        print(f"✅ Resume PDF generated: {output_file}")
    except FileNotFoundError:
        print("❌ Error: resume.yml not found in current directory.")
    except Exception as e:
        print(f"❌ Error generating resume: {e}")
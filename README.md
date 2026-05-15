# ResumeGen

**Simple. No bullshit. Just YAML + Python → Beautiful Resume.**

A minimal, self-hosted resume builder that turns a single `resume.yml` file into a clean, modern, print-perfect HTML resume (and PDF).

Built because every existing resume tool was bloated, full of AI spam, or had broken LinkedIn/PDF imports.

### Features
- One YAML file = your entire resume
- Modern, professional HTML output
- Perfect PDF via browser print (Ctrl + P)
- Headshot support
- Fully customizable
- Zero dependencies for basic use (just Python + PyYAML + Jinja2)
- GitHub Pages ready in one click

### Quick Start

```bash
# 1. Clone or download the repo
git clone https://github.com/camwin/resumegen.git
cd resumegen

# 2. Install dependencies
pip install pyyaml jinja2

# 3. Edit your resume
# → Open resume.yml and update your info

# 4. Generate the resume
python generate.py
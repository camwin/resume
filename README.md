# Resume

**YAML + Python = Beautiful Resume.**

A minimal, self-hosted resume builder that turns a single `resume.yml` file into a clean, modern, print-perfect HTML resume (and PDF).

Built because every existing resume tool was bloated, full of AI spam, or had broken imports.

### Features
- One YAML file = your entire resume
- Modern, professional HTML output with headshot support
- Perfect PDF via browser print (Ctrl + P)
- Fully customizable and no-bullshit
- GitHub Pages ready

### Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/camwin/resume.git
cd resume

# 2. Install dependencies
pip install pyyaml jinja2

# 3. Edit your info
#    → Open and update resume.yml

# 4. Generate the resume
python generate.py
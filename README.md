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
#    → create resume.yml

# 4. Generate the resume
python generate.py

```
### Github.io resume hosting
To host your resume under your own github.io URL:
After cloning or forking the repo:
1. Configure your resume.yml and run generate.py. Push to your repo. 
2. Goto settings (top tab)
3. Goto Pages (left menu)
4. Set the "Branch" to main and then save

You should now have the resume available at https://yourUsername.github.io/resume/


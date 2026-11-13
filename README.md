# AI EDA & ML Pipeline Evaluator Agent

## 📌 Overview
This AI Agent is an automated code reviewer designed to evaluate Exploratory Data Analysis (EDA) and Machine Learning (ML) pipelines. Inspired by the evaluation agent used in the **AISG Foundations** program, this tool analyzes your project codebase and generates a comprehensive, structured feedback report.

It acts as a virtual Data Science Mentor by:
- Rating your EDA and ML Pipeline out of 100 based on a strict evaluation rubric.
- Highlighting technical strengths and sound architectural choices.
- Providing concrete, actionable suggestions for learners to improve their data hygiene, feature engineering, model selection, and evaluation rigor.

---

## 🚀 1. Installation & Setup

You can either clone this repository to your local machine or duplicate/fork it to your own GitHub account to run as a remote action.

### Option A: Clone to Local Machine
To run the agent locally on your computer:
```bash
# Clone the repository
git clone https://github.com/your-username/eda_assessment_agent.git
cd eda_assessment_agent

# (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install the required dependencies
pip install -r requirements.txt
```

### Option B: Duplicate to Your GitHub
To use this as an automated GitHub Action, simply **fork** or **duplicate** this repository to your own GitHub account.

---

## 💻 2. How to Run Locally

If you cloned the project to your local machine, you can run it directly against any local data science repository.

**Step 1: Set your Gemini API Key**
You must set your Google AI Studio key as an environment variable in your terminal.
*   **Linux/macOS:** `export GEMINI_API_KEY="your-api-key"`
*   **Windows (PowerShell):** `$env:GEMINI_API_KEY="your-api-key"`
*   **Windows (CMD):** `set GEMINI_API_KEY=your-api-key`

**Step 2: Run the Evaluator**
Use the CLI to point the agent to the folder containing the project you want evaluated.
```bash
# Example: Pointing to a repository sitting in the parent folder
python main.py --repo-path "../my-ml-project"
```

The agent will scan the target folder and generate a detailed report inside the `evaluation_reports/` directory.

---

## ☁️ 3. How to Run via GitHub Actions

You can execute this agent entirely in the cloud using GitHub Actions. This allows you to evaluate any of your remote repositories without running code locally.

### Step 1: Configure Repository Secrets
Navigate to your repository on GitHub, then go to **Settings > Secrets and variables > Actions**. You need to add two **New repository secrets**:

1.  `GEMINI_API_KEY`: Your API key from Google AI Studio.
2.  `GH_PAT_TOKEN`: A GitHub Personal Access Token (Classic or Fine-Grained).
    *   *Why?* This is required if the agent needs to check out a **private** repository that you want to evaluate. Ensure the token has `repo` (Read-only) permissions.

### Step 2: Trigger the Workflow
1. Go to the **Actions** tab of this repository.
2. Click on the **Dynamic AI Repo Review** workflow on the left sidebar.
3. Click the **Run workflow** dropdown button.
4. An input box will appear. **Enter the name of the repository** you wish to evaluate (e.g., `activity-lvl`).
5. Click the green **Run workflow** button.

### Step 3: Download the Report
Once the GitHub Action completes successfully, click into the workflow run. Scroll down to the **Artifacts** section and download the generated `evaluation_report.md` file to view your score and feedback!

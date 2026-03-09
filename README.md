# Daily Insight Auto-Logger

This project automates daily journal entries by fetching a random programming quote from ZenQuotes and the local weather for Seattle from wttr.in. It then appends this information to a `journal.md` file and automatically commits the changes to a GitHub repository every day.

## How it works
The `logger.py` script makes API calls to ZenQuotes and wttr.in. It formats the data and appends it to `journal.md` with the current date.
A GitHub Actions workflow (`.github/workflows/daily.yml`) is scheduled to run this script daily at 1 PM UTC. It checks out the repository, installs the required `requests` library, runs the script, and pushes the updated `journal.md` back to the repository.

## Local Deployment / Running Manually

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script:**
   ```bash
   python logger.py
   ```
   This will fetch the quote and weather, append it to `journal.md`, and print a success message.

## GitHub Actions Deployment

1. **Push to GitHub:** Ensure your code (`logger.py`, `requirements.txt`, `.github/workflows/daily.yml`, and `journal.md`) is pushed to your GitHub repository.
2. **Workflow Permissions:** Go to your repository settings on GitHub: Settings -> Actions -> General -> Workflow permissions. Ensure "Read and write permissions" is selected. This allows the action to commit changes back to the repository.
3. **Automatic Execution:** The workflow will automatically run daily at 1 PM UTC based on the cron schedule in `.github/workflows/daily.yml`.
4. **Manual Execution:** You can also manually trigger the workflow from the "Actions" tab in your GitHub repository. Select the "Daily Insight Auto-Logger" workflow and click "Run workflow".

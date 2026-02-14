import schedule
import time
import os
import subprocess
import logging
import signal
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Get the absolute path of the project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # This is `scripts/`
PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)  # Move up to `real_time_sentiment_analysis/`

# Correct path to the Python executable in the virtual environment
PYTHON_EXECUTABLE = os.path.join(PROJECT_ROOT, "sentiment_env", "Scripts", "python.exe")

# Correct paths for the scripts inside the `scripts/` directory
SCRIPTS = [
    os.path.join(PROJECT_ROOT, "scripts", "data_collection.py"),
    os.path.join(PROJECT_ROOT, "scripts", "preprocessing.py"),
    os.path.join(PROJECT_ROOT, "scripts", "emotion_detection.py"),
    os.path.join(PROJECT_ROOT, "scripts", "sentiment_analysis.py"),
    os.path.join(PROJECT_ROOT, "scripts", "anomaly_detection.py"),
    os.path.join(PROJECT_ROOT, "scripts", "sentiment_forecasting.py"),
]

def run_all_scripts():
    """Run all scheduled scripts."""
    logging.info("▶ Running all scheduled scripts...")
    for script in SCRIPTS:
        logging.info(f"⏳ Running {script}...")

        # Ensure UTF-8 encoding and suppress TensorFlow warnings
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        env["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Suppress TensorFlow logs (0 = all, 3 = errors only)
        env["TF_ENABLE_ONEDNN_OPTS"] = "0"  # Suppress oneDNN warnings

        result = subprocess.run(
            [PYTHON_EXECUTABLE, script],
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=env
        )

        # Log script output
        if result.stdout:
            logging.info(result.stdout)
        if result.stderr:
            # Filter out TensorFlow and cmdstanpy warnings
            if "WARNING:tensorflow:" not in result.stderr and "cmdstanpy - INFO" not in result.stderr:
                logging.error(f"❌ Error in {script}: {result.stderr}")

    logging.info("✅ All scripts executed successfully!\n")

# Schedule all scripts to run every 2 minutes
schedule.every(2).minutes.do(run_all_scripts)

# Graceful shutdown handler
def graceful_shutdown(signum, frame):
    """Handle graceful shutdown."""
    logging.info("🛑 Shutting down scheduler gracefully...")
    sys.exit(0)

# Register signal handlers for graceful shutdown
signal.signal(signal.SIGINT, graceful_shutdown)  # Ctrl+C
signal.signal(signal.SIGTERM, graceful_shutdown)  # Termination signal

# Main loop
logging.info("🚀 Starting scheduler...")
while True:
    schedule.run_pending()
    time.sleep(30)  # Check every 60 seconds

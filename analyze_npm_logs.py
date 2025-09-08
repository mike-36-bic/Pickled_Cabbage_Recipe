import os
import shutil
import glob
from datetime import datetime

def find_latest_npm_log():
    """
    Finds the most recent npm debug log file in the user's home directory.
    Returns the full path to the log file or None if not found.
    """
    # npm stores logs in a directory like ~/.npm/_logs/
    log_dir = os.path.join(os.path.expanduser('~'), '.npm', '_logs')
    
    if not os.path.isdir(log_dir):
        print(f"Error: npm logs directory not found at {log_dir}")
        return None
    
    # Find all debug log files and sort by modification time to get the latest
    list_of_logs = glob.glob(os.path.join(log_dir, '*-debug-*.log'))
    if not list_of_logs:
        return None
        
    latest_log = max(list_of_logs, key=os.path.getmtime)
    return latest_log

def analyze_and_summarize_log(log_path):
    """
    Analyzes a given npm log file and returns a structured summary of the error.
    """
    summary = {
        "timestamp": os.path.getmtime(log_path),
        "file_path": log_path,
        "error_type": "Unknown Error",
        "error_message": "",
        "npm_version": "",
        "node_version": "",
    }
    
    with open(log_path, 'r', errors='ignore') as f:
        lines = f.readlines()
        for line in lines:
            if "npm ERR! code" in line:
                summary["error_type"] = line.split("npm ERR! code ")[1].strip()
            if "npm ERR! Failed to parse" in line:
                summary["error_message"] = line.strip()
            if "info using npm@" in line:
                summary["npm_version"] = line.split("info using npm@")[1].strip()
            if "info using node@" in line:
                summary["node_version"] = line.split("info using node@")[1].strip()
            if "npm ERR! JSON.parse" in line:
                summary["error_message"] += "\n" + line.strip().split("npm ERR! JSON.parse ")[1]
            
    return summary

def main():
    """
    Main function to find, copy, and analyze the latest npm log.
    """
    print("Starting local CI/CD log analysis...")
    latest_log_path = find_latest_npm_log()
    
    if not latest_log_path:
        print("No npm debug logs found. Run 'npm install' to generate logs on failure.")
        return

    summary = analyze_and_summarize_log(latest_log_path)
    
    # Create a sequential log file in the project directory
    project_log_dir = "local-ci-logs"
    os.makedirs(project_log_dir, exist_ok=True)
    
    existing_logs = glob.glob(os.path.join(project_log_dir, "npm-error-*.log"))
    next_log_number = len(existing_logs) + 1
    new_log_filename = f"npm-error-{next_log_number:02d}.log"
    new_log_path = os.path.join(project_log_dir, new_log_filename)
    
    shutil.copyfile(latest_log_path, new_log_path)
    
    # Print a summary of the error
    print("\n-----------------------------------------------------")
    print("             NPM Build Failure Summary             ")
    print("-----------------------------------------------------")
    print(f"Copied log to: {new_log_path}")
    print(f"Original Log Time: {datetime.fromtimestamp(summary['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Node Version: {summary['node_version']}")
    print(f"NPM Version: {summary['npm_version']}")
    print(f"Error Type: {summary['error_type']}")
    print(f"Error Message: {summary['error_message']}")
    print("-----------------------------------------------------\n")
    print("Action Required: Please fix the syntax error in your package.json as described above.")
    print("Once fixed, run 'npm install' again.")

if __name__ == "__main__":
    main()

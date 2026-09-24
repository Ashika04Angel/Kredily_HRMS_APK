"""
API Automation Test Runner: Executes Kredily HRMS API test suite and produces HTML report
"""
import sys
import os
import subprocess
import time
from datetime import datetime

# Configure standard encoding for Windows console output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    reports_dir = os.path.join(os.path.dirname(base_dir), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    report_html = os.path.join(reports_dir, "api_test_execution_report.html")
    
    print("=" * 70)
    print(">> KREDILY HRMS API AUTOMATION TEST SUITE")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Target Base URL: https://app.kredily.com")
    print(f"API Test Modules: Auth, Attendance, Leave Management, Dashboard")
    print("=" * 70)
    
    cmd = [
        sys.executable, "-m", "pytest",
        os.path.join(base_dir, "python-api-tests"),
        "-v",
        f"--html={report_html}",
        "--self-contained-html"
    ]
    
    start_time = time.time()
    try:
        result = subprocess.run(cmd, cwd=base_dir, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        duration = round(time.time() - start_time, 2)
        
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
            
        print("=" * 70)
        print(f">> API Automation Execution Completed in {duration}s")
        print(f">> Detailed HTML Report: {report_html}")
        print("=" * 70)
        return result.returncode
    except Exception as e:
        print(f"Error executing API automation: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())

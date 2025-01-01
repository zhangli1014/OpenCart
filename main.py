import subprocess
from utilities.s3_writer import upload_report_to_s3
import datetime
from utilities.readconfig import readConfig
import os

bucket_name = readConfig.getconfig('s3 info', 'bucketName')
timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
def run_tests_and_upload_report():
    # Step 1: Run the Selenium UI Tests and generate Allure results
    print("Running UI tests...")
    html_dir = f"html-report-{timestamp}"
    allure_result = "./allure-result"
    allure_report = f"./allure-report-{timestamp}"

    subprocess.run(['pytest','-v','-s','./TestCases', f'--alluredir={allure_result}',f'--html={html_dir}/report.html'], check=True)

    # Step 2: Generate Allure report
    print("Generating Allure report...")
    subprocess.run(['allure', 'generate', f'{allure_result}', '-o', f'{allure_report}', '--clean'], check=True)

    # Step 3: Upload Allure report to S3
    print("Uploading Allure report to S3...")
    upload_report_to_s3(f'{allure_report}', bucket_name,timestamp)
    upload_report_to_s3(f'{html_dir}', bucket_name, timestamp)

# Run the whole process
run_tests_and_upload_report()

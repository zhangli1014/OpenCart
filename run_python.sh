#!/bin/bash
TEST_DIR="./TestCases"                  
REPORT_DIR="./allure-report-$(date +%Y%m%d)"       
RESULT_DIR="./allure-result"
HTML_REPORT="./html-report"
BUCKET_NAME="opencart-test-result"
REPORT_NAME="test_results_$(date +%Y%m%d).html"
AWS_REGION="ca-central-1"

echo "Starting Python script at $(date)"
pytest -v -s $TEST_DIR --html=$HTML_REPORT/report-$(date +%Y%m%d).html --alluredir=$RESULT_DIR
allure generate $RESULT_DIR -o $REPORT_DIR --clean
# 检查测试是否结束
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "Tests completed successfully at $(date)"
else
    echo "Tests failed at $(date). Check logs for details."
fi

# 上传测试报告和日志到 S3
echo "Uploading results to S3..."
echo "bucketname" 
echo $BUCKET_NAME
aws s3 cp $REPORT_DIR/index.html s3://$BUCKET_NAME/ --region $AWS_REGION
aws s3 cp $HTML_REPORT/report-$(date +%Y%m%d).html s3://$BUCKET_NAME/ --region $AWS_REGION
#aws s3 cp $LOG_FILE s3://$BUCKET_NAME/test_logs/$(basename $LOG_FILE) --region $AWS_REGION

if [ $? -eq 0 ]; then
    echo "Results successfully uploaded to S3."
else
    echo "Failed to upload results to S3."
fi
echo "Finished Python script at $(date)"

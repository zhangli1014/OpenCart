pipeline {
    agent any  // 使用 Jenkins 中任何可用的 agent 来运行此任务

    environment {
        // 设置 Python 环境变量
        PYTHON_HOME = "/usr/bin/python3" // 需要根据你服务器上的实际路径修改
    }

    stages {
        stage('checkout code'){
            steps{
                script{
                    // 从 Git 仓库拉取最新的代码
                    checkout scm
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                // 安装依赖
                script {
                    sh 'pip install -r requirements.txt'  // 安装依赖
                }
            }
        }

        stage('Run Tests and Upload Report') {
            steps {
                script {
                    // 运行你的 main.py 文件
                    sh 'python main.py'  // 通过 shell 执行 main.py
                }
            }
        }

        stage('Clean Up') {
            steps {
                // 可选的清理步骤，比如删除临时文件
                script {
                    sh 'rm -rf allure-result allure-report-* html-report-*'
                }
            }
        }
    }

    post {
        always {
            // 确保无论测试成功或失败，都会执行清理操作
            echo "Cleaning up workspace..."
            deleteDir()  // 删除工作区内容
        }
    }
}

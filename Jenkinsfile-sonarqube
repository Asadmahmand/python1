pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.12.3'  // Updated Python version
        SONAR_SERVER = 'sonarserver'
        SONAR_TOKEN = 'sonartoken'
        SONAR_SCANNER = 'sonar6'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Asadmahmand/python1.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh "python${PYTHON_VERSION} -m venv venv" // Create a virtual environment with Python 3.12.3
                sh './venv/bin/pip install --upgrade pip' // Upgrade pip
            }
        }

        stage('Install Dependencies') {
            steps {
                sh './venv/bin/pip install -r requirements.txt' // Install dependencies
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/coverage run --source=src -m unittest discover -s tests -p "test_*.py"' // Run tests with coverage
                sh './venv/bin/coverage xml' // Generate coverage report
            }
        }

        stage('Sonar Code Analysis') {
            environment {
                scannerHome = tool 'sonar6'
            }
            steps {
                withSonarQubeEnv('sonarserver') {
                    sh '''${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=python1 \
                       -Dsonar.projectName=python1 \
                       -Dsonar.projectVersion=1.0 \
                       -Dsonar.sources=src \
                       -Dsonar.python.coverage.reportPaths=coverage.xml'''
                }
            }
        }

        stage('Check Dependencies') {
            steps {
                sh './venv/bin/pip list --outdated' // Check for outdated dependencies
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed. Please check the logs.'
        }
    }
}

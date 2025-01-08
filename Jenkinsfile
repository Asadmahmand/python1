pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9' // Specify the Python version
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Asadmahmand/python1.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh 'python3 -m venv venv' // Create a virtual environment
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
                sh './venv/bin/python -m unittest discover' // Discover and run unit tests
            }
        }

        stage('Package Application') {
            steps {
                echo 'Packaging is optional for Python projects'
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

pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9' // Define the Python version to use
    }

    tools {
        python "Python${PYTHON_VERSION}" // Ensure Python is installed in Jenkins
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Asadmahmand/python1.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh 'python -m venv venv' // Create a virtual environment
                sh './venv/bin/pip install --upgrade pip' // Upgrade pip
            }
        }


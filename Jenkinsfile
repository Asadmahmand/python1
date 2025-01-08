pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9' // Specify the Python version
        SONAR_SERVER = 'sonarserver'  // SonarQube server name
        SONAR_TOKEN = 'sonartoken'   // SonarQube server token
        SONAR_SCANNER = 'sonar6'     // SonarQube scanner tool name
        SONAR_HOST_URL = 'http://172.31.21.227'
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
               sh './venv/bin/python -m unittest discover -s tests -p "test_*.py"'
            }
        }

        stage('Package Application') {
            steps {
                echo 'Packaging is optional for Python projects'
            }
        }
        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('sonarserver') {
                    sh """
                        ${tool('sonar6')}/bin/sonar-scanner \
                        -Dsonar.projectKey=my-python-project \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=${env.SONAR_HOST_URL} \
                        -Dsonar.login=${env.SONAR_TOKEN}
                    """
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

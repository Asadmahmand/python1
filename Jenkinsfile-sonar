pipeline {
    agent any

    environment {
        SONAR_SERVER = 'sonarserver'  // SonarQube server name
        SONAR_TOKEN = 'sonartoken'   // SonarQube server token
        SONAR_SCANNER = 'sonar6'     // SonarQube scanner tool name
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/python -m unittest discover'
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
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Build failed. Please check the logs.'
        }
    }
}

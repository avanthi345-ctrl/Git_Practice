pipeline {
    agent any

    environment {
        APP_CREDENTIALS = credentials('demo-app-credentials')
    }

    stages {
        stage('Welcome') {
            steps {
                echo 'Hello Avanthika!'
                echo 'My first Jenkins Pipeline is running!'
            }
        }

    stage('Credential Test') {
    steps {
        bat 'echo Username is %APP_CREDENTIALS_USR%'
         }
       }    

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\SHASHWATH\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat '"C:\\Users\\SHASHWATH\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m playwright install chromium'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '"C:\\Users\\SHASHWATH\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest -v --junitxml=pytest-results.xml'
            }
        }
    }

    post {
        always {
            junit 'pytest-results.xml'
        }
    }
}
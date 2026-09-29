pipeline {
    agent any

    stages {
        stage('Welcome') {
            steps {
                echo 'Hello Avanthika!'
                echo 'My first Jenkins Pipeline is running!'
            }
        }

            stage('Install Dependencies') {
        steps {
             bat '"C:\\Users\\SHASHWATH\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
              }
            }

        stage('Execute Python') {
            steps {
                bat '"C:\\Users\\SHASHWATH\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest -v'
            }
        }

       }

    }

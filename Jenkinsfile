pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Running the app'
                sh 'python app.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Running unit tests'
                sh 'python -m unittest discover'
            }
        }
    }
}

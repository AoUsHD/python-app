pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python app.py' // or whatever your app does
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover'
            }
        }
    }
}

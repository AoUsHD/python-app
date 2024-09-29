pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/AoUsHD/python-app.git'
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python app.py'
            }
        }
        stage('Run Tests') {   // This is the new stage
            steps {
                sh 'python -m unittest discover'
            }
        }
    }
}


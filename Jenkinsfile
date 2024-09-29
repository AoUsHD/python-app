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
    }
}

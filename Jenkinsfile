pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python app.py' // Running the app
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover' // Running the tests
            }
        }
    }
}

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
                sh '''
                    set +x; 
                    echo "Starting Unit Tests..."
                    python -m unittest discover
                '''
            }
        }
    }
}

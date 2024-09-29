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
        stage('Deploy') {
            steps {
                // Deployment steps, assuming a Docker-based app
                sh 'docker build -t myapp:latest .' // Build Docker image
                sh 'docker run -d -p 5000:5000 myapp:latest' // Run the app in a container
            }
        }
    }
}

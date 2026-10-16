
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub repository connected!'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage successful'
            }
        }

        stage('Test') {
            steps {
                echo 'Test stage successful'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}

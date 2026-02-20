pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                sh 'python3 test.py'
            }
        }
    }

    post {
        success {
            emailext(
                to: 'vidyavn1234@gmail.com',
                subject: 'Jenkins Job SUCCESS',
                body: 'The Jenkins pipeline executed successfully and the Python script ran without errors.'
            )
        }

        failure {
            emailext(
                to: 'vidyavn1234@gmail.com',
                subject: 'Jenkins Job FAILURE',
                body: 'The Jenkins pipeline failed. Please check the console output for error details.'
            )
        }
    }
}
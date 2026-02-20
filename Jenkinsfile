pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                sh '''
                echo "Running Python script..."
                python3 test.py
                echo "Python script execution completed."
                '''
            }
        }
    }

    post {
        success {
            emailext(
                to: 'vidyavn1234@gmail.com',
                subject: 'Jenkins Job SUCCESS',
                body: 'The Jenkins pipeline executed successfully. Please check Jenkins console output for details.'
            )
        }

        failure {
            emailext(
                to: 'vidyavn1234@gmail.com',
                subject: 'Jenkins Job FAILURE',
                body: 'The Jenkins pipeline failed. Please check Jenkins console output for error details.'
            )
        }
    }
}

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


pipeline {
    agent any

    environment {
        IMAGE_NAME = 'idomash97/devops-ido-flask-app'
        IMAGE_TAG = 'latest'
        CHART_PATH = 'assignment-3-helm\\flask-app'
    }

    stages {
        stage('Build') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% assignment-1-docker'
            }
        }

        stage('Test') {
    steps {
        bat 'helm lint %CHART_PATH%'
        bat 'kubectl config current-context'
        bat 'kubectl cluster-info'
        bat 'helm upgrade --install flask-app %CHART_PATH%'
        bat 'kubectl rollout status deployment/flask-app'
        bat 'start /B kubectl port-forward service/flask-app 18080:5000'
        bat 'timeout /t 5 /nobreak'
        bat 'curl -f http://127.0.0.1:18080/health'
    }
}

        stage('Deploy') {
            steps {
                bat 'docker push %IMAGE_NAME%:%IMAGE_TAG%'
            }
        }
    }
}

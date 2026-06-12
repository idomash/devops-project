pipeline {
    agent any

    environment {
    IMAGE_NAME = 'idomash97/devops-ido-flask-app'
    IMAGE_TAG = 'latest'
    CHART_PATH = 'assignment-3-helm\\flask-app'
    KUBECONFIG = 'C:\\Users\\97250\\.kube\\config'
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
        bat 'ping 127.0.0.1 -n 6 > nul'
        bat 'curl -f http://127.0.0.1:18080/health'
    }
}

        stage('Deploy') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-credentials',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASS'
        )]) {
            bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
            bat 'docker push %IMAGE_NAME%:%IMAGE_TAG%'
        }
    }
}
    }
}

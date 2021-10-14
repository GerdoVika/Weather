pipeline {
    agent any
    
    stages {
        stage ('Checkout'){
            steps {
                checkout scm
            }
        }
        stage('Deploy image') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub_id') {
                        def customImage = docker.build('gerdovika/weather_app')
                        customImage.push()
                    }
                }
            }
        }
    }
}

pipeline {
    agent any
    
    stages {
        stage('Deploy image') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub_id') {
                        def customImage = docker.build('gerdovika/weather_app' + ":$BUILD_NUMBER")
                        customImage.push()
                    }
                }
            }
        }
    }
}

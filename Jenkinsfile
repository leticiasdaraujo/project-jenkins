pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verificar Versão do Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Testar: Celsius para Fahrenheit') {
            steps {
                echo 'Executando conversão de 30°C para Fahrenheit...'
                sh 'python3 conversor.py -t F -v 30'
            }
        }

        stage('Testar: Fahrenheit para Celsius') {
            steps {
                echo 'Executando conversão de 100°F para Celsius...'
                sh 'python3 conversor.py -t C -v 100'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executada com sucesso! As conversões funcionaram.'
        }
        failure {
            echo 'Algo deu errado! Verifique os logs e se o Python está instalado no servidor do Jenkins.'
        }
    }
}

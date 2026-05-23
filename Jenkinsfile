pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verificar Versao do Python') {
            steps {
                bat '"C:\\Users\\letic\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" --version'
            }
        }

        stage('Testar: Celsius para Fahrenheit') {
            steps {
                echo 'Executando conversao de 30C para Fahrenheit...'
                bat '"C:\\Users\\letic\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" conversor.py -t F -v 30'
            }
        }

        stage('Testar: Fahrenheit para Celsius') {
            steps {
                echo 'Executando conversao de 100F para Celsius...'
                bat '"C:\\Users\\letic\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" conversor.py -t C -v 100'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executada com sucesso! As conversoes funcionaram.'
        }
        failure {
            echo 'Algo deu errado! Verifique os logs do console para entender o motivo.'
        }
    }
}
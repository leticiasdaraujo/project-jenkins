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
                // Mudamos de 'sh' para 'bat' porque seu Jenkins roda no Windows
                // E mudamos de 'python3' para 'python'
                bat 'python --version'
            }
        }

        stage('Testar: Celsius para Fahrenheit') {
            steps {
                echo 'Executando conversao de 30C para Fahrenheit...'
                bat 'python conversor.py -t F -v 30'
            }
        }

        stage('Testar: Fahrenheit para Celsius') {
            steps {
                echo 'Executando conversao de 100F para Celsius...'
                bat 'python conversor.py -t C -v 100'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executada com sucesso! As conversoes funcionaram.'
        }
        failure {
            echo 'Algo deu errado! Verifique se o Python esta marcado nas variaveis de ambiente (PATH) do Windows.'
        }
    }
}

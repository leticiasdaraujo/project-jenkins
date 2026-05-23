pipeline {
    agent any

    triggers {
            cron('* * * * *')
        }
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
                bat '"C:\\Users\\letic\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" temperature_conversion.py -t F -v 30'
            }
        }

        stage('Testar: Fahrenheit para Celsius') {
            steps {
                echo 'Executando conversao de 100F para Celsius...'
                bat '"C:\\Users\\letic\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" temperature_conversion.py -t C -v 100'
            }
        }
    }
    stage('Testes Unitarios com Validacao de Erro') {
            steps {
                script {
                    try {
                        echo 'Executando testes...'
                        bat '"C:\\Users\\letic\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" temperature_conversion.py -t F -v 30'
                    } catch (Exception e) {
                        echo 'O teste falhou! Marcando o build como INSTAVEL (Amarelo).'
                        currentBuild.result = 'UNSTABLE'
                    }
                }
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


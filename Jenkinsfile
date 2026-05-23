pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
}
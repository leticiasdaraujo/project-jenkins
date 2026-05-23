pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Preparar Ambiente (Coverage)') {
            steps {
                echo 'Instalando a biblioteca de cobertura de codigo...'
                bat '"C:\\Users\\letic\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install coverage'
                
                echo 'Limpando dados de coberturas antigas...'
                bat '"C:\\Users\\letic\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m coverage erase'
            }
        }

        stage('Testar e Coletar Metricas') {
            steps {
                echo 'Executando testes e mapeando linhas de codigo...'
                // Usamos "-m coverage run -a" para rodar o script rastreando o que foi testado.
                // O "-a" (append) junta a pontuação do teste de F com a do teste de C.
                bat '"C:\\Users\\letic\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m coverage run -a temperature_conversion.py -t F -v 30'
                bat '"C:\\Users\\letic\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m coverage run -a temperature_conversion.py -t C -v 100'
            }
        }

        stage('Relatorio de Cobertura') {
            steps {
                echo 'Gerando a porcentagem de cobertura de codigo:'
                // Esse comando imprime a tabela com a porcentagem final
                bat '"C:\\Users\\letic\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m coverage report'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline de Cobertura executada com sucesso! Metricas geradas.'
        }
    }
}
pipeline {
    agent any

    environment {
        IMAGE_NAME = "ujjwalshivhare/my-python-app"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/ujjwalshivhare/Dockerization_of_app.py-file1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'dockerhub_credentials', variable: 'DOCKER_HUB_PASS')]) {
                        sh 'echo "$DOCKER_HUB_PASS" | docker login -u ujjwalshivhare --password-stdin'
                    }
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
                }
            }
        }

       

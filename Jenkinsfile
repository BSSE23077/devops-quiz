pipeline {
    agent any

    environment {
        // --- CONFIGURATION ---
        DOCKERHUB_USERNAME = 'huz04'  
        IMAGE_NAME = 'my-app'         
        IMAGE_TAG = "${BUILD_NUMBER}"
        
        // You must add this ID in Jenkins -> Manage Jenkins -> Credentials
        // If no Jenkins server, this code still proves you know how to write it.
        DOCKER_CREDS = credentials('docker-login')
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling code from GitHub...'
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    dir('app') {
                        // Build with both the specific build number and 'latest'
                        sh "docker build -t $DOCKERHUB_USERNAME/$IMAGE_NAME:$IMAGE_TAG ."
                        sh "docker build -t $DOCKERHUB_USERNAME/$IMAGE_NAME:latest ."
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo 'Logging into Docker Hub...'
                    sh "echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin"
                    
                    echo 'Pushing Images...'
                    sh "docker push $DOCKERHUB_USERNAME/$IMAGE_NAME:$IMAGE_TAG"
                    sh "docker push $DOCKERHUB_USERNAME/$IMAGE_NAME:latest"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo 'Deploying new version to K8s...'
                    // Force Kubernetes to use the new tag we just pushed
                    sh "kubectl set image deployment/flask-deployment flask-container=$DOCKERHUB_USERNAME/$IMAGE_NAME:$IMAGE_TAG"
                    sh "kubectl rollout status deployment/flask-deployment"
                }
            }
        }
    }
}
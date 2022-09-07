pipeline {

    agent any

    stages {
        stage('Setup') {
            steps {
                script{
                    withCredentials([[
                        sshUserPrivateKey(credentialsId:'62bdec20-80ac-4211-a5d3-1e4737781196', usernameVariable: SSH_USER, keyFileVariable: KEY)
                    ]])  {
                        sh "scp -i $KEY $SSH_USER@192.168.10.120:/home/pi/discord-bot/src/.env /var/jenkins_home/workspace/discord-bot/src/.env"
                    }
                }
            }
        }
        stage('Build') {
            steps {
                withCredentials([
                    usernamePassword(credentialsId:'56cc2a67-e48b-4399-be22-fe2b849ced4b', usernameVariable: USERNAME, passwordVariable: PASSWORD)
                ])  {
                    sh "docker login -u $USERNAME -p $PASSWORD 192.168.10.121:30000"
                    sh "docker build -t stepbot ."
                    sh "docker tag stepbot 192.168.10.121:30000/stepbot:1.0.$BUILD_NUMBER"
                    sh "docker push 192.168.10.121:30000/stepbot:1.0.$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy') {
            steps {
                sh "build_number=$BUILD_NUMBER"
                sh 'current_version=$(cat /home/pi/discord-bot/src/manifest/version.txt)'
                sh "sed -i s/1.0.$current_version/1.0.$build_number/ /home/pi/discord-bot/src/manifest/stepbot-deployment.yaml"
                sh "kubectl apply -f /home/pi/discord-bot/src/manifest/stepbot-deployment.yaml"
                sh "echo $build_number > /home/pi/discord-bot/src/manifest/version.txt"
            }
        }
    }
}

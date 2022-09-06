pipeline {

    agent any
    environment {
        VERSION = "1.0.0"
        SSH_USER = credentials()
    }
    stages {
        stage('Setup') {
            steps {
                echo "Setup..."
                withCredentials([
                    sshUserPrivateKey(credentialsId:'62bdec20-80ac-4211-a5d3-1e4737781196', usernameVariable: SSH_USER, keyFileVariable: KEY)
                ])  {
                    scp -i ${KEY} ${SSH_USER}@192.168.10.120:/home/pi/discord-bot/src/.env /var/jenkins_home/workspace/discord-bot/src/.env
                }
            }

        stage('Build') {
            steps {
                echo "Build..."
                withCredentials([
                    usernamePassword(credentialsId:'56cc2a67-e48b-4399-be22-fe2b849ced4b', usernameVariable: USERNAME, passwordVariable: PASSWORD)
                ])  {
                    docker login -u ${USERNAME} -p ${PASSWORD} 192.168.10.121:30000
                    docker build -t stepbot .
                    docker tag stepbot 192.168.10.121:30000/stepbot:1.0.${BUILD_NUMBER}
                    docker push 192.168.10.121:30000/stepbot:1.0.${BUILD_NUMBER}
                }

            }

        stage('Deploy') {
            steps {
                build_number=$BUILD_NUMBER
                current_version=$(cat /home/pi/discord-bot/src/manifest/version.txt)
                sed -i s/1.0.$current_version/1.0."$build_number"/ /home/pi/discord-bot/src/manifest/stepbot-deployment.yaml
                kubectl apply -f /home/pi/discord-bot/src/manifest/stepbot-deployment.yaml
                echo $build_number > /home/pi/discord-bot/src/manifest/version.txt
            }
        }
    }
}

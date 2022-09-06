pipeline {

    agent any

    stages {
        stage('Setup') {
            steps {
                scp -i $KEY $SSH_USER@192.168.10.120:/home/pi/discord-bot/src/.env /var/jenkins_home/workspace/discord-bot/src/.env
            }

        stage('Build') {
            steps {
                docker login -u $USERNAME -p $PASSWORD 192.168.10.121:30000
                docker build -t stepbot .
                docker tag stepbot 192.168.10.121:30000/stepbot:1.0.$BUILD_NUMBER
                docker push 192.168.10.121:30000/stepbot:1.0.$BUILD_NUMBER
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

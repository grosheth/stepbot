pipeline {
    agent any

    stages {
        stage('Copy environnement variables') {
            steps {
                scp -i $KEY $SSH_USER@192.168.10.120:/home/pi/discord-bot/src/.env /var/jenkins_home/workspace/discord-bot/src/.env
            }
        }
    }
}

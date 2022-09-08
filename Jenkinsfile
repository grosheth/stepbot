pipeline {

    agent any

    stages {
        stage('Setup') {
            steps {
                withCredentials([
                    sshUserPrivateKey(credentialsId:'62bdec20-80ac-4211-a5d3-1e4737781196', keyFileVariable: 'KEY', usernameVariable: 'SSH_USER')
                ])  {
                    sh "scp -i ${KEY} ${SSH_USER}@192.168.10.120:/home/pi/discord-bot/src/.env /var/jenkins_home/workspace/discord-bot/src/.env"
                }
            }
        }
        stage('Build') {
            steps {
                withCredentials([
                    usernamePassword(credentialsId:'56cc2a67-e48b-4399-be22-fe2b849ced4b', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')
                ])  {
                    sh ''' 
                        docker login -u $USERNAME -p $PASSWORD 192.168.10.121:30000
                        docker build -t stepbot .
                        docker tag stepbot 192.168.10.121:30000/stepbot:1.0.$BUILD_NUMBER
                        docker push 192.168.10.121:30000/stepbot:1.0.$BUILD_NUMBER
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([
                    sshUserPrivateKey(credentialsId:'root-pi', keyFileVariable: 'KEY', usernameVariable: 'SSH_USER')
                ])  {
                        echo '*** Executing remote commands ***'
                        sh '''
                            ssh -i $KEY $SSH_USER@192.168.10.120 << EOF
                            bash /home/pi/discord-bot/src/manifest/get_version.sh
                            echo $current_version
                            sed -i s/1.0.$current_version/1.0.${BUILD_NUMBER}/ /home/pi/discord-bot/src/manifest/stepbot-deployment.yaml
                            kubectl apply -f /home/pi/discord-bot/src/manifest/stepbot-deployment.yaml
                            echo ${BUILD_NUMBER} > /home/pi/discord-bot/src/manifest/version.txt
                            git config --global user.email "salledelavager@gmail.com"
                            git config --global user.name "salledelavage"
                            cd /home/pi/discord-bot && git add . && git commit -m "commit apres modif de version" && git push
                            exit
EOF
'''
                }
            }
        }
    }
}

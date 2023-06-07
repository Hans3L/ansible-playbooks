@Library('jenkins-library@master') _

def PLAYBOOK_TARGET

pipeline {
    agent { label 'linux' }
    environment {
        ANSIBLE_PRIVATE_KEY = credentials('carvajaldev-private-key')
        //ANSIBLE_PRIVATE_KEY = credentials('artifactorydev-private-key')
    }
    parameters {
        /*choice(name: 'ANSIBLE_PRIVATE_KEY',
                'choices': [
                        'carvajaldev-private-key',
                        'America/Asuncion',
                        'America/Bogota',
                        'America/La_Paz'
                ],
                description: 'Key private aws')*/
        choice(name: 'PLAYBOOKS',
                'choices': [
                        'assets/playbooks/message.yml',
                        'assets/playbooks/executor.yml'
                ], description: 'Choose ansible playbooks')
    }
    stages {
        stage('Run Playbook') {
            steps {
                script {
                    PLAYBOOK_TARGET = "${params.PLAYBOOKS}"
                    sh 'ansible-galaxy collection install -r requirements.yml'
                    sh 'ls'
                    //def playbookContent = libraryResource 'assets/playbooks/message.yml'
                    //def playbookPath = libraryResource('assets/playbooks/message.yml')
                    def playbookPath = libraryResource(PLAYBOOK_TARGET)
                    writeFile file: "./playbook.yml", text: playbookPath
                    //sh """'cd ${WORKSPACE} && sudo ansible-playbook --user ubuntu -i inventory/dev.hosts --private-key=$ANSIBLE_PRIVATE_KEY -e "key=/home/ubuntu/.ssh/id_rsa.pub" message.yml'"""
                    sh "cd ${WORKSPACE} && sudo ansible-playbook --user ubuntu -i inventory/dev.hosts --private-key=$ANSIBLE_PRIVATE_KEY -e 'key=$PATH_SSH_PUB' playbook.yml"
                }
            }
        }
    }
}
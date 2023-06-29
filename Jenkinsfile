@Library('jenkins-library@master') _

def PLAYBOOK_TARGET
def PRIVATE_KEY
def ANSIBLE_INVENTORY
pipeline {
    agent { label 'linux' }
    environment {
        //ANSIBLE_PRIVATE_KEY = credentials('carvajaldev-private-key')
        ANSIBLE_PRIVATE_KEY = credentials("${params.ANSIBLE_PKEY}")
    }
    parameters {
        choice(name: 'ANSIBLE_PKEY',
                'choices': [
                        'carvajaldev-private-key',
                        'artifactorydev-private-key'
                ],
                description: 'Key private aws')
        choice(name: 'INVENTORY',
                'choices': [
                        'dev.hosts',
                        'carvajalprd.hosts'
                ],
                description: 'Key private aws')
        choice(name: 'PLAYBOOKS',
                'choices': [
                        'assets/playbooks/message.yml',
                        'assets/playbooks/install-nginx-docker.yml',
                        'assets/playbooks/executor.yml'
                ], description: 'Choose ansible playbooks')
    }
    stages {
        stage('Run Playbook') {
            steps {
                script {
                    PLAYBOOK_TARGET = "${params.PLAYBOOKS}"
                    PRIVATE_KEY = "${params.ANSIBLE_PKEY}"
                    ANSIBLE_INVENTORY = "${params.INVENTORY}"
                    sh 'ansible-galaxy collection install -r requirements.yml'
                    sh 'ls'
                    //def playbookContent = libraryResource 'assets/playbooks/message.yml'
                    //def playbookPath = libraryResource('assets/playbooks/message.yml')
                    def playbookPath = libraryResource(PLAYBOOK_TARGET)
                    writeFile file: "./playbook.yml", text: playbookPath
                    //sh """'cd ${WORKSPACE} && sudo ansible-playbook --user ubuntu -i inventory/dev.hosts --private-key=$ANSIBLE_PRIVATE_KEY -e "key=/home/ubuntu/.ssh/id_rsa.pub" message.yml'"""
                    //sh "cd ${WORKSPACE} && sudo ansible-playbook --user ubuntu -i inventory/dev.hosts --private-key=$ANSIBLE_PRIVATE_KEY -e 'key=$PATH_SSH_PUB' playbook.yml"
                    //sh "cd ${WORKSPACE} && sudo ansible-playbook --user ubuntu -i inventory/dev.hosts --private-key=$ANSIBLE_PRIVATE_KEY -e 'key=$PATH_SSH_PUB' playbook.yml"
                    sh "cd ${WORKSPACE} && sudo ansible-playbook --user ubuntu -i $ANSIBLE_INVENTORY --private-key=$ANSIBLE_PRIVATE_KEY -e 'key=$PATH_SSH_PUB' playbook.yml"
                }
            }
        }
    }
}
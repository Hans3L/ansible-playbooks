@Library('jenkins-library@master') _

pipeline {
    agent { label 'linux' }
    /*environment {
        ANSIBLE_PRIVATE_KEY = credentials('carvajaldev-private-key')
    }*/
    parameters {
        choice(name: 'ANSIBLE_PRIVATE_KEY',
                'choices': [
                        'carvajaldev-private-key',
                        'America/Asuncion',
                        'America/Bogota',
                        'America/La_Paz'
                ],
                description: 'Key private aws')
        choice(name: 'PLAYBOOKS',
                'choices': [
                        'assets/playbooks/message.yml',
                        'Bancosol-dev'
                ], description: 'Choose ansible playbooks')
    }
    stages {
        stage('Run Playbook') {
            steps {
                script {
                    sh 'ansible-galaxy collection install -r requirements.yml'
                    sh 'ls'
                    def playbookPath = libraryResource('assets/playbooks/message.yml')
                    //sh """'cd ${WORKSPACE} && sudo ansible-playbook --user ubuntu -i inventory/dev.hosts --private-key=$ANSIBLE_PRIVATE_KEY -e "key=/home/ubuntu/.ssh/id_rsa.pub" message.yml'"""
                    sh 'cd ${WORKSPACE} && sudo ansible-playbook --user ubuntu -i dev.hosts --private-key=$ANSIBLE_PRIVATE_KEY -e "key=/home/ubuntu/.ssh/id_rsa.pub" message.yml'
                }
            }
        }
    }
}
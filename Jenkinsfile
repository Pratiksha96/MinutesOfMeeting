node {
stage('get code') {
    git branch: 'samridh', credentialsId: 'tsamridhid', url: 'https://github.com/Pratiksha96/MinutesOfMeeting/'
}
stage('create executable') {
    sh label: '', script: 'pyinstaller --onefile main.py'
    sh label: '', script: 'cp gui.ui dist'
}
}

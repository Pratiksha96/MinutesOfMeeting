node {
stage('get code') {
    git credentialsId: 'tsamridh86GHid', url: 'https://github.com/Pratiksha96/MinutesOfMeeting'
}
stage('create executable') {
    sh label: '', script: 'pyinstaller --onefile main.py'
}
}

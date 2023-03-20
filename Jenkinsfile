pipeline {
        agent any
        environment {
            LT_BUILD_NAME = "SeleniumTest"
        }
        stages {
    stage('Clean Up') {
        steps {
            deleteDir()
        }
    }
    stage('Run Selenium Test') {
        steps {
            sh 'wget https://raw.githubusercontent.com/drozkie/webtest/main/helloworld.py'
            sh 'python3 helloworld.py'
        }
    }

    stage('Next Step') {
        steps {
            
            sh 'echo "blah"'
            sh 'ls'
        }
    }
    }
}
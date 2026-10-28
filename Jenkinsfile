pipeline{
	agent any 
	
	environment{
		IMAGE_NAME = 'my-flask-app'
		TAG = 'latest'
	}

	stages{
		stage('Checkout'){
			steps{
				checkout scm
			}
		}
		
		stage('Build Docker image'){
			steps{
				script{
					sh "docker build -t ${IMAGE_NAME}:${TAG} ."
				}
			}
		}
	}

post{
	success{
		echo "Docker image '${IMAGE_NAME}:${TAG}' built successfully "
	}

	failure{
		echo "Pipeline failed during build process"
	}
}

}

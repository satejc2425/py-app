pipeline{
	agent any 
	
	environment{
		IMAGE_NAME = 'my-flask-app'
		TAG = 'latest'
		CONTAINER_NAME = 'my-flask-container'
		PORT = '5000'
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
		stage('Run Docker Container'){
			steps{
				script{
					//removes  exisiting conatiner if running
					sh "docker stop ${CONTAINER_NAME} || true"
					sh "docker rm ${CONTAINER_NAME} || true"

					sh "docker run -d -p ${PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}:${TAG} "
				}
			}
		}
	}

post{
	success{
		echo "Docker image '${IMAGE_NAME}:${TAG}' built successfully and '${CONTAINER_NAME}' is running"
	}

	failure{
		echo "Pipeline failed during build process"
	}
}

}

# End-to-End CI/CD Pipeline using Jenkins, Docker & AWS

## Project Overview
Built an automated CI/CD pipeline using Jenkins on an AWS EC2 Linux instance. The pipeline retrieves source code from GitHub, validates Python syntax, runs automated unit tests, builds a Docker image, tests the application inside Docker, and deploys a container.

## Technologies Used
- AWS EC2
- Linux
- Jenkins
- Git and GitHub
- Docker
- Python
- Groovy (Jenkins Pipeline)

## Pipeline Stages
1. **Checkout:** Retrieves source code from GitHub.
2. **Build:** Checks Python version and validates syntax.
3. **Test:** Runs automated Python unit tests.
4. **Docker Build:** Builds the Docker image.
5. **Docker Test:** Runs unit tests and the application inside Docker.
6. **Deploy:** Starts the application container.
7. **Webhook Trigger:** Automatically triggers Jenkins after a GitHub push.

## Key Features
- Automated CI/CD pipeline
- GitHub webhook integration
- Docker image build and container execution
- Automated Python unit testing
- Deployment through Jenkins

## Application Output
`DevOps CI/CD application is running!`

## Project Repository
https://github.com/Rujuta172/jenkins

## Future Improvements
- Deploy a web application with an exposed application port.
- Add Docker image versioning.
- Integrate monitoring and logging.
- Push images to Amazon ECR.

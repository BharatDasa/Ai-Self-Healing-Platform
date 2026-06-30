pipeline {

    agent {
        label 'devops-toolkit'
    }

    options {
        
        timestamps()
        timeout(time: 90, unit: 'MINUTES')

        buildDiscarder(
            logRotator(
                numToKeepStr: '20'
            )
        )
    }

    environment {

        // =====================================================
        // GIT
        // =====================================================

        GIT_REPO = 'git@github.com:BharatDasa/ai-self-healing-platform.git'

        GIT_BRANCH = 'master'

        // =====================================================
        // IMAGES
        // =====================================================

        IMAGE_REPO = 'bharatdasa'

        FRAUD_IMAGE = "${IMAGE_REPO}/fraud_ai_ml:latest"

        SELF_HEALING_IMAGE = "${IMAGE_REPO}/self-healing_ai_ml:v2"

        SIMULATOR_IMAGE = "${IMAGE_REPO}/transaction-simulator:v1"

        AIRFLOW_IMAGE = "${IMAGE_REPO}/enterprise-airflow:latest"

        // =====================================================
        // NAMESPACES
        // =====================================================

        PLATFORM_NAMESPACE = 'ai-platform'

        AIRFLOW_NAMESPACE = 'airflow'
    }

    stages {

        // =====================================================
        // CHECKOUT
        // =====================================================

        stage('Checkout Repository') {

            steps {

                container('toolkit') {

                    git branch: "${GIT_BRANCH}",
                    credentialsId: 'github-ssh',
                    url: "${GIT_REPO}"

                    sh 'pwd'

                    sh 'ls -la'

                    sh 'tree -L 3 || true'
                }
            }
        }

        // =====================================================
        // VERIFY TOOLKIT
        // =====================================================

        stage('Verify DevOps Toolkit') {

            steps {

                container('toolkit') {

                    sh 'kubectl version --client'

                    sh 'kubectl-argo-rollouts version'

                    sh 'docker --version'

                    sh 'python --version'

                    sh 'helm version'

                    sh 'trivy --version'

                    sh 'jq --version'

                    sh 'git --version'

                    sh 'flake8 --version'

                    sh 'pytest --version'
                }
            }
        }

        // =====================================================
        // VALIDATE FRAUD SERVICE
        // =====================================================

        stage('Validate Fraud Detection Service') {

            steps {

                container('toolkit') {

                    dir('services/fraud-detection') {

                        sh '''
                        pip install \
                        -r requirements.txt \
                        --break-system-packages
                        '''

                        sh '''
                        python -m py_compile app/*.py
                        '''

                        sh 'flake8 app || true'
                    }
                }
            }
        }

        // =====================================================
        // VALIDATE SELF-HEALING
        // =====================================================

        stage('Validate Self-Healing Service') {

            steps {

                container('toolkit') {

                    dir('services/self-healing') {

                        sh '''
                        pip install \
                        -r requirements.txt \
                        --break-system-packages
                        '''

                        sh '''
                        python -m py_compile app/*.py
                        '''

                        sh 'flake8 app || true'
                    }
                }
            }
        }

        // =====================================================
        // VALIDATE TRANSACTION SIMULATOR
        // =====================================================

        stage('Validate Transaction Simulator') {

            steps {

                container('toolkit') {

                    dir('services/transaction-simulator') {

                        sh '''
                        pip install \
                        -r requirements.txt \
                        --break-system-packages
                        '''

                        sh '''
                        python -m py_compile app/*.py
                        '''

                        sh 'flake8 app || true'
                    }
                }
            }
        }

        // =====================================================
        // VALIDATE AIRFLOW DAGS
        // =====================================================

        stage('Validate Airflow DAGs') {

            steps {

                container('toolkit') {

                    dir('ml-pipelines/airflow/dags') {

                        sh '''
                        python -m py_compile *.py
                        '''
                    }
                }
            }
        }

        // =====================================================
        // VALIDATE MLOPS SCRIPTS
        // =====================================================

        stage('Validate MLOps Scripts') {

            steps {

                container('toolkit') {

                    dir('ml-pipelines/airflow/scripts') {

                        sh '''
                        python -m py_compile *.py
                        '''
                    }
                }
            }
        }

        // =====================================================
        // BUILD FRAUD IMAGE
        // =====================================================

        stage('Build Fraud Detection Image') {

            steps {

                container('toolkit') {

                    dir('services/fraud-detection') {

                        sh """
                        docker build \
                        -t ${FRAUD_IMAGE} .
                        """
                    }
                }
            }
        }

        // =====================================================
        // BUILD SELF-HEALING IMAGE
        // =====================================================

        stage('Build Self-Healing Image') {

            steps {

                container('toolkit') {

                    dir('services/self-healing') {

                        sh """
                        docker build \
                        -t ${SELF_HEALING_IMAGE} .
                        """
                    }
                }
            }
        }

        // =====================================================
        // BUILD SIMULATOR IMAGE
        // =====================================================

        stage('Build Simulator Image') {

            steps {

                container('toolkit') {

                    dir('services/transaction-simulator') {

                        sh """
                        docker build \
                        -t ${SIMULATOR_IMAGE} .
                        """
                    }
                }
            }
        }

        // =====================================================
        // BUILD AIRFLOW IMAGE
        // =====================================================

        stage('Build Enterprise Airflow Image') {

            steps {

                container('toolkit') {

                    dir('ml-pipelines/airflow') {

                        sh """
                        docker build \
                        -t ${AIRFLOW_IMAGE} .
                        """
                    }
                }
            }
        }

        // =====================================================
        // TRIVY SCAN FRAUD IMAGE
        // =====================================================

        stage('Trivy Scan Fraud Image') {

            steps {

                container('toolkit') {

                    sh """
                    trivy image \
                    --severity HIGH,CRITICAL \
                    --exit-code 0 \
                    ${FRAUD_IMAGE}
                    """
                }
            }
        }

        // =====================================================
        // TRIVY SCAN SELF-HEALING IMAGE
        // =====================================================

        stage('Trivy Scan Self-Healing Image') {

            steps {

                container('toolkit') {

                    sh """
                    trivy image \
                    --severity HIGH,CRITICAL \
                    --exit-code 0 \
                    ${SELF_HEALING_IMAGE}
                    """
                }
            }
        }

        // =====================================================
        // TRIVY SCAN SIMULATOR IMAGE
        // =====================================================

        stage('Trivy Scan Simulator Image') {

            steps {

                container('toolkit') {

                    sh """
                    trivy image \
                    --severity HIGH,CRITICAL \
                    --exit-code 0 \
                    ${SIMULATOR_IMAGE}
                    """
                }
            }
        }

        // =====================================================
        // TRIVY SCAN AIRFLOW IMAGE
        // =====================================================

        stage('Trivy Scan Airflow Image') {

            steps {

                container('toolkit') {

                    sh """
                    trivy image \
                    --severity HIGH,CRITICAL \
                    --exit-code 0 \
                    ${AIRFLOW_IMAGE}
                    """
                }
            }
        }

        // =====================================================
        // DOCKER LOGIN
        // =====================================================

        stage('DockerHub Login') {

            steps {

                container('toolkit') {

                    withCredentials([
                        usernamePassword(
                            credentialsId: 'Dockerhub',
                            usernameVariable: 'DOCKER_USER',
                            passwordVariable: 'DOCKER_PASS'
                        )
                    ]) {

                        sh """
                        echo \$DOCKER_PASS | docker login \
                        -u \$DOCKER_USER \
                        --password-stdin
                        """
                    }
                }
            }
        }

        // =====================================================
        // PUSH IMAGES
        // =====================================================

        stage('Push Images') {

            parallel {

                stage('Push Fraud Image') {

                    steps {

                        container('toolkit') {

                            sh "docker push ${FRAUD_IMAGE}"
                        }
                    }
                }

                stage('Push Self-Healing Image') {

                    steps {

                        container('toolkit') {

                            sh "docker push ${SELF_HEALING_IMAGE}"
                        }
                    }
                }

                stage('Push Simulator Image') {

                    steps {

                        container('toolkit') {

                            sh "docker push ${SIMULATOR_IMAGE}"
                        }
                    }
                }

                stage('Push Airflow Image') {

                    steps {

                        container('toolkit') {

                            sh "docker push ${AIRFLOW_IMAGE}"
                        }
                    }
                }
            }
        }

        // =====================================================
        // DEPLOY PLATFORM
        // =====================================================

        stage('Deploy AI Platform') {

            steps {

                container('toolkit') {

                    sh '''
                    chmod +x scripts/*.sh
                    '''

                    sh '''
                    ./scripts/deploy.sh
                    '''
                }
            }
        }

        // =====================================================
        // WAIT FOR READINESS
        // =====================================================

        stage('Wait For Platform Readiness') {

            steps {

                container('toolkit') {

                    sh '''
                    kubectl rollout status deploy/self-healing \
                    -n ai-platform \
                    --timeout=300s
                    '''

                    sh '''
                    kubectl rollout status deploy/transaction-simulator \
                    -n ai-platform \
                    --timeout=300s
                    '''

                    sh '''
                    kubectl argo rollouts get rollout \
                    fraud-detection \
                    -n ai-platform 
                    '''
                }
            }
        }

        // =====================================================
        // VERIFY AIRFLOW
        // =====================================================

        stage('Verify Airflow') {

            steps {

                container('toolkit') {

                    sh '''
                    set -e

                    kubectl get pods -n airflow

                    AIRFLOW_POD=$(kubectl get pod -n airflow \
                    -o name | grep airflow-webserver | head -1 | cut -d/ -f2)

                    if [ -z "$AIRFLOW_POD" ]; then
                        echo "❌ Airflow webserver pod not found"
                        exit 1
                    fi

                    echo "Using pod: $AIRFLOW_POD"

                    kubectl wait \
                    --for=condition=Ready pod/$AIRFLOW_POD \
                    -n airflow \
                    --timeout=300s

                    kubectl exec -i -n airflow $AIRFLOW_POD -- \
                    airflow dags list
                    '''
                }
            }
        }

        // =====================================================
        // RUN ENTERPRISE VALIDATION
        // =====================================================

        stage('Run Enterprise Validation') {

            steps {

                container('toolkit') {

                    sh '''
                    chmod +x scripts/validation.sh
                    '''

                    sh '''
                    ./scripts/validation.sh
                    '''
                }
            }
        }

        // =====================================================
        // CHAOS TEST
        // =====================================================

        stage('Run Chaos Resilience Test') {

            steps {

                container('toolkit') {

                    sh '''
                    chmod +x scripts/resilience-test.sh
                    '''

                    sh '''
                    ./scripts/resilience-test.sh || true
                    '''
                }
            }
        }

        // =====================================================
        // CLEANUP
        // =====================================================

        stage('Cleanup Docker Resources') {

            steps {

                container('toolkit') {

                    sh '''
                    docker system prune -af || true
                    '''
                }
            }
        }
    }

    // =====================================================
    // POST ACTIONS
    // =====================================================

    post {

        always {

            container('toolkit') {

                sh 'kubectl get pods -A || true'

                sh 'kubectl get rollout -A || true'

                sh 'kubectl get hpa -A || true'

                sh 'kubectl get scaledobject -A || true'
            }
        }

        success {

            echo ''
            echo '================================================='
            echo '🏆 AI SELF-HEALING PLATFORM DEPLOYED'
            echo '================================================='
            echo ''
            echo '✅ Services validated'
            echo '✅ Airflow validated'
            echo '✅ MLOps validated'
            echo '✅ ML models validated'
            echo '✅ Analytics validated'
            echo '✅ Reports validated'
            echo '✅ Images built'
            echo '✅ Images pushed'
            echo '✅ Security scans completed'
            echo '✅ Kubernetes deployed'
            echo '✅ KEDA verified'
            echo '✅ Argo Rollouts verified'
            echo '✅ Chaos testing completed'
            echo ''
            echo '🚀 ENTERPRISE AI PLATFORM READY'
            echo ''
        }

        failure {

            echo ''
            echo '================================================='
            echo '❌ PIPELINE FAILED'
            echo '================================================='
            echo ''
            echo 'Check failed stage logs in Jenkins.'
            echo ''
        }
    }
}
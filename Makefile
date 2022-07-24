deploy:
	gcloud functins deploy ${FUNCTION_NAME} \
		--runtime python310 \
		--trigger-http \
		--entry-point main \
		--region asia-northeast1 \
		--project=${PROJECT_ID}
		--env-vars-file .env.yaml

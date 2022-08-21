include .env

deploy:
	gcloud functions deploy ${FUNCTION_NAME} \
		--runtime python310 \
		--trigger-http \
		--entry-point main \
		--region asia-northeast1 \
		--project ${PROJECT_ID}

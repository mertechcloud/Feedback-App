!#/bin/bash




STACK_NAME="feedback-app"


REGION="ca-central-1"


Template= "Presigned-S3-URL of the template file from S3"


Email="Example@gmail.com"



aws cloudformation create-stack \


    --stack-name $STACK_NAME \


    --template-url templates \


    --parameters ParameterKey=AdminEmail,ParameterValue=$EMAIL \


    --capabilities CAPABILITY_NAMED_IAM \


    --region $REGION

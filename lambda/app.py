import boto3
import urllib.request
import os
import csv
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    codedeploy = boto3.client('codedeploy')

    endpoint = os.environ['ENDPOINT']
    bucket = os.environ['BUCKET']
    file = os.environ['FILEPATH']
    perc_min = os.environ['ACCEPTANCE_THRESHOLD']
    
    count_200 = 0
    count_err = 0
    
    code = 0
    url = f"http://{endpoint}"
    
    try:
        request = urllib.request.urlopen(url)
        code = request.code
        if code == 200:
            count_200 = count_200 + 1
        else:
            count_err = count_err + 1
    except:
        count_err = count_err + 1
    if code == 0:
        logger.info(url+" Error")
    else:
        logger.info(url+" "+str(code))

    status = 'Failed'
    perc_200=(int((count_200/(count_200+count_err))*100))
    logger.info("HTTP 200 response percentage: ")
    logger.info(perc_200)
    if perc_200 > int(perc_min):
        status = "Succeeded"
    
    logger.info("TEST RESULT: ")
    logger.info(status)
        
    codedeploy.put_lifecycle_event_hook_execution_status(
        deploymentId=event["DeploymentId"],            
        lifecycleEventHookExecutionId=event["LifecycleEventHookExecutionId"],
        status=status
    )
    return True
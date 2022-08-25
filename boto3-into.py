import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def send_voice_message(
        sms_voice_client, origination_number, destination_number,
        language_code, voice_id, ssml_message):
    try:
        response = sms_voice_client.send_voice_message(
            DestinationPhoneNumber=destination_number,
            OriginationPhoneNumber=origination_number,
            Content={
                'SSMLMessage': {
                    'LanguageCode': language_code,
                    'VoiceId': voice_id,
                    'Text': ssml_message}})
    except ClientError:
        logger.exception(
            "Couldn't send message from %s to %s.", origination_number, destination_number)
        raise
    else:
        return response['MessageId']


def main():
    origination_number = "+19134045753"
    # caller_id = "+12065550199"
    destination_number = "+917488965940"
    language_code = "en-US"
    voice_id = "Matthew"
    ssml_message = (
        "<speak>"
        "This is a test message sent from <emphasis>Amazon Pinpoint</emphasis> "
        "using the <break strength='weak'/>AWS SDK for Python (Boto3). "
        "<amazon:effect phonation='soft'>Thank you for listening."
        "</amazon:effect>"
        "</speak>")
    print(f"Sending voice message from {origination_number} to {destination_number}.")
    message_id = send_voice_message(
        boto3.client('pinpoint-sms-voice'), origination_number,destination_number, language_code, voice_id, ssml_message)
    print(f"Message sent!\nMessage ID: {message_id}")


if __name__ == '__main__':
    main()
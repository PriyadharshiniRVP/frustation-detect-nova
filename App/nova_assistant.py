import boto3
import json

# Bedrock client
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)


def ask_ai(prompt):

    try:

        body = {
            "messages": [
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ]
        }

        response = bedrock.invoke_model(
            modelId="global.amazon.nova-2-lite-v1:0",   
            body=json.dumps(body),
            contentType="application/json"
        )

        result = json.loads(response["body"].read())

        answer = result["output"]["message"]["content"][0]["text"]

        return answer.strip()

    except Exception as e:
        print("Nova AI unavailable:", e)
        return "Hey 👋 take a breath. Try isolating the bug step-by-step. You've got this."


def debugging_assistant(problem):

    prompt = f"""
You are CodeBuddy, a friendly AI coding assistant helping a frustrated developer.

Problem:
{problem}

Give:
• 1 short explanation
• 1 debugging suggestion
• 1 encouragement message

Keep the answer under 4 lines.
"""

    return ask_ai(prompt)
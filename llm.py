import requests
from config import credentials
import utime
from machine import Pin
import time

LED = Pin(2, Pin.OUT)

api_key = credentials.get("GROQ_API_KEY")

def invoke_llm(user_message, api_key):
    prompt_template = """You are a helpful AI. Follow these rules,
                            1. If query is realted to following tools, respond with the exact tool name and one exact parameter only:
                            [move(left, right, forward, backword): "move car left, right, forward, or backword",
                            light(on, off): "turn the light on or off",
                            stop(None): "stop the car"]
                            2. Otherwise, respond with the exact answer to the user's query for 10 years old child under 50 words.
                            User: {user_message}"""
    formatted_prompt = prompt_template.format(user_message=user_message)
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "messages": [{"role": "user", "content": f"{formatted_prompt}"}],
        "model": "llama3-70b-8192"
    }
    
    try:
        start_time = utime.ticks_ms()
        response = requests.post(url, headers=headers, json=payload)
        elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

        # print(f"Response Code: {response.status_code}")  # Print response code
        # print(f"Response Text: {response.text}")  # Print raw response text

        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content'].lower()
            if "move" in content:
                if "left" in content:
                    return "turning left"
                elif "right" in content:
                    return "turning left"
                elif "forward" in content:
                    return "moving forward"
                elif "backword" in content:
                    return "moving backword"
                else:
                    return content
            elif "light" in content:
                if "on" in content:
                    LED.value(1)
                    return "light turned on"
                elif "off" in content:
                    LED.value(0)
                    return "light turned off"
                else:
                    return content

            elif "stop" in content:
                return "car stoped"
            else:
                return content
        else:
            raise Exception(f"API error ({response.status_code}): {response.reason}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    prompt1 = "Tell me about machine Learning"
    prompt2 = "move car forward"
    prompt3 = "illuminate the place with light"
    prompt4 = "turn off light"
    prompt5 = "turn on speaker"
    prompt6 = "turn off speaker"
    
    response = invoke_llm(prompt1, api_key)
    print(response)
    time.sleep(5)
    response = invoke_llm(prompt2, api_key)
    print(response)

from gradio_client import Client
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

messages = list()

def amazigh_stt(audio_path: str):
    client = Client("https://ayymen-mms-asr.hf.space/")
    result = client.predict(
				audio_path,
                audio_path,
				"Tachelhit (shi)", 
				api_name="/predict"
    )
    return result

def amazigh_tts(text: str):
    client = Client("https://ayymen-amazigh-tts.hf.space/")
    result = client.predict(
				text,
				"Tachelhit",
				api_name="/predict"
    )
    os.replace(result, "./audio.wav")
    return "./audio.wav"


def create_message(role: str, content: str):
    return {"role": role,
            "content": content}

def translate(src: str, src_type:str , dest:str, text:str):
    global messages

    if src=='Tachelhit' and src_type=='speech':
        text=amazigh_stt(text)
    

    translation_prompt = f'''Translate me this english text to the {dest} language.
                        The text I will give you to translate is in {src}.
                        I want you to return only the translation. Don't say anything else.
                        I want the translation to be very accurate.'''

    
    messages.append(create_message("system", translation_prompt))

    try:
        
        messages.append(create_message('user', text))
        completion_response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            messages=messages,
            temperature=1
        )

        translated = completion_response.choices[0].message.content
    
        return translated
    
    except Exception as e:
        print("There is an exception in translating the text:\n"+str(e))

def amazigh_resp(text: str):
    global messages
    resp_prompt = '''Your next response should be in Amazigh Tachelhit language.
                    Your response should be written in the Amazigh Tachelhit language.
                    Do not include any word not in Amazigh Tachelhit'''
    
    messages.append(create_message('system', resp_prompt))
    messages.append(create_message('user', text))

    tachelhit_response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            messages=messages,
            temperature=1
    )

    tachelhit_resp = tachelhit_response.choices[0].message.content

    return tachelhit_resp


def amazigh_chatbot(req: str, req_type:str):
    if req_type=='speech':
        text_amazigh_req = amazigh_stt(req)
    
    else:
        text_amazigh_req = req


    text_tachelhit_resp = amazigh_resp(text_amazigh_req)
    audio_tachelhit_resp_path = amazigh_tts(text_tachelhit_resp)

    return audio_tachelhit_resp_path, text_tachelhit_resp
    
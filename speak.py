# -*- coding: utf-8 -*-
import openai
import pygame
import os
import speech_recognition as sr
from gtts import gTTS
import time

# Replace with your GPT-3 API key
openai.api_key = "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"

def generate_gpt3_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()#GPT-3生成的第一个响应文本的字符串返回，并去除开头和结尾的空白字符。

def speak(text, language="zh-cn"):
    tts = gTTS(text=text, lang=language)
    tts.save("response.mp3")

    pygame.mixer.init()#初始化pygame.mixer模块
    pygame.mixer.music.load("response.mp3")#方法加载response.mp3音频文件
    pygame.mixer.music.play()#播放该音频文件

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)#当音频正在播放时，pygame.mixer.music.get_busy()方法将返回True，while循环会不断调用tick()方法等待音频播放完毕。

    # 等待 3 秒，确保文件不再被占用
    time.sleep(3)

    os.remove("response.mp3")

def recognize_speech(retries=3):
    recognizer = sr.Recognizer()
    for _ in range(retries):#默认尝试3次麦克风识别
        with sr.Microphone() as source:#打开麦克风
            print("请说话...")
            audio = recognizer.listen(source)#Recognizer对象监听来自麦克风的语音输入，并将其存储在audio变量中以备后续的语音识别

        try:
            text = recognizer.recognize_google(audio, language="zh-CN")#将存储在audio变量中的语音转换为文本
            print(f"你说的是: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition 无法识别语音")
        except sr.RequestError as e:
            print(f"无法从 Google 语音识别服务请求结果; {e}")

    return None

def aispeak():
    while True:
        spoken_command = recognize_speech()

        if spoken_command is not None:
            # Get a keyword from the spoken command and translate it to English
            keyword_prompt = f"从 \"{spoken_command}\" 中提取一个关键词并翻译成英文"
            keyword = generate_gpt3_response(keyword_prompt)
            print(f"Keyword: {keyword}")

            if keyword.lower() == "joke":
                joke_pormpt = f"请用中文给我讲一个笑话"
                joke = generate_gpt3_response(joke_pormpt)
                speak(joke)
            elif keyword.lower() == "song":
                if "猜猜" in spoken_command:
                    guess_prompt = f"猜猜我最喜欢的歌曲"
                    guess = generate_gpt3_response(guess_prompt)
                    speak(guess)
                else:
                    song_prompt = f"请告诉我今年的十大热门歌曲"
                    top_song = generate_gpt3_response(song_prompt)
                    speak(top_song)
            elif "小车" in spoken_command:
                response_prompt = f"请根据 \"{spoken_command}\" 生成一个合适的回复"
                response = generate_gpt3_response(response_prompt)
                speak(response)
            
            else:
                if "相关" in spoken_command:
                    content_prompt = f"请根据关键词\"{keyword}\" 生成一段有关的内容"
                    content = generate_gpt3_response(content_prompt)
                    speak(content)
                else:
                    modified_response = f"我在找{keyword}快让我看看 "
                    speak(modified_response)
                    return keyword

        # 暂停 5 秒
        time.sleep(5)

if __name__ == "__main__":
    result=aispeak()
    print(f"Returned: {result}")
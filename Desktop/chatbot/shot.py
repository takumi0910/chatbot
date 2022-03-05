{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "44ec53b5-b3c4-46eb-84f9-6dc0c4916cc0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: line-bot-sdk in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (2.1.0)\n",
      "Requirement already satisfied: future in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from line-bot-sdk) (0.18.2)\n",
      "Requirement already satisfied: aiohttp>=3.7.4 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from line-bot-sdk) (3.8.1)\n",
      "Requirement already satisfied: requests>=2.0 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from line-bot-sdk) (2.27.1)\n",
      "Requirement already satisfied: typing-extensions>=3.7.4 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from aiohttp>=3.7.4->line-bot-sdk) (4.1.1)\n",
      "Requirement already satisfied: asynctest==0.13.0 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from aiohttp>=3.7.4->line-bot-sdk) (0.13.0)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from aiohttp>=3.7.4->line-bot-sdk) (1.2.0)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from aiohttp>=3.7.4->line-bot-sdk) (21.4.0)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from aiohttp>=3.7.4->line-bot-sdk) (1.2.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from aiohttp>=3.7.4->line-bot-sdk) (5.2.0)\n",
      "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from aiohttp>=3.7.4->line-bot-sdk) (4.0.2)\n",
      "Requirement already satisfied: charset-normalizer<3.0,>=2.0 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from aiohttp>=3.7.4->line-bot-sdk) (2.0.12)\n",
      "Requirement already satisfied: idna-ssl>=1.0 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from aiohttp>=3.7.4->line-bot-sdk) (1.1.0)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from aiohttp>=3.7.4->line-bot-sdk) (1.7.2)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from requests>=2.0->line-bot-sdk) (1.26.8)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from requests>=2.0->line-bot-sdk) (2021.10.8)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\takumi\\appdata\\local\\programs\\python\\python36\\lib\\site-packages (from requests>=2.0->line-bot-sdk) (3.3)\n"
     ]
    }
   ],
   "source": [
    "!pip install line-bot-sdk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9cbba0f8-4bf3-45e7-967a-bb977bdceca9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0c814042-24f1-4819-a657-e15f9b4c30f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "file = open('info.json', 'r')\n",
    "info = json.load(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b83d9072-22a5-47b9-b583-0588d89e50de",
   "metadata": {},
   "outputs": [],
   "source": [
    "# info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f0bb12d8-0d45-41f0-9c6d-67cab25d3f62",
   "metadata": {},
   "outputs": [],
   "source": [
    "from linebot import LineBotApi\n",
    "from linebot.models import TextSendMessage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3386fb2f-acea-4016-8c82-2b0c82b508dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']\n",
    "line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7e149f8a-ce4a-41c3-aa19-1f70d187779b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    USER_ID = info['USER_ID']\n",
    "    messages = TextSendMessage(text=\"おはよう\")\n",
    "    line_bot_api.push_message(USER_ID, messages=messages)\n",
    "      \n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce2f9987-d503-4fa7-a4e0-469b5a561290",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

from instagram import main as instagram_main
from chatAPI import main as chat_main
from tiktok import main as tiktok_main

def main():
    # TODO need to change filedir to include extra backslahes or will run into issues with parsing
    # fileDir = input("What is the directory to the files you wish to upload: \n")
    # api_key = input("Enter your openAI api key: \n")
    # instaUsername = input("What is your instagram username: \n")
    # instaPassword = input("What is your instagram password: \n")

    # instagram_main(fileDir,api_key,instaUsername,instaPassword)
    tiktok_main()
    

main()
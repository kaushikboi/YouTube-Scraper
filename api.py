import os
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"
    
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = 'AIzaSyBQtrFOwz0OIiIn9wT6j4sanwq_K78aoFo')

    request = youtube.search().list(
        part="snippet",
        maxResults=2,
        q="surfing"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
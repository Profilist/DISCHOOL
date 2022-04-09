import json
import os.path
import discord
from discord.ext import commands
# import requests
# import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# from google.oauth2 import service_account

class Classroom(commands.Cog, name='commands'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def classroom(self, ctx: commands.Context):
        """Extracts Google Classroom assignments"""

        SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly', 'https://www.googleapis.com/auth/classroom.coursework.students']
        creds = None

        # credentials = service_account.Credentials.from_service_account_file(
        #     '/Users/Larris Xie/PycharmProjects/DISCHOOL/commands/classroom/services.json',
        #     scopes=['https://www.googleapis.com/auth/classroom.courses.readonly', 'https://www.googleapis.com/auth/classroom.coursework.students.readonly'],
        # )
        # bearer_token = credentials.token

        if os.path.exists('token.json'):
            # print("exists")
            creds = Credentials.from_authorized_user_file('token.json', scopes=SCOPES)
        if not creds or not creds.valid:
            # print("invalid uh oh")
            if creds and creds.expired and creds.refresh_token:
                # print("1st")
                creds.refresh(Request())
            else:
                # print("2nd")
                flow = InstalledAppFlow.from_client_secrets_file(
                    '/Users/Larris Xie/PycharmProjects/DISCHOOL/commands/classroom/credentials.json', scopes=SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                # print("3rd")
                token.write(creds.to_json())

        try:
            service = build('classroom', 'v1', credentials=creds)

            results = service.courses().list(pageSize=10).execute()
            courses = results.get('courses', [])

            if not courses:
                print('No courses found.')
            else:
                temp = {}
                for course in courses:
                    temp[course['name']] = course['alternateLink']

        except HttpError as error:
            print('An error occurred: %s' % error)

        results = service.courses().list(pageSize=10).execute()
        courses = results.get('courses', [])

        # if not courses:
        #     print('No courses found.')
        # else:
        #     print('Courses:')
        #     for course in courses:
        #         print(course['name'])
        #         print(course['id'])

        # print(courses[0]['id'])
        courseworkList = service.courses().courseWork().list(courseId=int(courses[0]['id'])).execute()
        for coursework in courseworkList["courseWork"]:
            # print(coursework)
            embed = discord.Embed(url=coursework['alternateLink'], title=coursework['title'], description=coursework['description'], color=0x20A464)
            if('material' in json.dumps(coursework)):
                embed.add_field(name='Attachments', value=coursework['materials'][0]['driveFile']['driveFile']['title']+'\n'+coursework['materials'][0]['driveFile']['driveFile']['alternateLink'], inline=False)
            embed.set_author(name='Larris Xie', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Eo_circle_pink_letter-l.svg/1024px-Eo_circle_pink_letter-l.svg.png')
            embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Google_Classroom_icon.svg/1200px-Google_Classroom_icon.svg.png')
            embed.set_footer(text=('Due date: '+str(coursework['dueDate']['year'])+'/0'+str(coursework['dueDate']['month'])+'/'+str(coursework['dueDate']['day'])), icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Google_Calendar_icon_%282020%29.svg/1024px-Google_Calendar_icon_%282020%29.svg.png')

            channel_id = 962414470930522112
            channel = ctx.bot.get_channel(channel_id)
            await channel.send("Larris Xie posted an assignment in "+courses[0]['name'])
            await channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Classroom(bot))
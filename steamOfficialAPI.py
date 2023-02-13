SERVICE_KEY = "8E86A6E9063B0A6C07376958AB45FC38"
SAMPLE_STEAM_ID = "76561198995229738"

from steam.webapi import WebAPI

def init():
    api = WebAPI(key=SERVICE_KEY)

def get_server_info():
    api.call('ISteamWebAPIUtil.GetServerInfo')

def get_steamID_info():
    api.call('ISteamUser.GetPlayerSummaries',steamids=SAMPLE_STEAM_ID)

def get_user_stat():
    api.call('ISteamUserStats.GetUserStatsForGame',steamid=SAMPLE_STEAM_ID, appid=1621690)


def get_all_game_list():
    api.call('ISteamApps.GetAppList')

    
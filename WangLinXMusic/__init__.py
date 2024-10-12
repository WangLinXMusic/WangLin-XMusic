from WangLinXMusic.core.bot import Hotty
from WangLinXMusic.core.dir import dirr
from WangLinXMusic.core.git import git
from WangLinXMusic.core.userbot import Userbot
from WangLinXMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "BRANDED_KUDI_BOT"  # connect music api key "Dont change it"

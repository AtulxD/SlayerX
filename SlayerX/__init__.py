from SlayerX.core.bot import Slayer
from SlayerX.core.dir import dirr
from SlayerX.core.git import git
from SlayerX.core.userbot import Userbot
from SlayerX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Slayer()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

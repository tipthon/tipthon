import re
import time
from datetime import datetime
from Arab import StartTime, iqthon
from Arab.Config import Config
from Arab.plugins import mention
help1 = ("**☭⦙ كيفيه التنصيب :**")
help2 = ("**☭⦙ قـائمـه الاوامـر :**\n**☭⦙ قنـاه السـورس :** @E9N99\n**☭⦙ شـرح اوامـر السـورس : @a_aaaf**\n**☭⦙ شـرح فـارات السـورس : @aa_aaf** ")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**.𓄌 : version 7.5  𓇡.** \n.𓄌 : me  {mention}  𓇡. \n**.𓄌 : time  {TM}  𓇡.**\n**.𓄌 : My Bot {TG_BOT} 𓇡.**\n**.𓄌 : Source : @E9N99  𓇡.**"

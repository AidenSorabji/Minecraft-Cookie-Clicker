import osascript
import os
title = "Success"
message = "File downloaded"
command = f'''
osascript -e 'display notification "{message}" with title "{title}"'
'''
os.system(command)

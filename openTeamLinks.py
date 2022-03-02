"""
自动打开常用的计划 Links

Version: 0.1
Author: 黄华智
"""

import os
# 需要打开的 tabs
tabs_list = [
  # Jupiter Release Schedule 
  # 'https://docs.google.com/spreadsheets/d/1cl10AHmQ1QwZGdQkEe3n0gCwwx8icsu1hMATs0hR93w/edit#gid=540016998',
  'https://docs.google.com/spreadsheets/d/1cl10AHmQ1QwZGdQkEe3n0gCwwx8icsu1hMATs0hR93w/edit#gid=2123718530',

  # OVERALL ScrumBoard
  # 'https://jira.ringcentral.com/secure/RapidBoard.jspa?rapidView=4869&view=detail&selectedIssue=FIJI-30516&sprint=16646&quickFilter=16142',
  # # Titan wishlist
  # 'https://docs.google.com/spreadsheets/d/11UCFueGUcgi4sqaCLmVmRaliLI1Ay2u2MXoywWXlnDs/edit#gid=1508044272',
  # # Titan dashboard
  # 'https://jira.ringcentral.com/secure/Dashboard.jspa?selectPageId=25460',

  # Application Phone Team Task Planning
  'https://docs.google.com/spreadsheets/d/1fRQfkm5lr_e4s8oDVXYss4nSBzDiKA6-QtJoT26pTZA/edit#gid=2008159245',

  # Phone ScrumBoard
  'https://jira.ringcentral.com/secure/RapidBoard.jspa?rapidView=5429&selectedIssue=FIJI-46626&sprint=18894&quickFilter=19373',

  # AHA - Jupiter Phone Feature list 
  # 'https://ringcentral.aha.io/bookmarks/feature_grids/7065107510977201830/7070411801200672071',
  'https://ringcentral.aha.io/bookmarks/feature_grids/7065107510977201830/7070412117513104192',

  # Feature owners
  'https://docs.google.com/spreadsheets/d/1s8dwjO7dIg0VfZV4BAA2qO1SRrRBBPlfDeC-6QsZMpo',
]
# -n opens a new instance of an application. Google Chrome detects this and remedies the situation by closing the new instance and passing the tab’s location to the first instance, but this is necessary to force arguments to be read.
# --args indicates what's to follow are arguments to be passed to Google Chrome, not open.
# --new-window is a Google Chrome argument to force a new window to be created.
os.system('open -na "Google Chrome" --args --new-window ' + ' '.join(tabs_list))
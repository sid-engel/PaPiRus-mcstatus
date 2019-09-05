# Created by Sid Engel. Free to use and play with!

from mcstatus import MinecraftServer
from papirus import PapirusTextPos
from time import sleep

# Options
server = MinecraftServer.lookup("ottercraft.net:25565")
timer = 15

# Initial Screen Draw
status = server.status()
text = PapirusTextPos()
text.AddText("= OtterCraft =", 5, 10, Id="Title")
text.AddText(str(status.latency) + "ms", 5, 32, Id="Ping")
text.AddText(str(status.players.online) + " players", 5, 54, Id="Count")
print("Initial Query + Screen Drawing Complete!")
loopStat = True
loopCount = 1
failedCount = 0

while loopStat:
  try:
    # Board Stat Updates
    status = server.status()
    text.UpdateText("Ping", str(status.latency) + "ms")
    text.UpdateText("Count", str(status.players.online) + " players")
    print("=================")
    print("Ping = " + str(status.latency))
    print("Players = " + str(status.players.online))
    print("Loop Count: " + str(loopCount))
    print("Failed Loop Count: " + str(failedCount))
    print("=================")
    loopCount = loopCount + 1
    sleep(timer)
  except:
    # Failed!
    failedCount = failedCount + 1
    text.UpdateText("Ping", str(0) + "ms")
    text.UpdateText("Count", "FAILED" + " players")
    print("=================")
    print("FAILED TO GET STATUS! Likely bad connection, retrying in 15 seconds...")
    print("Loop Count: " + str(loopCount))
    print("Failed Loop Count: " + str(failedCount))
    print("=================")
    sleep(timer)

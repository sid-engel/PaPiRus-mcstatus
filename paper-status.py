from mcstatus import MinecraftServer
from papirus import PapirusTextPos
from time import sleep

server = MinecraftServer.lookup("ottercraft.net:25565")
text = PapirusTextPos()
status = server.status()

# Initial Screen Draw
text.AddText("= OtterCraft =", 5, 10, Id="Title")
text.AddText(str(status.latency) + "ms", 5, 32, Id="Ping")
text.AddText(str(status.players.online) + " players", 5, 54, Id="Count")

loopStat = True
while loopStat:
  # Board Stat Updates
  status = server.status()
  text.UpdateText("Ping", str(status.latency) + "ms")
  text.UpdateText("Count", str(status.players.online) + " players")

# CLEAR THE BOARD, AND REPEAT LOOP
  sleep(15)

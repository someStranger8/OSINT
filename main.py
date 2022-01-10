
import twint

# banner
print("")
print(" |_   _|_ __ _(_) |_| |_ ___ _ _   / _ \/ __|_ _| \| |_   _|")
print("   | | \ V  V / |  _|  _/ -_) '_| | (_) \__ \| || .` | | |  ")
print("   |_|  \_/\_/|_|\__|\__\___|_|    \___/|___/___|_|\_| |_|  ")
print("")

# varibles
to = sys.argv[1]
kw = sys.argv[2]

# search
c = twint.Config()
c.Username = to
c.Search = kw
twint.run.Search(c)

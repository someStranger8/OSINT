import twint
print(" |_   _|_ __ _(_) |_| |_ ___ _ _   / _ \/ __|_ _| \| |_   _|")
print("   | | \ V  V / |  _|  _/ -_) '_| | (_) \__ \| || .` | | |  ")
print("   |_|  \_/\_/|_|\__|\__\___|_|    \___/|___/___|_|\_| |_|  ")
print("")
to=input("[*] enter username: ")
kw=input("[*] enter keyword: ")
c = twint.Config()
c.Username = to
c.Search = kw
twint.run.Search(c)

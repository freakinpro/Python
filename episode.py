user_input = input();
length = len(user_input)
s = user_input.find("_")
season = user_input[0: s]
slen = len(season)
seasonNum = season[1: slen]
e = user_input.find("_", s + 1)
episode = user_input[s + 1: e]
eplen = len(episode)
episodeNum = episode[1: eplen]
epName = user_input[e + 1: length]

print(f"Season {seasonNum}, Episode {episodeNum}: {epName} (The Simpsons)")
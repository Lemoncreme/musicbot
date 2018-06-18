import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pylast
import youtubemp3
import giphypop
import pydub

credentials = SpotifyClientCredentials(
	"08900fa0e9bb4fa5bbf4bf0ecbb1ab2e", "4b30100a2e6840b09e5988f4b15b4bd8")

def main():
	sp = spotipy.Spotify(client_credentials_manager=credentials)
	tracks = sp.user_playlist(
		"lemoncreme", "7uMpszsJUhANmeclkiaulK")["tracks"]["items"]
	#print([track["track"] for track in tracks])
	tags = []
	for track in tracks:
		print(track["track"]["name"])
		tags.extend([artist["name"] for artist in track["track"]["artists"]])
		tags.extend(sp.artist(track["track"]["artists"][0]["uri"])["genres"])
		print(tags)
		tags.clear()

if __name__ == "__main__":
	main()

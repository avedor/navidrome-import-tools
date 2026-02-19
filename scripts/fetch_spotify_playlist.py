import csv
import json

from spotify_client import (
    extract_playlist_id,
    fetch_playlist_tracks,
    get_spotify_client,
)

# Put your playlist ID or URL here
PLAYLIST_ID = "3cXFWPgBhhMy3k2z8HXama"

sp = get_spotify_client()
playlist_id = extract_playlist_id(PLAYLIST_ID)
playlist_name, playlist_tracks = fetch_playlist_tracks(sp, playlist_id)

print(f"Playlist: {playlist_name}")

# Save to JSON
with open("playlist_tracks.json", "w", encoding="utf-8") as f:
    json.dump(playlist_tracks, f, ensure_ascii=False, indent=2)
print("Exported playlist songs to playlist_tracks.json")

# Save to CSV
if playlist_tracks:
    keys = playlist_tracks[0].keys()
    with open("playlist_tracks.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(playlist_tracks)
    print("Exported playlist songs to playlist_tracks.csv")
else:
    print("No tracks found to export.")

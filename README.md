# EditYoutubeMusicPlaylists
**I recently had to clean up a huge playlist (with over 4,000 songs in it).
The Youtubemusic GUI doesn't work for such large playlists.  Luckily, I found a cool
API for it (https://github.com/sigma67/ytmusicapi).**

***NOTE:* Requires file "headers_auth.json" in program folder.  It contains some headers including your
session cookie.  Format:**

`
{
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json",
    "X-Goog-AuthUser": "0",
    "x-origin": "https://music.youtube.com",
    "Cookie" : "<PASTE YOUR COOKIE HERE>"
}
`

I've implemented functions to work with playlists, and will be adding more functionality later.
For now, just call the functions from the program.

* function "samplePl()" - 
add sample playlist with 1 track

* function "getPlaylists(w)" - 
get playlists.  if w = 1, write to file

* function "deletePl(plId)" - 
Delete Playlists

* function "addTrack(plId, songTitle)" - 
pass in playlistID and songTitle to add

* function "deleteTrackByTitle(plId, songTitle)" - 
pass in playlistID and songTitle to delete

* function "deleteTracksByArtist(plId, artistName)" - 
 pass in playlistID and Artist Name to delete.
 WARNING: Deletes all songs by that artist in the playlist.

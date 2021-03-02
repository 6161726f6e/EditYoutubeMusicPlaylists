# EditYoutubeMusicPlaylists
**I recently had to clean up a huge playlist (with over 4,000 songs in it).

The Youtubemusic GUI doesn't work for such large playlists.  Luckily, I found a cool API for it (https://github.com/sigma67/ytmusicapi).  

This program allows managing your music library (see full list of options below).  I mostly use this app now to manage my playlists.  It makes many tasks much easier, such as deleting a song from large playlist, liking all songs in a playlist, listing all songs in a playlist, deleting all songs by an artist from a playlist, deleting/adding a list of songs, auto-liking songs when adding them to a playlist, deleting songs with partially matching song titles, etc.**

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
get playlists.  if w = 1, write to file.

* function "getPlaylistTracks(plName)" - 
pass in name of a Playlist to list all tracks, artists, and track count.

* function "getPlaylistId(plName)" - 
pass in name of Playlist to get the ID so can edit it. 

* function "deletePl(plId)" - 
Deletes Playlist with playlistId.

* function "addTracks(plId, songTitles)" - 
pass in playlistID and songTitles (as list) to add.

* function "addAlbumToPl(plId, albumString)" - 
pass in playlistId and album search string to add all songs from that album to a Playlist.

* function "addPl2PL(plFrom, plTo)" - 
add all songs from a public source playlist to your library playlist.
pass in args as strings.

* function "deleteTrackByTitle(plId, songTitle)" - 
pass in playlistID and songTitle to delete.

* function "deleteTracksByArtist(plId, artistName)" - 
pass in playlistID and Artist Name to delete.
WARNING: Deletes all songs by that artist in the playlist.

* function "likeTracks([songTitles])" - 
pass in list of songs to like (thumbs up).

* function "likeAllTracks(pl)" - 
pass in playlist name to like (thumbs up) all tracks in it.


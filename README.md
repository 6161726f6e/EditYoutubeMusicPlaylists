# EditYoutubeMusicPlaylists
**I recently had to clean up a huge playlist (with over 4,000 songs in it).
The Youtubemusic GUI doesn't work for such large playlists.  Luckily, I found a cool
API for it (https://github.com/sigma67/ytmusicapi).**

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

# Manage YouTube Music Playlists
# 
# Supported Operations: add playlist and songs, delete playlist, get list of
#    playlists, delete song by title from playlist, delete songs by artist from
#    playlist
#
# Requirements: headers_auth.json file with cookie info
# 
# Author: Aaron Dhiman
# Reference: uses this awesome YTMusic API: https://github.com/sigma67/ytmusicapi
###################################################################################

from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')    #start session

def samplePl():
#add sample playlist with 1 track
	playlistId = ytmusic.create_playlist('HL', 'HL PL')
	search_results = ytmusic.search("Human League Don't You Want Me")
	ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
	return(playlistId)

def getPlaylists(w):
# get playlists.  if w = 1, write to file
	myPlaylistsDict=ytmusic.get_library_playlists(limit=250)
	#print(myPlaylistsDict[0])
	#print(myPlaylistsDict['title'])
	if w==1:
		f = open("playlistIDs.txt", "a")
	for i in myPlaylistsDict:
		print(i['title'], i['playlistId'])
		print("-------------------------")
		if w == 1:
			f.write(i['title'] + "   " + i['playlistId'] + "\n")
			f.write("-------------------------\n")
	if w == 1:
		f.close()

def deletePl(plId):
# Delete Playlists
	ytmusic.delete_playlist(plId)

def addTrack(plId, songTitle):
# pass in playlistID and songTitle to add
	search_results = ytmusic.search("Human League Don't You Want Me")
	ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])

def deleteTrackByTitle(plId, songTitle):
# pass in playlistID and songTitle to delete
	playlist=ytmusic.get_playlist(playlistId=plId, limit=6000)
	for i in playlist["tracks"]:
		if i["title"] == songTitle:
			print(i["videoId"], ": ", i["setVideoId"])
			videoId=i["videoId"]
			setVideoId=i["setVideoId"]
			print("Deleting song ", songTitle)
			ytmusic.remove_playlist_items(playlistId=plId, \
				videos=[i])

def deleteTracksByArtist(plId, artistName):
# pass in playlistID and Artist Name to delete.
# WARNING: Deletes all songs by that artist in the playlist.
	playlist=ytmusic.get_playlist(playlistId=plId, limit=6000)
	for i in playlist["tracks"]:
		for j in i["artists"]:
			#print(j["name"])
			if j["name"] == artistName:
				print(i["videoId"], ": ", i["setVideoId"])
				videoId=i["videoId"]
				setVideoId=i["setVideoId"]
				print("Deleting song ", i["title"], j["name"])
				ytmusic.remove_playlist_items(playlistId=plId, \
					videos=[i])

#newPl=samplePl()
#getPlaylists(0)
#deleteTrackByTitle("PLDmWpptAIZNKIlIjtGZMCQoVhtsj6eKqb", "Don't You Want Me")
deleteTracksByArtist("PLDmWpptAIZNIueD733bERuDqj-dvtIhep", "ELECTRIFY001")
#deleteTracksByArtist("PLDmWpptAIZNL9I5XZq7ETuHw-ycY3vvV9", "The Human League")

#deletePl("PLDmWpptAIZNKIlIjtGZMCQoVhtsj6eKqb")

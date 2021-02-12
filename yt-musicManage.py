# Manage YouTube Music Playlists
# 
# Supported Operations: add playlist and songs, delete playlist, get list of
#    playlists, delete song by title from playlist, delete songs by artist from
#    playlist, get playlistID by name
#
# Requirements: headers_auth.json file with cookie info
# 
# Author: Aaron Dhiman
# Reference: uses this awesome YTMusic API: 
#     https://ytmusicapi.readthedocs.io/en/latest/index.html
###################################################################################

from ytmusicapi import YTMusic

ytmusic = YTMusic("headers_auth.json")    #start session

def samplePl():
#add sample playlist with 1 track
	playlistId = ytmusic.create_playlist("SamplePL", "My Sample PL")
	search_results = ytmusic.search("All the Things Dual Core")
	ytmusic.add_playlist_items(playlistId, [search_results[0]["videoId"]])
	return(playlistId)

def getPlaylists(w):
# get playlists.  if w = 1, write to file
	myPlaylistsDict=ytmusic.get_library_playlists(limit=250)
	#print(myPlaylistsDict[0])
	#print(myPlaylistsDict["title"])
	if w==1:
		f = open("playlistIDs.txt", "a")
	for i in myPlaylistsDict:
		print(i["title"], i["playlistId"])
		print("-------------------------")
		if w == 1:
			f.write(i["title"] + "   " + i["playlistId"] + "\n")
			f.write("-------------------------\n")
	if w == 1:
		f.close()

def getPlaylistId(plName):
# get playlist Id by name.  Then you can edit it.
	myPlaylistsDict=ytmusic.get_library_playlists(limit=250)
	#print(myPlaylistsDict[0])
	#print(myPlaylistsDict["title"])
	for i in myPlaylistsDict:
		if i["title"].lower() == plName.lower():
			print("Getting Playlist ID...")
			print(i["title"], "=",i["playlistId"])
			print("-------------------------")
			return(i["playlistId"])

def deletePl(plId):
# Delete Playlist by ID
	print("Deleting playlist with ID", plId)
	ytmusic.delete_playlist(plId)

def deleteTrackByTitle(plId, songTitle):
# pass in playlistID and songTitle to delete
	playlist=ytmusic.get_playlist(playlistId=plId, limit=6000)
	for i in playlist["tracks"]:
		if i["title"].lower() == songTitle.lower():
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
			if j["name"].lower() == artistName.lower():
				print(i["videoId"], ": ", i["setVideoId"])
				videoId=i["videoId"]
				setVideoId=i["setVideoId"]
				print("Deleting song \"", i["title"], j["name"],"\"")
				ytmusic.remove_playlist_items(playlistId=plId, \
					videos=[i])

def addTracks(plId, songTitle):
# pass in playlistID and songTitles (as list) to add
	for i in songTitle:
		search_results = ytmusic.search(i)
		print("Adding song:", i)
		ytmusic.add_playlist_items(plId, [search_results[0]["videoId"]])

def addAlbumToPl(plId, albumString):
	search_results = ytmusic.search(query=albumString, filter="albums")
	print(search_results[0])
	browseID=search_results[0]["browseId"]
	print("found album named ",search_results[0]["title"])
	print("browseId = ",browseID)
	search_results = ytmusic.get_album(browseID)
	print("Tracks on Album = ", search_results["trackCount"])
	for i in search_results["tracks"]:
		print("Adding song:", i["title"])
		#print("videoID = ", i["videoId"])
		ytmusic.add_playlist_items(plId, [i["videoId"]])

######## Get list of all your PLs
#getPlaylists(0)

######## Create new Pl or edit existing one
#pl2edit=samplePl()
pl2edit=getPlaylistId("pr0Gr4mm1ng")

######## Add entire album to PL
#addAlbumToPl(pl2edit,"the prodigy charly")

######## Add tracks to PL
addTracks(pl2edit, ["the prodigy break & enter", "the prodigy thunder", "the prodigy one love"])

######## Delete tracks from PL
#deleteTracksByArtist(pl2edit, "dUAl cORe")
#deleteTrackByTitle(pl2edit, "aLl thE tHingS")

######## Delete entire PL
#deletePl(pl2edit)

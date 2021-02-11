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

ytmusic = YTMusic('headers_auth.json')    #start session

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
	#print(myPlaylistsDict['title'])
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
# get playlist ID by name.  Then you can edit it.
	myPlaylistsDict=ytmusic.get_library_playlists(limit=250)
	#print(myPlaylistsDict[0])
	#print(myPlaylistsDict['title'])
	for i in myPlaylistsDict:
		if i["title"].lower() == plName.lower():
			print("Getting Playlist ID...")
			print(i["title"], "=",i['playlistId'])
			print("-------------------------")
			return(i['playlistId'])

def deletePl(plId):
# Delete Playlist by ID
	print("Deleting playlist with ID", plId)
	ytmusic.delete_playlist(plId)

def addTrack(plId, songTitle):
# pass in playlistID and songTitle to add
	search_results = ytmusic.search(songTitle)
	print("Adding song ", songTitle)
	ytmusic.add_playlist_items(plId, [search_results[0]['videoId']])

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
				print("Deleting song ", i["title"], j["name"])
				ytmusic.remove_playlist_items(playlistId=plId, \
					videos=[i])


## Get list of all your PLs
#getPlaylists(0)

## Create new Pl or edit existing one
#pl2edit=samplePl()
pl2edit=getPlaylistId("pr0Gr4mm1ng")

## Add tracks to PL
#addTrack(pl2edit, "Breathe Prodigy")
#addTrack(pl2edit, "Elysian Feels The Future Sound Of London")
#addTrack(pl2edit, "Fortune Days The Glitch Mob")
#addTrack(pl2edit, "Papua New Guinea The Future Sound of London")
#addTrack(pl2edit, "Obsidian (feat. Jennifer Folker) Banco de Gaia")
#addTrack(pl2edit, "True Grit The Crystal Method")
#addTrack(pl2edit, "Xinobi Day Off Anoraak Remix")
#addTrack(pl2edit, "I Remember (Vocal Mix) deadmau5")
#addTrack(pl2edit, "strobe deadmau5")
#addTrack(pl2edit, "Ghosts 'n' Stuff (feat. Rob Swire) deadmau5")
#addTrack(pl2edit, "monophobia deadmau5")
#addTrack(pl2edit, "raise your weapon deadmau5")
#addTrack(pl2edit, "Keep Hope Alive (Trip Hope mix) The Crystal Method")

## Delete tracks from PL
#deleteTrackByTitle(pl2edit, "Keep It Clean (Original Mix)")
#deleteTracksByArtist(pl2edit, "Dual Core")

## Delete entire PL
#deletePl(pl2edit)

package room

import "github.com/pion/webrtc/v2"

var rooms []Room

type Room struct {
	Id                string
	Available         bool
	PeerConnectionMap map[string]chan *webrtc.Track
}

func New(id string) Room {
	room := Room{
		Id:                id,
		Available:         true,
		PeerConnectionMap: make(map[string]chan *webrtc.Track),
	}

	rooms = append(rooms, room)

	return room
}

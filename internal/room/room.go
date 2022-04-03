package room

import (
	"fmt"

	"github.com/pion/webrtc/v2"
)

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

func Find(id string) (*Room, error) {
	for _, room := range rooms {
		if room.Id == id && room.Available {
			return &room, nil
		}
	}

	return nil, fmt.Errorf("room not found: %v", id)
}

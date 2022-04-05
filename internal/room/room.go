package room

import (
	"fmt"

	"github.com/pion/webrtc/v2"
)

var rooms []Room

type Room struct {
	Id                string
	Available         bool
	Admin             string
	PeerConnectionMap map[string]chan *webrtc.Track
}

func New(id string, admin string) Room {
	room := Room{
		Id:                id,
		Available:         true,
		Admin:             admin,
		PeerConnectionMap: make(map[string]chan *webrtc.Track),
	}

	rooms = append(rooms, room)

	return room
}

func All() []string {
	var ids []string

	for _, room := range rooms {
		ids = append(ids, room.Id)
	}

	return ids
}

func Find(id string) (*Room, error) {
	for _, room := range rooms {
		if room.Id == id && room.Available {
			return &room, nil
		}
	}

	return nil, fmt.Errorf("room not found: %v", id)
}

func Close(id string, admin string) {
	for _, room := range rooms {
		if room.Id == id && room.Admin == admin {
			room.Available = false

			break
		}
	}
}

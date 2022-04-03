package room

import "github.com/pion/webrtc/v2"

type Room struct {
	Id                string
	PeerConnectionMap map[string]chan *webrtc.Track
}

func New(id string) Room {
	return Room{
		Id:                id,
		PeerConnectionMap: make(map[string]chan *webrtc.Track),
	}
}

package track

import "github.com/pion/webrtc/v2"

func ReceiveTrack(
	bobPeerConnection *webrtc.PeerConnection,
	peerConnectionMap map[string]chan *webrtc.Track,
	AliceID string) {

	if _, ok := peerConnectionMap[AliceID]; !ok {
		peerConnectionMap[AliceID] = make(chan *webrtc.Track, 1)
	}

	localTrack := <-peerConnectionMap[AliceID]
	_, _ = bobPeerConnection.AddTrack(localTrack)
}

package cmd

import (
	"github.com/pion/webrtc/v2"

	"github.com/amirhnajafiz/Blue-sky/internal/pion/media"
)

type Sdp struct {
	Sdp string
}

func Exec() {
	peerConnectionConfig := media.GetPeerConfig()
	api := media.GetMediaAPI()

	var session Sdp
	offer := webrtc.SessionDescription{}

	peerConnection, _ := api.NewPeerConnection(peerConnectionConfig)

	_ = peerConnection.SetRemoteDescription(offer)

	answer, _ := peerConnection.CreateAnswer(nil)

	err := peerConnection.SetLocalDescription(answer)
	if err != nil {
		panic(err)
	}
}

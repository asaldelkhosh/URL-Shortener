package cmd

import (
	"fmt"
	"github.com/amirhnajafiz/Blue-sky/internal/pion/media"

	"github.com/pion/webrtc/v2"
)

func Exec() {
	peerConnectionConfig := media.GetPeerConfig()

	fmt.Println(peerConnectionConfig.Certificates)

	m := webrtc.MediaEngine{}
	m.RegisterCodec(webrtc.NewRTPVP8Codec(webrtc.DefaultPayloadTypeVP8, 90000))
	api := webrtc.NewAPI(webrtc.WithMediaEngine(m))

	fmt.Println(api)
}

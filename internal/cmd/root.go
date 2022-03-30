package cmd

import (
	"fmt"
	"github.com/pion/webrtc/v2"
)

func Exec() {
	peerConnectionConfig := webrtc.Configuration{
		ICEServers: []webrtc.ICEServer{
			{
				URLs: []string{"stun:stun.l.google.com:19302"},
			},
		},
	}

	fmt.Println(peerConnectionConfig.Certificates)
}

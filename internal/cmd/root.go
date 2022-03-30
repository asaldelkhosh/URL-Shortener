package cmd

import (
	"fmt"

	"github.com/amirhnajafiz/Blue-sky/internal/pion/media"
)

func Exec() {
	peerConnectionConfig := media.GetPeerConfig()
	api := media.GetMediaAPI()

	fmt.Println(peerConnectionConfig.Certificates)
	fmt.Println(api)
}

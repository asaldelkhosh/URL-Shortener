package cmd

import (
	"fmt"
	"strconv"

	"github.com/amirhnajafiz/Blue-sky/internal/pion/media"
	"github.com/gin-gonic/gin"
	"github.com/pion/webrtc/v2"
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

	router := gin.Default()
	router.POST("/webrtc/sdp/m/:meetingId/c/:userID/p/:peerId/s/:isSender", func(c *gin.Context) {
		isSender, _ := strconv.ParseBool(c.Param("isSender"))
		userID := c.Param("userID")
		peerID := c.Param("peerId")

		fmt.Println(isSender, userID, peerID)
	})

	_ = router.Run(":8080")
}

func recieveTrack(
	bobPeerConnection *webrtc.PeerConnection,
	peerConnectionMap map[string]chan *webrtc.Track,
	AliceID string) {

	if _, ok := peerConnectionMap[AliceID]; !ok {
		peerConnectionMap[AliceID] = make(chan *webrtc.Track, 1)
	}

	localTrack := <-peerConnectionMap[AliceID]
	_, _ = bobPeerConnection.AddTrack(localTrack)
}

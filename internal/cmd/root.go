package cmd

import (
	"fmt"
	"github.com/amirhnajafiz/Blue-sky/internal/pion/signal"
	"net/http"
	"strconv"
	"time"

	"github.com/amirhnajafiz/Blue-sky/internal/pion/media"
	"github.com/gin-gonic/gin"
	"github.com/pion/webrtc/v2"
)

const (
	rtcpPLIInterval = time.Second * 3
)

type Sdp struct {
	Sdp string
}

func Exec() {
	router := gin.Default()

	peerConnectionMap := make(map[string]chan *webrtc.Track)
	api := media.GetMediaAPI()
	peerConnectionConfig := media.GetPeerConfig()

	router.POST("/webrtc/sdp/m/:meetingId/c/:userID/p/:peerId/s/:isSender", func(c *gin.Context) {
		isSender, _ := strconv.ParseBool(c.Param("isSender"))
		userID := c.Param("userID")
		peerID := c.Param("peerId")

		var session Sdp
		if err := c.ShouldBindJSON(&session); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		offer := webrtc.SessionDescription{}
		signal.Decode(session.Sdp, &offer)

		fmt.Println(isSender, userID, peerID)
	})

	peerConnection, _ := api.NewPeerConnection(peerConnectionConfig)

	_ = peerConnection.SetRemoteDescription(offer)

	answer, _ := peerConnection.CreateAnswer(nil)

	err := peerConnection.SetLocalDescription(answer)
	if err != nil {
		panic(err)
	}

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

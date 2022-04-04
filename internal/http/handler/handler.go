package handler

import (
	"net/http"
	"strconv"

	"github.com/amirhnajafiz/Blue-sky/internal/config"
	"github.com/amirhnajafiz/Blue-sky/internal/pion/signal"
	"github.com/amirhnajafiz/Blue-sky/internal/pion/track"
	"github.com/amirhnajafiz/Blue-sky/internal/room"
	"github.com/gin-gonic/gin"
	"github.com/pion/webrtc/v2"
)

type Sdp struct {
	Sdp string
}

type Handler struct {
	Cfg                  config.Config
	Api                  *webrtc.API
	PeerConnectionConfig webrtc.Configuration
}

func (h Handler) Call(c *gin.Context) {
	isSender, _ := strconv.ParseBool(c.Param("isSender"))
	userID := c.Param("userID")
	peerID := c.Param("peerId")
	meetID := c.Param("meetingId")

	r, e := room.Find(meetID)
	if e != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": e.Error()})

		return
	}

	var session Sdp
	if err := c.ShouldBindJSON(&session); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})

		return
	}

	offer := webrtc.SessionDescription{}
	signal.Decode(h.Cfg.Signal.Compress, session.Sdp, &offer)

	peerConnection, _ := h.Api.NewPeerConnection(h.PeerConnectionConfig)
	_ = peerConnection.SetRemoteDescription(offer)

	if !isSender {
		track.ReceiveTrack(peerConnection, r.PeerConnectionMap, peerID)
	} else {
		track.CreateTrack(peerConnection, r.PeerConnectionMap, userID)
	}
}

func (h Handler) Register(app *gin.RouterGroup) {
	app.POST("/webrtc/sdp/m/:meetingId/c/:userID/p/:peerId/s/:isSender", h.Call)
}
package handler

import (
	"fmt"
	"net/http"
	"strconv"
	"time"

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

func (h Handler) NewRoom(c *gin.Context) {
	admin, ok := c.Get("user_id")
	if !ok {
		c.JSON(http.StatusBadRequest, gin.H{"error": fmt.Errorf("user id field not found")})

		return
	}

	id := time.Millisecond.String()
	room.New(id, admin.(string))

	c.JSON(http.StatusCreated, gin.H{"id": id})
}

func (h Handler) CloseRoom(c *gin.Context) {
	meetID := c.Param("meetingId")
	admin, ok := c.Get("user_id")
	if !ok {
		c.JSON(http.StatusBadRequest, gin.H{"error": fmt.Errorf("user id field not found")})

		return
	}

	room.Close(meetID, admin.(string))

	c.String(http.StatusNoContent, "room closed")
}

func (h Handler) AllRooms(c *gin.Context) {
	c.JSON(http.StatusOK, room.All())
}

func (h Handler) Register(app *gin.RouterGroup) {
	app.POST("/webrtc/sdp/m/:meetingId/c/:userID/p/:peerId/s/:isSender", h.Call)
	app.PUT("/webrtc/room", h.NewRoom)
	app.DELETE("/webrtc/room/:meetingId", h.CloseRoom)
	app.GET("webrtc/room", h.AllRooms)
}

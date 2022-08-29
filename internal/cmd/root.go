package cmd

import (
	"github.com/amirhnajafiz/blue-sky/internal/config"
	"github.com/amirhnajafiz/blue-sky/internal/http/handler"
	"github.com/amirhnajafiz/blue-sky/internal/pion/media"
	"github.com/gin-gonic/gin"
)

func Execute() {
	cfg := config.Load()

	router := gin.Default()

	handler.Handler{
		Cfg:                  cfg,
		Api:                  media.GetMediaAPI(),
		PeerConnectionConfig: media.GetPeerConfig(),
	}.Register(router.Group("api"))

	if err := router.Run(cfg.Address); err != nil {
		panic(err)
	}
}

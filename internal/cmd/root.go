package cmd

import (
	"github.com/amirhnajafiz/Blue-sky/internal/config"
	"github.com/amirhnajafiz/Blue-sky/internal/http/handler"
	"github.com/amirhnajafiz/Blue-sky/internal/pion/media"
	"github.com/gin-gonic/gin"
)

func Exec() {
	cfg := config.Load()
	router := gin.Default()

	handler.Handler{
		Cfg:                  cfg,
		Api:                  media.GetMediaAPI(),
		PeerConnectionConfig: media.GetPeerConfig(),
	}.Register(router.Group("api"))

	_ = router.Run(cfg.Address)
}

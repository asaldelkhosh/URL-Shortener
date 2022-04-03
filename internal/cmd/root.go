package cmd

import (
	"github.com/amirhnajafiz/Blue-sky/internal/config"
	"github.com/gin-gonic/gin"
)

func Exec() {
	cfg := config.Load()
	router := gin.Default()

	_ = router.Run(cfg.Address)
}

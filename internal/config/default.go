package config

import (
	"github.com/amirhnajafiz/blue-sky/internal/pion/signal"
	"github.com/amirhnajafiz/blue-sky/internal/room"
)

func Default() Config {
	return Config{
		Address: ":8080",
		Room: room.Config{
			Rooms:    10,
			Capacity: 5,
			Prefix:   "_room",
		},
		Signal: signal.Config{
			Compress: true,
		},
	}
}

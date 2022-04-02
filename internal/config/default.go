package config

import "github.com/amirhnajafiz/Blue-sky/internal/pion/signal"

func Default() Config {
	return Config{
		Address: ":8080",
		Signal: signal.Config{
			Compress: true,
		},
	}
}

package room

type Config struct {
	Rooms    int    `koanf:"rooms"`
	Capacity int    `koanf:"capacity"`
	Prefix   string `koanf:"prefix"`
}

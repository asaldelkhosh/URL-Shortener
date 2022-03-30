package media

import "github.com/pion/webrtc/v2"

func GetMediaAPI() *webrtc.API {
	m := webrtc.MediaEngine{}

	m.RegisterCodec(webrtc.NewRTPVP8Codec(webrtc.DefaultPayloadTypeVP8, 90000))

	return webrtc.NewAPI(webrtc.WithMediaEngine(m))
}

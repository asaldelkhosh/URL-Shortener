package signal

import (
	"bytes"
	"compress/gzip"
	"encoding/base64"
	"encoding/json"
	"io/ioutil"
)

func Decode(compress bool, in string, obj interface{}) {
	b, err := base64.StdEncoding.DecodeString(in)
	if err != nil {
		panic(err)
	}

	if compress {
		b = unzip(b)
	}

	err = json.Unmarshal(b, obj)
	if err != nil {
		panic(err)
	}
}

func unzip(in []byte) []byte {
	var b bytes.Buffer

	_, err := b.Write(in)
	if err != nil {
		panic(err)
	}

	r, err := gzip.NewReader(&b)
	if err != nil {
		panic(err)
	}

	res, err := ioutil.ReadAll(r)
	if err != nil {
		panic(err)
	}

	return res
}

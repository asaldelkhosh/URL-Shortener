package signal

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

// Allows compressing offer/answer to bypass terminal input limits.
const compress = false

func MustReadStdin() string {
	r := bufio.NewReader(os.Stdin)

	var in string
	for {
		var err error
		in, err = r.ReadString('\n')
		if err != io.EOF {
			if err != nil {
				panic(err)
			}
		}
		in = strings.TrimSpace(in)
		if len(in) > 0 {
			break
		}
	}

	fmt.Println("")

	return in
}

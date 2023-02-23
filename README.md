<p align="center">
    <img src="assets/logo.webp" width="400" alt="logo" />
</p>

<h1 align="center">
Blue Sky
</h1>

Blue sky is an application for holding video conference, build with **WebRTC**. The main
idea behind this project was to work with **PION** and
webRTC in Golang.

## How to use the project?
### Start
Clone and start server:
```shell
go run main.go
```

#### Create a new room
| Syntax    | Description  |
|-----------|--------------|
| Route     | /webrtc/room |
| Method    | PUT          |

##### Body
```json
{
  "user_id": "[admin]"
}
```

##### Response
```json
{
  "id": "[room id]"
}
```

#### Get all available rooms
| Syntax    | Description  |
|-----------|--------------|
| Route     | /webrtc/room |
| Method    | GET          |

##### Response
```json
[
  "[id 1]", "[id 2]"
]
```

#### Make a call
| Syntax   | Description                                              |
|----------|----------------------------------------------------------|
| Route    | /webrtc/sdp/m/:meetingId/c/:userID/p/:peerId/s/:isSender |
| Method   | POST                                                     |


#### Close a room
| Syntax    | Description             |
|-----------|-------------------------|
| Route     | /webrtc/room/:meetingId |
| Method    | DELETE                  |

##### Body
```json
{
  "user_id": "[room admin]"
}
```

## Deploy
To deploy the project on kubernetes:
````shell
kubectl apply -f ./deploy/deployments.yaml
kubectl apply -f ./deploy/service.yaml
````

## Resources

- https://www.tutorialspoint.com/webrtc/index.htm
- https://www.researchgate.net/publication/322511267_eeDTLS_Energy-Efficient_Datagram_Transport_Layer_Security_for_the_Internet_of_Things
- https://telnyx.com/resources/webrtc-servers-explained
- https://webrtccourse.com/
- https://w3c.github.io/webrtc-pc/
- https://ortc.org/
- https://webrtc.github.io/samples/
- https://github.com/pion/webrtc
- https://gabrieltanner.org/blog/broadcasting-ion-sfu/
- https://webrtcforthecurious.com/
- https://www.manning.com/books/real-world-cryptography

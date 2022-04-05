# Blue-sky

Blue sky is an application for holding video conference, build with WebRTC.

## How to use?
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

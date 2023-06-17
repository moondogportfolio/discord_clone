## Description

- A copy of the popular chatting app Discord.
- Implements guilds, channels, direct messages, group messages and threads with regards to text messages.
- Users can also upload and send images, as well as stickers and custom emojis.
- Partial support for installable third-party applications.


## Technical
- Javascript/Vue files are located in ***src*** folder.
- Frontend is written in Vue 3 and is designed as a single-page application (SPA). HTML components from [Quasar library](https://quasar.dev/components) are also used.
- State management is handled by Vuex library (***src>store***). AJAX requests to the server is handled by Axios library.
- Python files are located in **pyserver** folder.
- Server is programmed in Python and utilizes the FASTapi library.
- Security with regards to authorization is achieved JSON Web Tokens that follow the OAuth2 specification.
- Database is connected to a MongoDB server.
- Realtime updates are streamed downward to the client using websockets. Project uses socketio library both for server and client websocket needs.
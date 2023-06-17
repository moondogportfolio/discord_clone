import { getField } from 'vuex-map-fields';
import { date } from 'quasar'

export { getField }

export function SEND_MESSAGES (state) {
  SEND_MESSAGES: state => {
      // https://codeforwin.org/2016/01/c-program-to-get-value-of-nth-bit-of-number.html
      try { return (state.selected_serverdata.permissions >> 11) & 1 ? true : false }
      catch (error) {
        console.log('SEND_MESSAGES error')
      }

    }
}

export function server_id (state) {
  return state.serverdata.selected_serverdata._id
}

export function room_id (state) {
  return state.roomdata.selected_roomdata._id
}

export function user_id (state) {
  return state.userdata._id
}

export function selected_serverdata(state) {
  return state.serverdata.selected_serverdata
}

export function selected_roomdata(state) {
  return state.roomdata[state.selected_room]
}


export function pinned_rooms (state) {
  return state.userdata.state.pinned_rooms
}

export function userstate (state) {
  return state.userdata.state
}

export function selected_workspacedata(state) {
  return state.workspacedata[state.userdata.state.selected_workspace]
}

export function friend_dict (state) {
  return state.friendlist.reduce((prev, curr) => {prev[curr['_id']] = curr; return prev}, {})
}


export function friends (state) {
  return state.userdata.relationships.friend
}

export function array_fields () {
  return ['number', 'text','color', 'date', 'daterange', 'resource', 'involved', 'checkbox']
}

export function q_date() {
  return date
}
export default function () {
  return {

    auth: null,

    form_role: {
      name: null,
      color: null,
      hoist: true,
      permissions: 0,
      mentionable: true,
    },
    logged_in: false,
    admin_selected_menu: "roles",


    //workspace
    selected_workspace: null,
    logic: {
      "conditions": [
       { "==": [ 'Done', {var: 'task.status'} ] },
      ],
      "triggers": [
        {}
      ]
    },
    settings_overlay: false,
    settings_component: 'server_settings',
    isvisible_members: true,
    isvisible_profile_modal: false,
    
    //server header tab
    server_header_tab: 'mails',
    isvisible_todomodal: false,

    //chat
    selected_room: null,

    //post
    isreplying_to: false,
    replyingto_id: null,
    selected_post: null,
    chatContainerScrollRef: null,
    focused_room: null,
    
    //thread
    selected_post_object: null,
    isvisible_thread: false, //threadheader
    thread_mode: 'create', //[create or thread]

    userdata: null,
    serverdata: null,
    channeldata: null,
    roomdata: null,
    serverlist: [],
    dmdict: {},
    chatdata: null,
    friendlist: null,

    hovered_member: null,
    selected_emoticon: null,
    selected_group: null,
  };
}

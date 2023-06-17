const ChannelContainer = () => import(/* webpackChunkName: "server" */ 'src/components/channelComponents/channelContainer.vue')
const HeaderContainer = () => import(/* webpackChunkName: "server" */ 'src/components/headerComponents/headerContainer.vue')
const ChatViewContainer = () => import(/* webpackChunkName: "server" */ 'src/components/chatComponents/chat view container.vue')
const MemberContainer = () => import(/* webpackChunkName: "server" */ 'src/components/memberComponents/memberContainer.vue')
const ThreadContainer = () => import(/* webpackChunkName: "server" */ 'src/components/threadComponents/threadContainer.vue')

const FriendHeaderContainer = () => import(/* webpackChunkName: "@me" */ 'src/components/friendPanelComponents/friendHeader.vue')
const CenterContainer = () => import(/* webpackChunkName: "@me" */ 'src/components/friendPanelComponents/centerContainer.vue')
const ActiveFriendsContainer = () => import(/* webpackChunkName: "@me" */ 'src/components/friendPanelComponents/activeFriendsContainer.vue')
const DmContainer = () => import(/* webpackChunkName: "@me" */ 'src/components/friendPanelComponents/dmContainer.vue')

const DscvrSidebar = () => import(/* webpackChunkName: "discover" */ 'src/components/exploreComponents/discoverSidebar.vue')
const DscvrMain = () => import(/* webpackChunkName: "discover" */ 'src/components/exploreComponents/discoverMain.vue')


const ParticipantsContainer = () => import(/* webpackChunkName: "@me/room_id" */ 'src/components/dmComponents/participants.vue')
const DmChatContainer = () => import(/* webpackChunkName: "@me/room_id" */ 'src/components/dmComponents/dm chat wrapper.vue')

const workspaceMain = () =>  import(/* webpackChunkName: "workspace" */ "src/components/productivity/workspaceMainComponents/workspaceContainer.vue")
const workspaceTop  = () =>  import(/* webpackChunkName: "workspace" */ "src/components/productivity/workspaceTopComponents/headerContainer.vue")
const workspaceLeft = () => import(/* webpackChunkName: "workspace" */ "src/components/productivity/workspaceLeftComponents/Container.vue")
const workspaceRight  = () =>  import(/* webpackChunkName: "workspace" */ "src/components/productivity/workspaceRightComponents/RightContainer.vue")
// const workspaceMain  = () =>  import(/* webpackChunkName: "workspace" */ "src/components/productivity/graph/cytoContainer.vue")
// const workspaceMain  = () =>  import(/* webpackChunkName: "workspace" */ "src/components/projectComponents/resource/resourceContainer.vue")
// const workspaceMain = () =>  import(/* webpackChunkName: "workspace" */ "src/components/projectComponents/entity/entityContainer.vue")

import Interstitial from 'src/components/Interstitial.vue';

const routes = [
  {
    path: "/",
    beforeEnter: (to, from, next) => {
      if (sessionStorage.getItem('jwt') == null){
          console.log('ROUTE: Jwt not found. Routing to login.') 
          next('/login');
        }
      else {
        console.log('ROUTE: Jwt found. Routing to interstitial.')
        next('/interstitial');
      }
    }
  },
  {
    path: "/interstitial",
    component: Interstitial
  },
  {
    path: "/channels",
    component: () => import("pages/MainView.vue"),
    children: [
      {
        //DM VIEW
        path: "@me/:room_id",
        components: {
          'dm-chat-container': ChatViewContainer,
          'participants-container': ParticipantsContainer,
          // 'chat-header-container': FriendHeaderContainer,
          'dm-container': DmContainer,
        }
      },
      {
        //FRIENDS VIEW
        path: "@me",
        components: {
          'center-container': CenterContainer,
          'active-friends-container': ActiveFriendsContainer,
          'friend-header-container': FriendHeaderContainer,
          'dm-container': DmContainer,
          
        }
      },
      {
        //SERVER VIEW
        path: ":server_id/:room_id",
        components: {
          'channel-container': ChannelContainer,
          'header-container': HeaderContainer,
          'chat-container': ChatViewContainer,
          'member-container': MemberContainer,
          'thread-container': ThreadContainer
        }
      },
      {
        //DISCOVERY VIEW
        path: "server-discovery",
        components: {
          'discover-sidebar': DscvrSidebar,
          'discover-main': DscvrMain
        }
      }
    ]
  },
  {
    path: "/login",
    component: () => import("pages/FirstView.vue"),
  },
  {
    path: "/dataplex",
    component: () => import("pages/dataplex.vue"),
  },
  {
    path: "/test",
    // component: () => import("src/components/productivity/graph/cytoContainer.vue"),
    // component: () => import("src/components/projectComponents/resource planner/rpContainer.vue"),
    // component: () => import("src/components/projectComponents/resource/resourceContainer.vue"),
    // component: () => import("src/pages/drag test.vue"),
    component: () => import("src/pages/test.vue"),
    // component: () => import("src/pages/create org.vue"),
    // component: () => import("src/components/productivity/workspaceMainComponents/workspaceContainer.vue"),

  },

  {
    path: "/task",
    component: () => import("src/components/productivity/taskComponents/datasource.vue"),
  },
  {
    path: "/invite/:invite_id",
    component: () => import("pages/Invites.vue"),
  },
  {
    path: "/workspace/:workspace_id",
    component: () => import("pages/MainView.vue"),
    children: [{
      path: "",
      components: {
        'workspace-main': workspaceMain,
        'workspace-top': workspaceTop,
        'workspace-left':  workspaceLeft,
        'workspace-right': workspaceRight

      }
    }]
  },
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/Error404.vue"),
  },
];

export default routes;

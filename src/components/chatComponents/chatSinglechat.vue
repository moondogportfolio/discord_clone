<template lang="pug">
div.chat-single()
  //- div
    //- q-avatar(size="42px")
      //- q-img(:src="`http://localhost:8000/user-icon/${post.author}`")
  div.q-mx-md(style="width: 100%")
    div.cursor-pointer.text-grey(v-if="reference") reply to: 
      span.reference-content(@click="scroll_to_reference") {{ reference.content }} {{ post.message_reference }}
    template(v-if="ishidden_edit_box")
      div
        div
          span.text-bold.q-mr-sm  {{post.author.slice(0,4)}}
          span {{ timestamp_convert(post.timestamp) }}
        //- div.text-bold post_id: {{post_id}}
        div(v-html="rendered" :id="`post-${post_id}`")
        div
          q-chip(v-for="reaction in Object.entries(post.reactions)" :key="reaction")
            q-avatar
              q-img(:src="`http://localhost:8000/emojis/${server_id}/${reaction[0]}`")
            q-tooltip
              span {{reaction[1].join(', ')}} reacted with {{emoji_name(reaction[0])}}
        template(v-if="post.thread")
          div post thread: {{post.thread}}
          thread-mini(@show_thread="show_thread")
      

    template(v-else)
      div.chat-input-wrapper
        q-input.q-ml-sm(
          borderless
          v-model="edit_contents"
          @keyup.enter="edit_message"
          @keyup.escape="cancel_edit"
          )
          template(v-slot:append)
            div.q-mr-md
              q-icon.cursor-pointer(name="emoji_emotions")
      div.text-grey-7
        span.text-caption escape to 
        span.text-caption.url-link(@click="cancel_edit") cancel
        span.text-caption  • 
        span.text-caption.url-link(@click="edit_message") enter
        span.text-caption  to save

q-menu.chat-menu-outer(
  anchor="top right"
  self="top right"
  :model-value="ishidden_message_menu"
  :target="`#post-${post_id}`"
  )
  div.chat-single-menu
    q-icon.cursor-pointer(name="mood" size="24px")
      q-menu
        emoticon-container-vue
    q-icon.cursor-pointer(name="reply" color="green" size="24px" @click="reply")
    q-icon.cursor-pointer(name="edit" color="green" size="24px" @click="show_edit")
    q-icon.cursor-pointer(name="push_pin" color="green" size="24px" )
    q-icon.cursor-pointer(name="tag" color="red" size="24px" @click="init_create_thread")
    q-icon.cursor-pointer(name="delete" color="red" size="24px")

</template>

<script>
import emoticonContainerVue from '../emojiComponents/emoticonContainer.vue';
import threadMini from './threadMini.vue';

export default {
  components: {emoticonContainerVue, threadMini}, 
  computed: {
    rendered() {
      try {
        return this.$markdown.render(this.post.content);
      } catch (error) {
        return `cant be markdown rendered ${this.post.content}`
      }
    },
    server_id() {
      return this.$store.state.serverdata.selected_serverdata._id
    },
    room_id() {
      return this.$store.state.roomdata.selected_roomdata._id
    }
  },
  methods: {
    timestamp_convert(timestamp) {
      // https://www.codegrepper.com/code-examples/javascript/toLocaleDateString%28%29+options
      return new Date(timestamp).toLocaleDateString('en-gb',
        {
          year: 'numeric',
          month: 'long',
          day: 'numeric',
          hour: 'numeric',
          minute: 'numeric'
        }
      )
    },
    async show_thread() {
      this.$store.commit('mutate_shallow', {
        isvisible_thread: true,
        thread_mode: 'loading'
        }
      );
      let threaddata = await this.$api({
        method: 'get',
        url: `/thread/${this.post.thread}`,
        headers : {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.$store.state.auth}`
        }
      }).then((response)=>{
        return response.data
      }).catch((error) => {
        console.log(error)
      })
      if(threaddata) {
        this.$store.commit('mutate_deep',
          {
            userdata: {
              state: {
                selected_thread: this.post.thread
                }
              },
            threaddata: threaddata,
            thread_mode: 'thread'
          }
        );
        
      }
    },
    init_create_thread() {
      this.$store.commit('mutate_shallow',
        {
          selected_post_object: {
            id: this.post_id,
            object: this.post,
            reference: this.reference
          },
          isvisible_thread: true,
          thread_mode: 'create',
        });
    },
    scroll_to_reference() {
      let ele = document.querySelector(`#post-${this.post.message_reference}`)
      if (this.chatContainerScrollRef.getScrollPosition().top > ele.offsetTop) {
        this.chatContainerScrollRef.setScrollPosition('vertical', ele.offsetTop, 200)
      }
    },  
    get_replied_to_post() {
      this.$store.state.roomdata.selected_roomdata.posts
    },
    set_selected_post() {
      this.$store.commit('mutate_shallow', {selected_post: this.post_id})
      console.log(this.$store.state.selected_post)
    },
    emoji_name(emoji_id) {
      return this.$store.state.serverlist.find(ele => ele._id == this.server_id).emoji[emoji_id].name
    },
    reply() {
      this.$store.commit('mutate_shallow', {
        isreplying_to: true,
        replyingto_id: this.post_id
        })
    },
    pin_message() {
      this.save_edit({
        pinned: !this.post.pinned
      })
    },
    edit_message() {
      this.save_edit({
        content: this.edit_contents
        })
    },
    save_edit(data) {
      this.ishidden_edit_box = true;
      this.$api({
        method: 'patch',
        url: `/room/${this.room_id}/message/${this.post_id}`,
        data: data,
        headers : {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.$store.state.auth}`
        }
      }).then((response)=>{
          console.log(response);
          this.edit_contents = this.post.content
      }).catch((error) => {
          null
      })
    },
    cancel_edit() {
       this.ishidden_edit_box = true;
       this.edit_contents = this.post.content;
    },
    show_edit() {
      console.log('EDIT')
      this.ishidden_edit_box = false;
    }
  },
  data() {
    return {
      ishidden_message_menu: false,
      ishidden_edit_box: true,
      edit_contents: null,
    }
  },
  name: "ChatSingleChat",
  props: ["post", "post_id", "reference", "chatContainerScrollRef"],
};
</script>

<style>
.chat-single {
  display: flex;
  margin-bottom: 20px;
  margin-right: 20px;
  padding: 5px 0;
}

.chat-single:hover {
  background: #f0f0f4;
  border-radius: 5px;
}

.chat-menu-outer {
  box-shadow: unset;
  border: 1px solid lightgray;
}

.chat-menu-outer:hover {
  box-shadow: 0px 1px 10px 0px rgb(0 0 0 / 30%);
  -webkit-box-shadow: 0px 1px 10px 0px rgb(0 0 0 / 30%);
  -moz-box-shadow: 0px 1px 10px 0px rgb(0 0 0 / 30%);
}

.chat-single-menu {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-column-gap: 5px;
  margin: 5px;
}

.chat-single-menu .q-icon:hover {
  color:hotpink;
}

.url-link {
  color: #0068E0
}

.url-link:hover {
  text-decoration: underline;
}

.reaction {
  padding: 2px 5px;
  border-radius: 5px;
  margin-right: 5px;
  border: 1px solid cornflowerblue;

}

.reference-content:hover {
  color: black;
}
</style>

<template lang="pug">
div.chat-input-wrapper.q-ma-sm
  div.cursor-pointer.q-pa-sm.relative-position.text-grey-7(
    style="background: #F2F3F5; border-radius: 10px 5px"
    v-if="isreplying_to"
    @click="goto_message")
    span Reply to 
    span.text-bold mccndcg
    q-avatar(icon="close" style="position: absolute; right:5px; margin: auto 0px" size="20px" color="grey" @click="cancel_reply")
  //- menu-commands(:input_chat="input_chat")
  //- menu-mentions(:offset="offset")
  q-input(
    standout
    :bottom-slots="false"
    input-class="chat-input"
    @keyup.enter="send_chat"
    @select="select_text()"
    
    v-model="input_chat"
    )
    template(v-slot:prepend)
      q-icon.q-ml-md(name="add_box")
    template(v-slot:hint)
      div Try slash commands.
    template(v-slot:append)
      div.q-mr-md
        q-icon(name="add_box")
        q-icon.cursor-pointer(name="emoji_emotions" @click="show_emoticon_container = !show_emoticon_container")
          q-menu.emoticon-select
            p lorem
            emoticon-container-vue

//- label Markdown
//-   input( value="markdown"  name="inputformat" type="radio" checked)
//- label Prose Mirror
//-   input( value="prosemirror"  name="inputformat" type="radio")
//- textarea#content(style="visibility: hidden")
//- .q-ma-lg
//-   #editor
  
</template>

<script>
import emoticonContainerVue from '../emojiComponents/emoticonContainer.vue';
import { shrug } from '../builtin apps/shrug.js';
import menuMentions from './menu mentions.vue';
import menuCommands from './menu commands.vue' ;


import {EditorView} from "prosemirror-view"
import {EditorState} from "prosemirror-state"
import {schema, defaultMarkdownParser,
        defaultMarkdownSerializer} from "prosemirror-markdown"
import {exampleSetup} from "prosemirror-example-setup"

class ProseMirrorView {
  constructor(target, content) {
    this.view = new EditorView(target, {
      state: EditorState.create({
        doc: defaultMarkdownParser.parse(content),
        plugins: exampleSetup({schema})
      })
    })
  }

  get content() {
    return defaultMarkdownSerializer.serialize(this.view.state.doc)
  }
  focus() { this.view.focus() }
  destroy() { this.view.destroy() }
}

class MarkdownView {
  constructor(target, content) {
    this.textarea = target.appendChild(document.createElement("textarea"))
    this.textarea.value = content
  }

  get content() { return this.textarea.value }
  focus() { this.textarea.focus() }
  destroy() { this.textarea.remove() }
}

export default {
  setup () {
    return {
      shrug
    }
  },
  mounted() {
    return
    let place = document.querySelector("#editor")
    let view = new MarkdownView(place, document.querySelector("#content").value)

    document.querySelectorAll("input[type=radio]").forEach(button => {
      button.addEventListener("change", () => {
        if (!button.checked) return
        let View = button.value == "markdown" ? MarkdownView : ProseMirrorView
        if (view instanceof View) return
        let content = view.content
        view.destroy()
        view = new View(place, content)
        view.focus()
      })
    })
  },
  name: "ChatInput",
  components: {emoticonContainerVue, menuMentions, menuCommands},
  computed: {
    userstate() {
      return this.$store.state.userdata.state
    },
    CAN_SEND_MESSAGES() { 
      return true
    },
    selected_room() {
      return this.userstate.selected_room
    },
    selected_thread() {
      return this.userstate.selected_thread;
    },
    isreplying_to() {
      return this.$store.state.isreplying_to
    },
  },
  data() {
    return {
      shape: 'prosemirror',
      quill: null,
      editor: null,
      show_emoticon_container: false,
      input_chat: null,
      isvisible_mentionmenu: false,
      offset: null,
    };
  },
  sockets: {
    message_create(post) {
      this.$store.commit('message_create', post)
    }
  },
  methods: {
    create_mention() {
    },
    goto_message() {
      document.querySelector(`#post-${this.$store.state.replyingto_id}`).scrollIntoView()
    },
    cancel_reply() {
      this.$store.commit('mutate_shallow', {isreplying_to: false})
    },
    send_chat() {
      // console.log(document.querySelector('#contenteditable'))
      // return
      // console.log(this.shrug(this.input_chat));
      // console.log(`selected command is ${this.selected_command}`);
      // console.log(`selected subcommands are ${this.subcommands}`);
      // console.log(`input chat is ${this.input_chat}`)
      if(this.input_chat == null) return
      let message = {
        "author": this.$store.state.userdata._id,
        "content": this.input_chat,
        'message_reference': this.isreplying_to ? this.$store.state.replyingto_id : null
      }
      this.input_chat = null; 
      this.$api({
        method: 'post',
        url: `/room/${this.$store.state.focused_room}/message`,
        data: message,
        headers : {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.$store.state.auth}`
         }
      }).then((response)=>{
      }).catch((error) => {
        console.log(error)
      })
    },
  },
};
</script>

<style>

.chat-input-wrapper {
  background-color: #EBEDEF;
  border-radius: 10px;
}

.mention {
  border: 1px solid green;
  padding: 2px;
  margin: 0 3px;
  cursor: pointer;
}

div#contenteditable:focus {
  outline: 0
}

div#editor textarea {
  outline: 0;
  width: 100%;
  border: 0;
  padding: 10px;

}

.ProseMirror {
  position: relative;
}

.ProseMirror {
  word-wrap: break-word;
  white-space: pre-wrap;
  white-space: break-spaces;
  -webkit-font-variant-ligatures: none;
  font-variant-ligatures: none;
  font-feature-settings: "liga" 0; /* the above doesn't seem to work in Edge */
}

.ProseMirror pre {
  white-space: pre-wrap;
}

.ProseMirror li {
  position: relative;
}

.ProseMirror-hideselection *::selection { background: transparent; }
.ProseMirror-hideselection *::-moz-selection { background: transparent; }
.ProseMirror-hideselection { caret-color: transparent; }

.ProseMirror-selectednode {
  outline: 2px solid #8cf;
}

/* Make sure li selections wrap around markers */

li.ProseMirror-selectednode {
  outline: none;
}

li.ProseMirror-selectednode:after {
  content: "";
  position: absolute;
  left: -32px;
  right: -2px; top: -2px; bottom: -2px;
  border: 2px solid #8cf;
  pointer-events: none;
}
.ProseMirror-textblock-dropdown {
  min-width: 3em;
}

.ProseMirror-menu {
  margin: 0 -4px;
  line-height: 1;
}

.ProseMirror-tooltip .ProseMirror-menu {
  width: -webkit-fit-content;
  width: fit-content;
  white-space: pre;
}

.ProseMirror-menuitem {
  margin-right: 3px;
  display: inline-block;
}

.ProseMirror-menuseparator {
  border-right: 1px solid #ddd;
  margin-right: 3px;
}

.ProseMirror-menu-dropdown, .ProseMirror-menu-dropdown-menu {
  font-size: 90%;
  white-space: nowrap;
}

.ProseMirror-menu-dropdown {
  vertical-align: 1px;
  cursor: pointer;
  position: relative;
  padding-right: 15px;
}

.ProseMirror-menu-dropdown-wrap {
  padding: 1px 0 1px 4px;
  display: inline-block;
  position: relative;
}

.ProseMirror-menu-dropdown:after {
  content: "";
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 4px solid currentColor;
  opacity: .6;
  position: absolute;
  right: 4px;
  top: calc(50% - 2px);
}

.ProseMirror-menu-dropdown-menu, .ProseMirror-menu-submenu {
  position: absolute;
  background: white;
  color: #666;
  border: 1px solid #aaa;
  padding: 2px;
}

.ProseMirror-menu-dropdown-menu {
  z-index: 15;
  min-width: 6em;
}

.ProseMirror-menu-dropdown-item {
  cursor: pointer;
  padding: 2px 8px 2px 4px;
}

.ProseMirror-menu-dropdown-item:hover {
  background: #f2f2f2;
}

.ProseMirror-menu-submenu-wrap {
  position: relative;
  margin-right: -4px;
}

.ProseMirror-menu-submenu-label:after {
  content: "";
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  border-left: 4px solid currentColor;
  opacity: .6;
  position: absolute;
  right: 4px;
  top: calc(50% - 4px);
}

.ProseMirror-menu-submenu {
  display: none;
  min-width: 4em;
  left: 100%;
  top: -3px;
}

.ProseMirror-menu-active {
  background: #eee;
  border-radius: 4px;
}

.ProseMirror-menu-disabled {
  opacity: .3;
}

.ProseMirror-menu-submenu-wrap:hover .ProseMirror-menu-submenu, .ProseMirror-menu-submenu-wrap-active .ProseMirror-menu-submenu {
  display: block;
}

.ProseMirror-menubar {
  border-top-left-radius: inherit;
  border-top-right-radius: inherit;
  position: relative;
  min-height: 1em;
  color: #666;
  padding: 1px 6px;
  top: 0; left: 0; right: 0;
  border-bottom: 1px solid silver;
  background: white;
  z-index: 10;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  overflow: visible;
}

.ProseMirror-icon {
  display: inline-block;
  line-height: .8;
  vertical-align: -2px; /* Compensate for padding */
  padding: 2px 8px;
  cursor: pointer;
}

.ProseMirror-menu-disabled.ProseMirror-icon {
  cursor: default;
}

.ProseMirror-icon svg {
  fill: currentColor;
  height: 1em;
}

.ProseMirror-icon span {
  vertical-align: text-top;
}
.ProseMirror-gapcursor {
  display: none;
  pointer-events: none;
  position: absolute;
}

.ProseMirror-gapcursor:after {
  content: "";
  display: block;
  position: absolute;
  top: -2px;
  width: 20px;
  border-top: 1px solid black;
  animation: ProseMirror-cursor-blink 1.1s steps(2, start) infinite;
}

@keyframes ProseMirror-cursor-blink {
  to {
    visibility: hidden;
  }
}

.ProseMirror-focused .ProseMirror-gapcursor {
  display: block;
}
/* Add space around the hr to make clicking it easier */

.ProseMirror-example-setup-style hr {
  padding: 2px 10px;
  border: none;
  margin: 1em 0;
}

.ProseMirror-example-setup-style hr:after {
  content: "";
  display: block;
  height: 1px;
  background-color: silver;
  line-height: 2px;
}

.ProseMirror ul, .ProseMirror ol {
  padding-left: 30px;
}

.ProseMirror blockquote {
  padding-left: 1em;
  border-left: 3px solid #eee;
  margin-left: 0; margin-right: 0;
}

.ProseMirror-example-setup-style img {
  cursor: default;
}

.ProseMirror-prompt {
  background: white;
  padding: 5px 10px 5px 15px;
  border: 1px solid silver;
  position: fixed;
  border-radius: 3px;
  z-index: 11;
  box-shadow: -.5px 2px 5px rgba(0, 0, 0, .2);
}

.ProseMirror-prompt h5 {
  margin: 0;
  font-weight: normal;
  font-size: 100%;
  color: #444;
}

.ProseMirror-prompt input[type="text"],
.ProseMirror-prompt textarea {
  background: #eee;
  border: none;
  outline: none;
}

.ProseMirror-prompt input[type="text"] {
  padding: 0 4px;
}

.ProseMirror-prompt-close {
  position: absolute;
  left: 2px; top: 1px;
  color: #666;
  border: none; background: transparent; padding: 0;
}

.ProseMirror-prompt-close:after {
  content: "âœ•";
  font-size: 12px;
}

.ProseMirror-invalid {
  background: #ffc;
  border: 1px solid #cc7;
  border-radius: 4px;
  padding: 5px 10px;
  position: absolute;
  min-width: 10em;
}

.ProseMirror-prompt-buttons {
  margin-top: 5px;
  display: none;
}
#editor, .editor {
  background: white;
  color: black;
  background-clip: padding-box;
  border-radius: 4px;
  border: 2px solid rgba(0, 0, 0, 0.2);
  padding: 5px 0;
  margin-bottom: 23px;
}

.ProseMirror p:first-child,
.ProseMirror h1:first-child,
.ProseMirror h2:first-child,
.ProseMirror h3:first-child,
.ProseMirror h4:first-child,
.ProseMirror h5:first-child,
.ProseMirror h6:first-child {
  margin-top: 10px;
}

.ProseMirror {
  padding: 4px 8px 4px 14px;
  line-height: 1.2;
  outline: none;
}

.ProseMirror p { margin-bottom: 1em }


</style>

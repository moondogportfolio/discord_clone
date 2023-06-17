import Quill from "quill";

const Embed = Quill.import("blots/embed");

class MentionBlot extends Embed {

  static create(data) {
    const node = super.create();
    const denotationChar = document.createElement("span");
    denotationChar.innerHTML = '@';
    node.appendChild(denotationChar);
    node.innerHTML += data;
    return node
  }

  static value(domNode) {
    return domNode.dataset;
  }


}



MentionBlot.blotName = "mention";
MentionBlot.tagName = "span";
MentionBlot.className = "mention";

// Quill.register(MentionBlot);
export { MentionBlot };
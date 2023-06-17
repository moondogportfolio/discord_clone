<template lang="pug">
div.page_div {{dataplex}}
</template>

<script>

export default ({
  name: 'dataplex',
    created() {
      setInterval(()=>{
        this.dataplex += this.chars[~~(Math.random() * this.chars.length)];
        var x = document.querySelector('.page_div')
        x.scrollTo(0, x.scrollHeight);
        },1)
    },
    data() {
      return {
        chars: ['▀', '▄', '█','▌','▐', '░', '▒', '▓', '▬'],
        dataplex: ''
      }
  }
})
</script>

<style>
.page_div {
  max-width: 100vw;
  display:block;
  overflow-wrap: break-word;
  overflow-y: hidden;
  height: 100vh;
}
</style>

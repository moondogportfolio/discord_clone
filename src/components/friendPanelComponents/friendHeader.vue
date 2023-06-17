<template lang="pug">
q-icon(name="people")
span.text-bold Friends
q-separator(vertical)
</template>

<script>
export default {
  name: "FriendHeader",
  data() {
    return {
      tab: null
    }
  }
};
</script>

<style>
#header-bar {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}
</style>

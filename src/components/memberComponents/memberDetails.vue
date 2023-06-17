<template>
  
  <q-card class="fit member-detail click" dark>
    <q-img src="~/assets/mountains.jpg" :ratio="16 / 4"></q-img>
    <q-card-section>
      <q-avatar color="primary" icon="place" class="absolute avatar" />
      <div class="q-gutter-xs absolute" style="right: 10px">
        <q-badge rounded color="yellow" />
        <q-badge rounded color="red" />
        <q-badge rounded color="yellow" />
        <q-badge rounded color="yellow" />
        <q-badge rounded color="yellow" />
        <q-badge rounded color="yellow" />
      </div>
    </q-card-section>
    <q-card-section>
      <div class="">{{ id }}</div>
      <div class="">{{ status }}</div>
    </q-card-section>
    <q-separator dark inset />
    <q-card-section class="q-ma-sm">
      <div class="">ABOUT ME</div>
      <div class="">PLAYING</div>
      <div class="">ROLES</div>
      <div class="row">
        <q-chip icon="event">Add to calendar</q-chip
        ><q-chip icon="event">Add to calendar</q-chip
        ><q-chip icon="event">Add to calendar</q-chip
        ><q-chip icon="event">Add to calendar</q-chip>
      </div>
    </q-card-section>
    <q-card-section>
      <div class="">NOTE</div>
      <q-input
        v-model="ph"
        dark
        borderless
        dense
        placeholder="Click to add a note"
      />
      <q-input
        v-model="ph"
        dark
        dense
        outlined
        placeholder="Message this user"
      />
    </q-card-section>

    <q-card-section class="q-pt-none"> ASDASDASD </q-card-section>
  </q-card>
  
</template>

<script>
export default {
  name: "MemberDetails",
  data() {
    return {
      id: "Matt Eudaimonia#7817",
      status: "Je crois en moi.",
      ph: null,
    };
  },
};
</script>

<style>
.avatar {
  height: 90px;
  top: 0;
  left: 12px;
  transform: translateY(-50%);
  width: 90px;
  border: 4px solid #1d1d1d;
}

.member-detail {
  border-radius: 10px;
}
</style>

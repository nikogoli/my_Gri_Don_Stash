<template :ref="dialogue_part">
 <div>
  <v-dialog v-model="dialog" max-width="500px">
    <v-card>
      <v-card-title class="headline grey lighten-2" primary-title>
        {{card_title}}
      </v-card-title>
      <v-card-text style="white-space:pre-line">
        <div v-for="mp of detail_mps.values()" :key="mp.get('part')">
          <v-icon>{{mp.get('icon')}}</v-icon> {{mp.get("part")}} ：  {{mp.get("name")}} 
        </div>
      </v-card-text>
    </v-card>
  </v-dialog>
</div>
</template>

<script>
 export default {
   data: ()=>({
     card_title : "",
     detail_mps: new Map(),
     dialog: false
   }),
   methods: {
     open(ttle, mps){
       this.card_title = ttle
       this.detail_mps = mps
       this.dialog = true
     }
   },
   watch: {
     dialog: function (value) {
       !value
     }
   }
 }
</script>
 
 

<template>
  <v-container grid-list-md>
    <v-layout row justify-center align-center>
      <p>dialog sample.</p>
      <button @click.prevent="showDialog">show</button>
      <v-text-field
          v-model="search_number"
          append-icon="search"
          label="数字"
          single-line
          hide-details
        ></v-text-field>
      </v-layout>
  </v-container>
</template>

<script>
import DialogHelper from '@/components/DialogHelper.js';
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data () {
    return {
      item_list: [],
      search_number: 0
    }
  },
  methods: {
    make_message: function () {
      return this.item_list[this.search_number]
    },
    showDialog () {
      DialogHelper.showDialog(this, {
        subject: 'Subject',
        message: this.make_message(),
        ok: () => { console.log('click ok') },
        cancel: () => { console.log('click cancel') }
      });
    }
  },
  mounted: function () {
    console.log('mounted')
    axios.get('/api/items/')
      .then((response) => {
        this.item_list = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
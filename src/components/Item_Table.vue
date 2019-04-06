<template>
  <v-container grid-list-md>
    <v-layout row justify-center align-center>
      <v-flex xs12 v-for="l_class in l_class_list" :key=l_class.id >
        <v-btn @click='Filter_item(l_class.name)'>
          {{l_class.name}}
        </v-btn>
      </v-flex>
    </v-layout>
    <v-layout row justify-center align-center>
      <v-flex xs3>
        <v-select
          v-model="selected_class"
          :items="s_class_list"
          label="小分類"
          outline
        ></v-select>
      </v-flex>
      <v-flex xs5 offset-xs3>
        <v-text-field
          v-model="searched_name"
          append-icon="search"
          label="アイテム名検索(小文字のみ)"
          single-line
          hide-details
        ></v-text-field>
      </v-flex>
    </v-layout>
    <v-layout column align-center justify-start style="max-height: 450px" class="scroll-y">
      <v-flex>
        <v-data-table :headers="headers" :items="item_list" class="elevation-10"
        no-data-text="大分類を選択してください" :search="searched_name" :customFilter="Custom_filter" hide-actions
        >
          <template v-slot:items="lists">
            <td>{{lists.item.name}}</td>
            <td>{{lists.item.item_small_class}}</td>
            <td>{{lists.item.item_place}}</td>
          </template>
        </v-data-table>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import axios from 'axios'

export default {
  name: 'LargeClassList',
  data () {
    return {
      searched_name: "",
      selected_class: "All",
      l_class_list: [
        {"id":1, "name":"All" },
        {"id":2, "name":"Armors"},
        {"id":3, "name":"Accessories"},
        {"id":4, "name":"One-Weapons"},
        {"id":5, "name":"Two-Weapons"}
      ],
      s_class_list: ["All"],
      headers: [
        {text: "アイテム名", sortable: true, value:"name"},
        {text: "小分類", sortable: true, value:"item_small_class"},
        {text: "倉庫の場所", sortable: true, value:"item_place"},
      ],
      classed_item_list: [],
      item_list: [],
      classified: [],
    }
  },
  methods: {
    Filter_item: function(value) {
      this.item_list = []
      this.s_class_list = ["All"]
      this.selected_class = "All"
      for (let cls of this.classed_item_list) {
        if(cls["name"] == value) {
          this.item_list = cls["item_set"]
          for (let s_cls of cls["small_class_set"]) {
            this.s_class_list.push(s_cls["name"])
          }
        }
      }
    },
    Custom_filter(items, search, filter){
      if (this.selected_class == "All") {
        this.classified = items
      } else {
        this.classified = items.filter(itm => itm.item_small_class == this.selected_class)
      }
      return this.classified.filter(item => filter(item.name, search))
    }
  },
  mounted: function () {
    console.log('mounted')
    axios.get('/api/item_table/')
      .then((response) => {
        this.classed_item_list = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>
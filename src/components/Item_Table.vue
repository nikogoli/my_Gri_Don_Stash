<template>
  <v-container grid-list-md>
    <v-layout row justify-center align-center>
      <v-flex v-for="l_cls in large_class_list" :key=l_cls.name >
          <input type="radio" v-model="l_radios" name="radios" :value="l_cls.name" @change="Make_small_cls_list(l_cls.name)" /> {{l_cls.name}}
      </v-flex>
    </v-layout>
    <v-layout row justify-center align-center>
      <v-flex xs3>
        <v-select
          v-model="selected_s_cls"
          :items="small_class_list"
          item-text = "name"
          item-value = "name"
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
            <td>{{lists.item.item_large_class}}</td>
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
      l_radios: "All",
      selected_s_cls: "All",
      searched_name: "",
      headers: [
        {text: "アイテム名", sortable: true, value:"name"},
        {text: "小分類", sortable: true, value:"item_small_class"},
        {text: "大分類", sortable: true, value:"item_large_class"},
        {text: "倉庫の場所", sortable: true, value:"item_place"},
      ],
      large_class_list: [],
      l_s_class_dict: {},
      small_class_list: [{"name": "All"}],
      item_list: [],
      classified: [],
    }
  },
  methods: {
    Make_small_cls_list: function(value) {
      this.small_class_list = this.l_s_class_dict[value]
      this.small_class_list.unshift({"name": "All"})
      this.selected_s_cls= "All"
    },
    Custom_filter(items, search, filter){
      let tmp_lis = []
      if (this.l_radios == "All") {
        this.classified = items
      } else {
        tmp_lis = items.filter(itm => itm.item_large_class == this.l_radios)
        if (this.selected_s_cls == "All") {
          this.classified = tmp_lis
        } else {
          this.classified = tmp_lis.filter(itm => itm.item_small_class == this.selected_s_cls)
        }
      }
      return this.classified.filter(item => filter(item.name, search))
    },
  },
  mounted: function () {
    console.log('mounted')
    axios.get('/api/item_table/')
      .then((response) => {
        this.large_class_list = response.data["0"]["large_classes"]
        this.l_s_class_dict = response.data["0"]["small_classes"]
        this.item_list = response.data["0"]["items"]
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>
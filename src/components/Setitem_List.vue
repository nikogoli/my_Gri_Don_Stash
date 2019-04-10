<template>
  <v-container>
  <app-dialogue ref="child_Dialogue"></app-dialogue>
    <v-layout row grid-list-lg justify-start align-center wrap>
        <v-flex md4 v-for="setmap of itemset_map_list" :key="setmap.get('id')" >
          <v-card max-height="190px" min-height="150px"
            max-width="330px"
            @click="show_detail_dialog(setmap)">
            <v-card-title class="title mb-0 pb-0">
                {{ make_title(setmap.get('header_info')) }}
            </v-card-title>
            <v-card-text>
              <div v-for="itemmap of setmap.get('content_items')" :key="itemmap.get('part')">
                <v-icon>{{itemmap.get('icon')}}</v-icon> {{itemmap.get("part")}}
              </div>
            </v-card-text>
          </v-card>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import appDialogue from '@/components/part_Dialogue.vue'
import axios from 'axios'

export default {
  name: 'Setitem_List',
  data () {
    return {
      itemset_map_list: []
    }
  },
  components: {
    appDialogue
  },
  methods: {
    make_title: function(mp) {
      if (mp.get("is_lv94") == false) {
        return mp.get("name") + "　 (下位)"
      } else {
        return mp.get("name")
      }
    },
    show_detail_dialog: function(setmp) {
      const items_list = setmp.get("content_items")
      const card_header = setmp.get("header_info")
      this.$refs.child_Dialogue.open( card_header.get("name") , items_list)
    },
    arrange_cont_items_list: function(head_mp, cont_list) {
      let mapped_cont = new Map()
      const parts_list = head_mp.get("contained_parts").split(",").map(prt => prt.trim())
      parts_list.forEach( part => {
        const default_map = new Map([
          ["name", ""], ["part", part], ["owned", false], ["icon", "check_box_outline_blank"] 
        ])
        mapped_cont.set( part, default_map )
      })
      let count = 0
      cont_list.forEach(itm => {
        let itm_map = new Map([...Object.entries(itm)])
        let part_name = ""
        let sml_cls = itm_map.get("item_small_class")
        if ( parts_list.includes(sml_cls + "(1)") ) {
          count += 1
          part_name = sml_cls + "(" + count.toString(10) +")"
        } else {
          part_name = sml_cls
        }
        itm_map.delete("item_small_class")
        itm_map.set("part", part_name )
        itm_map.set("owned", true)
        itm_map.set("icon", "check_box")
        mapped_cont.set( part_name, itm_map)
      })
      return [...mapped_cont.values()]
    },
    APIList_to_cardmaps: function (obj_lis) {
      let cardmaps_list = []
      obj_lis.forEach( obj => {
        let mp = new Map([...Object.entries(obj)])
        let head_mp = new Map( [...Object.entries( mp.get("header_info") )] )
        let conts_list = mp.get("content_items")
        let arranged_cont = this.arrange_cont_items_list(head_mp, conts_list)
        mp.set( "header_info", head_mp)
        mp.set( "content_items", arranged_cont)
        cardmaps_list.push( mp )
      })
      return cardmaps_list
    }
  },
  mounted: function () {
    console.log('mounted')
    axios.get('/api/item_sets/')
      .then((response) => {
        this.itemset_map_list = this.APIList_to_cardmaps(response.data)
        console.log(this.itemset_map_list)
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>
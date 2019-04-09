<template>
  <v-container>
  <app-dialogue ref="child_Dialogue"></app-dialogue>
    <v-layout row grid-list-lg justify-start align-center wrap>
        <v-flex md4 v-for="setmap of itemset_list" :key="setmap.get('name')" >
          <v-card max-height="190px" min-height="150px"
            max-width="330px" @click="show_detail_dialog(setmap)">
            <v-card-title class="title mb-0 pb-0">
                {{ make_title(setmap) }}
            </v-card-title>
            <v-card-text>
              <div v-for="map of pickup_items_map(setmap)" :key="map.get('part')">
                <v-icon>{{map.get('icon')}}</v-icon> {{map.get("part")}}
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
      itemset_list: [],
      items_maps_map: new Map()
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
    pickup_items_map: function(setmp) {
      return this.items_maps_map.get( setmp.get("name") )
    },
    make_items_map: function(mp) {
      let items_map = new Map()
      const contained_part_list = mp.get("contained_parts").split(",").map(prt => prt.trim())
      contained_part_list.forEach( part => {
        let default_map = new Map([
            ["id", ""], ["item_place", ""], ["name", ""], ["part", part],
            ["owned", false], ["icon", "check_box_outline_blank"] 
        ])
        items_map.set( part, default_map )
      })
      let count = 0
      mp.get("owned_parts_ITEMLIST").forEach(itm => {
        let part_name = ""
        let sml_cls = itm.get("item_small_class")
        if ( contained_part_list.includes(sml_cls + "(1)") ) {
          count += 1
          part_name = sml_cls + "(" + count.toString(10) +")"
        } else {
          part_name = sml_cls
        }
        itm.delete("item_small_class")
        itm.set( "part", part_name )
        itm.set("owned", true)
        itm.set("icon", "check_box")
        items_map.set( part_name, itm)
      })
      return [ mp.get("name"), [...items_map.values()] ]
    },
    show_detail_dialog: function(setmp) {
      let detail_mps = this.items_maps_map.get( setmp.get("name") )
      this.$refs.child_Dialogue.open( setmp.get("name") , detail_mps)
    },
    make_maps_with_nest: function (obj) {
      let replaced_map = new Map()
      Object.entries(obj).map( ([key,val]) => {
        if (key.includes("ITEMLIST")) {
          let new_list = val.map( itm => new Map( Object.entries(itm) ) )
          replaced_map.set( key, new_list )
        } else {
          replaced_map.set( key, val )
        }
      })
      return replaced_map
    },
    APIList_to_map: function (lis) {
      return lis.map( itm => this.make_maps_with_nest(itm) )
    }
  },
  mounted: function () {
    console.log('mounted')
    axios.get('/api/item_sets/')
      .then((response) => {
        this.itemset_list = this.APIList_to_map(response.data)
        this.items_maps_map = new Map(
          this.itemset_list.map(mp => this.make_items_map(mp))
        )
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>
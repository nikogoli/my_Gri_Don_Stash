<template>
    <v-layout row grid-list-lg justify-start align-center wrap>
        <v-flex md4 v-for="set of itemset_list" :key="set.name" >
          <v-card max-height="190px" min-height="150px"
            max-width="330px" @click="show_detail_dialog(set)">
            <v-card-title class="title mb-0 pb-0">
                {{ make_title(set) }}
            </v-card-title>
            <v-card-text>
              <div v-for="row of make_check_list(set)" :key="row.get('part')">
                <v-icon>{{row.get('icon')}}</v-icon> {{row.get("part")}}
              </div>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import axios from 'axios'
import DialogHelper from '@/components/DialogHelper.js'

export default {
  name: 'Setitem_List',
  data () {
    return {
      itemset_list: []
    }
  },
  methods: {
    make_title: function(dic) {
      if (dic.is_lv94 == false) {
        return dic.name + "　 (下位)"
      } else {
        return dic.name
      }
    },
    make_check_list: function(dic) {
      let item_dic = new Map()
      const contained_part_list = dic.contained_parts.split(",").map(prt => prt.trim())
      let count = 0
      let sml_cls = ""
      for (let part of contained_part_list) {
        item_dic.set( part, 
            new Map([
              ["part", part],
              ["item", ""],
              ["owned", false],
              ["icon", "check_box_outline_blank"]
            ])
        )
      }
      for (let itm of dic.owned_parts) {
        if ( contained_part_list.includes(itm.item_small_class + "(1)") ) {
          count += 1
          sml_cls = itm.item_small_class + "(" + count.toString(10) +")"
        } else {
          sml_cls = itm.item_small_class
        }
        item_dic.set( sml_cls, 
          new Map([
            ["part", sml_cls], ["item", itm.name], 
            ["owned", true], ["icon", "check_box"]
          ])
        )
      }
      return item_dic.values()
    },
    show_detail_dialog: function(dic) {
      let dialog_txt = ""
      for (let row of this.make_check_list(dic)) {
        dialog_txt += row.get("part") + ":\t " + row.get("item") + "\n"
      }
      console.log(dialog_txt)
      DialogHelper.showDialog(this, {
        subject: dic.name,
        message: dialog_txt,
        ok: () => { console.log('click ok') },
        cancel: () => { console.log('click cancel') }
      })
    }
  },
  mounted: function () {
    console.log('mounted')
    axios.get('/api/item_sets/')
      .then((response) => {
        this.itemset_list = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>
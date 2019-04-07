<template>
    <v-layout column justify-start align-center wrap>
        <v-flex v-for="item in item_list" :key=item.id >
          <v-card>
            <v-card-title>
              <span class="headline">
                {{ item.name }}
              </span>
            </v-card-title>
            <v-card-text>
              <blockquote>
                部位：{{ item.item_small_class }}　(セット装備：{{item.is_set}})  倉庫の場所：{{item.item_place}}
                <footer></footer>
              </blockquote>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import axios from 'axios'

export default {
  name: 'ItemList',
  data () {
    return {
      item_list: []
    }
  },
  mounted: function () {
    console.log('mounted')
    // APIを叩く。
    // 開発サーバで動作中はちゃんとDjangoの8000番ポートを叩いてくれます。
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
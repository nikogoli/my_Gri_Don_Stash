<template>
  <div id="app">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <v-app id="sidenavi">
      <v-navigation-drawer fixed permanent width="200" app>
        <v-toolbar flat>
          <v-list>
            <v-list-tile>
              <v-list-tile-title class="title">
                Item List for GD
              </v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-toolbar>
        <v-divider></v-divider>
        <v-list dense class="pt-0">
          <v-list-tile>
            <v-list-tile-content>
              <v-list-tile-title>
                <router-link to="/item_table">アイテム表</router-link>
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile>
            <v-list-tile-content>
              <v-list-tile-title>
                <router-link to="/LargeClassList">大分類</router-link>
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile>
            <v-list-tile-content>
              <v-list-tile-title>
                <router-link to="/SetItemList">セット装備</router-link>
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>          
        </v-list>
      </v-navigation-drawer>
      <v-content>
        <router-view></router-view>
      </v-content>
    </v-app>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>

export default {
  name: 'app',
  components: {}
}
</script>

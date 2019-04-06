import Vue from 'vue'
import Router from 'vue-router'
import ItemList from '@/components/ItemList'
import LargeClassList from '@/components/LargeClassList'
import SetItemList from '@/components/SetItemList'
import Item_Table from '@/components/Item_Table'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/ItemList',
      name: 'ItemList',
      component: ItemList
    },
    {
    	path: '/LargeClassList',
    	name: 'LargeClassList',
    	component: LargeClassList
    },
    {
      path: '/SetItemList',
      name: 'SetItemList',
      component: SetItemList
    },
    {
      path: '/item_table',
      name: 'Item_Table',
      component: Item_Table
    },
  ]
})

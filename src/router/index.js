import Vue from 'vue'
import Router from 'vue-router'
import ItemList from '@/components/ItemList'
import LargeClassList from '@/components/LargeClassList'
import Setitem_List from '@/components/Setitem_List'
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
      path: '/Setitem_List',
      name: 'Setitem_List',
      component: Setitem_List
    },
    {
      path: '/item_table',
      name: 'Item_Table',
      component: Item_Table
    },
  ]
})

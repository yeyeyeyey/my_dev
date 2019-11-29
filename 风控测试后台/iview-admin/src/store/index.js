import Vue from 'vue'
import Vuex from 'vuex'

import user from './module/user'
import app from './module/app'
import fielddconfig from './module/fielddconfig'
import mockconfig from './module/mockconfig'
import resultdisplay from './module/resultdisplay'
import rerun from './module/rerun'
import schedule from './module/schedule'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    //
  },
  mutations: {
    //
  },
  actions: {
    //
  },
  modules: {
    user,
    app,
    fielddconfig,
    mockconfig,
    resultdisplay,
    rerun,
    schedule
  }
})

import {
  getStrategys,
  addStrategy,
  deleteStrategy,
  saveStrategy,
  deleteField,
  updateIdCard
} from '@/api/fieldconfig'
// import { setToken, getToken } from '@/libs/util'

export default {
  state: {
    items: [],
    tittle: '123',
    activeId: ''
  },
  mutations: {

    setItems (state, items) {
      state.items = items
    },
    addStrategy (state, strategy) {
      state.items.push(strategy)
    },
    deleteByIndex (state, index) {
      state.items.splice(index, 1);
    },
    setTittle (state, tittle) {
      state.tittle = tittle
    },
    setActiveID (state, activeId) {
      state.activeId = activeId
    }
  },

  actions: {
    getStrategys ({ commit }) {
      return new Promise((resolve, reject) => {
        getStrategys().then(res => {
          const data = res.data
          // console.log(data)
          commit('setItems', data)
          resolve()
        }).catch(err => {
          reject(err)
        })
      })
    },
    // 重置身份证
    updateIdCard ({ commit }, data) {
      return new Promise((resolve, reject) => {
        // console.log(data)
        updateIdCard(data).then(res => {
          // const data = res.data
          // console.log("----"+data)
          // commit('identityID', data)
          resolve()
        }).catch(err => {
          reject(err)
        })
      })
    },

    addStrategy ({ commit }, strategy) {
      return new Promise((resolve, reject) => {
        addStrategy(strategy).then(res => {
          const data = res.data
          // console.log(data)
          commit('setItems', data)
          resolve()
        }).catch(err => {
          reject(err)
        })
      })
    },
    deleteStrategy ({ commit }, strategy) {
      return new Promise((resolve, reject) => {
        deleteStrategy(strategy).then(res => {
          const data = res.data
          // console.log(data)
          commit('setItems',data)
          resolve()
        }).catch(err => {
          reject(err)
        })
      })
    },
    saveStrategy({ commit }, strategy){
      // console.log("vuex:");
      // console.log(strategy)
      return new Promise((resolve, reject) => {
        saveStrategy(strategy).then(res => {
          const data = res.data
          // console.log("vuex:");
          // console.log(data)
          commit('setItems',data)
          resolve()
        }).catch(err => {
          reject(err)
        })
      })
    },
    deleteField ({ commit }, field){
      // console.log("vuexfield:");
      // console.log(field)
      return new Promise((resolve, reject) => {
        deleteField(field).then(res => {
          const data = res.data
          // console.log("vuex:");
          // console.log(data)
          // commit('setItems',data)
          resolve()
        }).catch(err => {
          reject(err)
        })
      })
    },

  }
}

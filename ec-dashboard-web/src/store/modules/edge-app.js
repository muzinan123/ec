import {
  fetchList,
  fetchItem,
  deleteApp

} from '@/api/edge-app'

const state = {
  name: ''
}
const mutations = {
  SET_APPNAME: (state, name) => {
    state.name = name
  }
}
const actions = {
  //应用列表
  getAppList({}) {
    return new Promise((resolve, reject) => {
      fetchList().then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  //应用详情
  getAppItem({ commit, state }) {
    return new Promise((resolve, reject) => {
      fetchItem(state.name).then(response => {
        resolve(response)
        commit('SET_APPNAME', '')
      }).catch(error => {
        reject(error)
      })
    })
  },
  //删除应用
  deleteApp({ commit, state }) {
    return new Promise((resolve, reject) => {
      let params = {
        'pod_name': state.name
      }
      deleteApp(params).then(response => {
        commit('SET_APPNAME', '')
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  setAppName({ commit, state }, name) {
    return new Promise(resolve => {
      commit('SET_APPNAME', name)
      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}

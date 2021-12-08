import { loginByUsername } from '@/api/login'
import { registerByUsername } from '@/api/register'
import { getHistoryMsg, addHistoryMsg, delHistoryMsg } from '@/api/msg'
import { adddynamic, getHistoryDynamic, addHistoryComment } from '@/api/dynamic'
import { setUserName } from '@/utils/localStorage'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 存放用户连接
    socket: '',
    // 存放历史记录
    msgHistory: {
      info: [],
      allmessage: []
    },
    dynamicHistory: {
      info: [],
      allmessage: []
    },
    // 存放房间信息，为了方便以后做多房间
    roomDetail: {
      id: '',
      users: {},
      info: []
    }
  },

  getters: {
    getSocket: state => state.socket,
    getUsers: state => state.roomDetail.users,
    getInfo: state => state.roomDetail.info,
    getMsgHistoryInfo: state => state.msgHistory.info,
    getDynamicsHistoryInfo: state => state.dynamicHistory.info
  },

  mutations: {
    SET_SOCKET (state, socket) {
      state.socket = socket
    },
    SET_USERS: (state, user) => {
      state.roomDetail.users = user
    },
    ADD_ROOM_DETAIL_INFO: (state, info) => {
      state.roomDetail.info.push(info)
    },
    SET_ROOM_DETAIL_INFO: (state) => {
      state.roomDetail.info = []
    },
    SET_MSG_HISTORY_INFO: (state, info) => {
      state.msgHistory.info = info
    },
    SET_DYNAMICS_HISTORY_INFO: (state, info) => {
      state.dynamicHistory.info = info
    },
    DEL_ROOM_DETAIL_INFO: (state, info) => {
      state.roomDetail.info.map((val, i) => {
        if (JSON.stringify(val) === JSON.stringify(info)) {
          state.roomDetail.info.splice(i, 1)
          console.log('delok')
          return new Promise((resolve, reject) => {
            delHistoryMsg(info).then(response => {
              resolve()
            }).catch(error => {
              reject(error)
            })
          })
        }
      })
    }
  },

  actions: {
    LoginByUsername ({ commit }, userInfo) {
      const username = userInfo.username.trim()
      return new Promise((resolve, reject) => {
        loginByUsername(username, userInfo.password).then(response => {
          const data = response.data
          console.log(data.msg)
          if (data.msg === '登录成功') {
            commit('SET_USERS', data.username)
            setUserName(data.username)
            resolve()
          } else {
            alert('登录失败，请检查用户名或密码！')
          }
        }).catch(error => {
          reject(error)
        })
      })
    },
    RegisterByUsername ({ commit }, userInfo) {
      const username = userInfo.username.trim()
      return new Promise((resolve, reject) => {
        registerByUsername(username, userInfo.password).then(response => {
          const data = response.data
          if (data.msg === '注册成功') {
            commit('SET_USERS', data.username)
            setUserName(data.username)
            resolve()
            alert(data.msg)
          } else {
            alert('您的用户名已被使用！')
          }
        }).catch(error => {
          reject(error)
        })
      })
    },
    SetWebSocket ({ commit }, wsocket) {
      commit('SET_SOCKET', wsocket)
    },
    GetMessHistory ({ commit }) {
      return new Promise((resolve, reject) => {
        getHistoryMsg().then(response => {
          const data = response.data
          commit('SET_MSG_HISTORY_INFO', data)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    GetDynamicsHistory ({ commit }) {
      return new Promise((resolve, reject) => {
        getHistoryDynamic().then(response => {
          const data = response.data
          commit('SET_DYNAMICS_HISTORY_INFO', data)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    AddMessHistory ({ commit }, data) {
      return new Promise((resolve, reject) => {
        addHistoryMsg(data).then(response => {
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    AddCommentHistory ({ commit }, data) {
      return new Promise((resolve, reject) => {
        addHistoryComment(data).then(response => {
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    Adddynamic ({ commit }, data) {
      return new Promise((resolve, reject) => {
        adddynamic(data).then(response => {
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    AddChatMsg ({ commit }, msg) {
      commit('ADD_ROOM_DETAIL_INFO', msg)
    },
    SetChatMsg ({ commit }) {
      commit('SET_ROOM_DETAIL_INFO')
    },
    DelChatMsg ({ commit }, msg) {
      commit('DEL_ROOM_DETAIL_INFO', msg)
    }
  }
})

// store/modules/auth.js

const state = {
    token: localStorage.getItem('token') || '',
  }
  
  const getters = {
    token: state => state.token,
    isAuthenticated: state => !!state.token,
  }
  
  const actions = {
    login({ commit }, token) {
      commit('setToken', token)
    },
    logout({ commit }) {
      commit('clearToken')
    },
  }
  
  const mutations = {
    setToken(state, token) {
      state.token = token
      localStorage.setItem('token', token)
    },
    clearToken(state) {
      state.token = ''
      localStorage.removeItem('token')
    },
  }
  
  export default {
    state,
    getters,
    actions,
    mutations,
  }
  
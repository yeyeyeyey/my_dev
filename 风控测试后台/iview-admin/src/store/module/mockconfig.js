import {
    getMockconfigs,
    postMockconfig,
    deleteMockconfig,
    getCurrentOutputsJson,
    postCurrentOutputsJson,
    postGitpushmock,
    getMockhistory,
    postMockhistory,
    deleteMockhistory,
    searchExecution
} from '@/api/mockconfig'


export default {
    state: {
        mockItems: [],
        mockHistory: [],
        tittle: '123',
        activeId: '',
        currentOutputsJson: '',
        cid: '',
        execute_action: '',
        mockConfig: '',
        combineJson: '',
        checkAllGroup: [],
        execute_action_list: []
    },
    getters: {
    },
    mutations: {

        setMockItems(state, mockItems) {
            state.mockItems = mockItems
        },
        setActiveID(state, activeId) {
            state.activeId = activeId
        },
        deleteItem(state, id) {
            var index = state.mockItems.findIndex(item => item.id === id)
            state.mockItems.splice(index, 1)
        },
        setCurrentOutputsJson(state, value) {
            state.currentOutputsJson = value
        },
        setCid(state, value) {
            state.cid = value
        },
        setExecuteAction(state, value) {
            state.execute_action = value
        },
        setMockConfig(state, value) {
            state.mockConfig = value
        },
        setCombineJson(state, value) {
            state.combineJson = value;
        },
        setMockHistory(state, mockHistory) {
            state.mockHistory = mockHistory;
        },
        addExecute_action_list(state, execute_action_list_item) {
                state.execute_action_list.push(execute_action_list_item)
        },
        setExecute_action_list(state, execute_action_list) {
            state.execute_action_list = execute_action_list
        }

    },
    actions: {
        getMockhistory({ commit }) {
            return new Promise((resolve, reject) => {
                getMockhistory().then(res => {
                    const data = res.data
                    // console.log("getMockhistory:")
                    // console.log(data)
                    commit('setMockHistory', data)
                    console.log("getMockhistory:")
                    console.log(data)
                    resolve()
                }).catch(err => {
                    reject(err)
                })
            })
        },
        saveMockhistory({ commit }, Mockhistory) {
            console.log("Mockhistory:")
            console.log(Mockhistory)
            return new Promise((resolve, reject) => {
                postMockhistory(Mockhistory).then(res => {
                    const data = res.data
                    console.log(Mockhistory)
                    commit('setMockHistory', data)
                    resolve(data)
                }).catch(err => {
                    reject(err)
                })
            })
        },
        deleteMockhistory({ commit }, Mockhistory) {
            // console.log(" deleteMockhistory:Mockhistory:")
            console.log(Mockhistory)
            return new Promise((resolve, reject) => {
                deleteMockhistory(Mockhistory).then(res => {
                    const data = res.data
                    console.log(data)
                    commit('setMockHistory', data)
                    resolve()
                }).catch(err => {
                    reject(err)
                })
            })
        },


        getMockconfigs({ commit }) {
            return new Promise((resolve, reject) => {
                getMockconfigs().then(res => {
                    const data = res.data
                    // console.log("getMockconfigs:")
                    // console.log(data)
                    commit('setMockItems', data)
                    resolve()
                }).catch(err => {
                    reject(err)
                })
            })
        },
        saveMockconfig({ commit }, mockconfig) {
            return new Promise((resolve, reject) => {
                postMockconfig(mockconfig).then(res => {
                    const data = res.data
                    // console.log(data)
                    commit('setMockItems', data)
                    resolve(data)
                }).catch(err => {
                    reject(err)
                })
            })
        },
        deleteMockconfig({ commit }, mockconfig) {
            // console.log(" deleteMockconfig:mockconfig:")
            console.log(mockconfig)
            return new Promise((resolve, reject) => {
                deleteMockconfig(mockconfig).then(res => {
                    const data = res.data
                    console.log(data)
                    commit('setMockItems', data)
                    resolve()
                }).catch(err => {
                    reject(err)
                })
            })
        },

        getCurrentOutputsJson({ commit }) {
            return new Promise((resolve, reject) => {
                getCurrentOutputsJson().then(res => {
                    const data = res.data
                    // console.log(data)
                    commit('setCurrentOutputsJson', data)
                    resolve()
                }).catch(err => {
                    reject(err)
                })
            })
        },
        postCurrentOutputsJson({ commit }, data) {
            return new Promise((resolve, reject) => {
                postCurrentOutputsJson(data).then(res => {
                    const data = res.data
                    // console.log(data)
                    var newJson = JSON.stringify(JSON.parse(data), '', 4)
                    // console.log(newJson)
                    commit('setCurrentOutputsJson', newJson)
                    resolve()
                }).catch(err => {
                    reject(err)
                })
            })
        },
        gitPushMock({ state, commit },data) {
            return new Promise((resolve, reject) => {

                var jenkinsJob = (data.decisionName == 'lc-decision' ? 'modify-mock-config-lc' : 'modify-mock-config')
                console.log('jenkinsJob:')
                console.log(jenkinsJob)
                console.log('gitPushMock:')
                console.log(data)
                postGitpushmock(jenkinsJob,data).then(res => {
                    const data = res.data
                    // console.log(data)
                    // commit('setCurrentOutputsJson', newJson)
                    resolve()
                }).catch(err => {
                    reject(err)
                })
            })
        },
        searchExecution({ state, commit }, key) {
            var data = {
                key: key
            }
            return new Promise((resolve, reject) => {
                console.log("data:")
                console.log(data)
                searchExecution(data).then(res => {
                    console.log(res.data)
                    if (res.data) {
                        commit('setExecute_action_list', res.data)
                    }
                }).catch(err => {
                    reject(err)
                })
            })
        }
    }
}
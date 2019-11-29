import {
    createTask,
    getTaskList,
    getTaskCount,
    getTaskListPool,
    getTaskCountPool
  } from '@/api/schedule'

export default {
    state: {
        formValidate: {
            task_id: '',
            task_name: '',
            task_type_id: '',
            task_cycle: '',
            task_status:'',
            due_mi: '',
            due_hh: '',
            due_dd: '',
            due_wd: '',
            frequency: '',
            create_user: '',
            update_user: '',
            prop_name: '',
            prop_value: '',
            parent_task_id: ''
        },
        tTaskCount: 0,
        tTaskCurrent: 1,
        tTaskData: [],
        tTaskCountPool: 100,
        tTaskCurrentPool: 1,
        tTaskDataPool: [],
    },
    mutations: {
        setFormValidate(state, value){
            state.formValidate = value;
        },
        setTaskCount(state, value){
            state.tTaskCount = value;
        },
        setTaskCurrent(state, value){
            state.tTaskCurrent = value;
        },
        setTaskData(state,value){
            state.tTaskData = value;
        },
        setTaskCountPool(state, value){
            state.tTaskCountPool = value;
        },
        setTaskCurrentPool(state, value){
            state.tTaskCurrentPool = value;
        },
        setTaskDataPool(state,value){
            state.tTaskDataPool = value;
        }
    },
    actions: {
        postTask ({ state,commit }) {
            return new Promise((resolve, reject) => {
              createTask(state.formValidate).then(res => {
                  console.log(state.formValidate)
                const data = res.data
                // console.log("getMockconfigs:")
                // console.log(data)
                // commit('setMockItems', data)
                resolve(data)
              }).catch(err => {
                reject(err)
              })
            })
        },
        getTaskList ({ state,commit }) {
            return new Promise((resolve, reject) => {
              getTaskList(state.tTaskCurrent).then(res => {
                const data = res.data
                console.log("getTaskList:")
                console.log(data)
                commit('setTaskData', data)
                resolve(data)
            }).catch(err => {
                reject(err)
                })
            })
        },   
        getTaskCount ({ state,commit }) {
            return new Promise((resolve, reject) => {
              getTaskCount().then(res => {
                const data = res.data
                // console.log("getTaskCount:")
                // console.log(data['T_TASK_COUNT'])
                commit('setTaskCount', parseInt(data['T_TASK_COUNT']))
                resolve(data)
            }).catch(err => {
                reject(err)
                })
            })
        },  
        getTaskListPool ({ state,commit }) {
            return new Promise((resolve, reject) => {
              getTaskListPool(state.tTaskCurrentPool).then(res => {
                const data = res.data
                console.log("getTaskList:")
                console.log(data)
                commit('setTaskDataPool', data)
                resolve(data)
            }).catch(err => {
                reject(err)
                })
            })
        },   
        getTaskCountPool ({ state,commit }) {
            return new Promise((resolve, reject) => {
              getTaskCountPool().then(res => {
                const data = res.data
                // console.log("getTaskCount:")
                // console.log(data['T_TASK_COUNT'])
                commit('setTaskCountPool', parseInt(data['T_TASK_POOL_COUNT']))
                resolve(data)
            }).catch(err => {
                reject(err)
                })
            })
        },   
    }
}
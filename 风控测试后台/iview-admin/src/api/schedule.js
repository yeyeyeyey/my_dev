import axios from '@/libs/api.request'

export const createTask = (data) => {
    return axios.request({
        url: 'api/v1/task/insert',
        method: 'post',
        data:data
    })
}
export const getTaskList = (pageNo) => {
    return axios.request({
        url: 'api/v1/task/getTask',
        method: 'get',
        params: {
            pageNo
        }
    })
}
export const getTaskCount = () => {
    return axios.request({
        url: 'api/v1/task/getTaskCount',
        method: 'get',
    })
}
export const getTaskListPool = (pageNo) => {
    return axios.request({
        url: 'api/v1/task/getTaskPool',
        method: 'get',
        params: {
            pageNo
        }
    })
}
export const getTaskCountPool = () => {
    return axios.request({
        url: 'api/v1/task/getTaskPoolCount',
        method: 'get',
    })
}
import axios from '@/libs/api.request'

export const getStrategys = () => {
  return axios.request({
    url: 'api/strategy/',
    method: 'get'
  })
}
export const addStrategy = (strategy) => {
  return axios.request({
    url: 'api/strategy/',
    method: 'post',
    data: strategy
  })
}
export const deleteStrategy = (strategy) => {
  return axios.request({
    url: 'api/strategy/',
    method: 'post',
    data: strategy
  })
}
export const saveStrategy = (strategy) => {
  return axios.request({
    url: 'api/strategy/',
    method: 'post',
    data: strategy
  })
}
export const deleteField = (field) => {
  return axios.request({
    url: 'api/strategyfield/',
    method: 'delete',
    data: field
  })
}

// export const login = ({ userName, password }) => {
//   const data = {
//     userName,
//     password
//   }
//   return axios.request({
//     url: 'login',
//     data,
//     method: 'post'
//   })
// }

// 重置身份证
export const updateIdCard = (field) => {
  return axios.request({
    url: 'api/updatedb/',
    method: 'post',
    data: field
  })
}


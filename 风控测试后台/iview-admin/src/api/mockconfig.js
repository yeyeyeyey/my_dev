import axios from '@/libs/api.request'
import qs from 'qs' // qs在安装axios后会自动安装，只需要组件里import一下即可


export const getMockhistory = () => {
  return axios.request({
    url: 'api/mockhistory/',
    method: 'get'
  })
}

export const postMockhistory = (mockhistory) => {
  return axios.request({
    url: 'api/mockhistory/',
    method: 'post',
    data: mockhistory

  })
}

export const deleteMockhistory = (mockhistory) => {
  return axios.request({
    url: 'api/mockhistory/',
    method: 'delete',
    data: mockhistory
  })
}

export const getMockconfigs = () => {
  return axios.request({
    url: 'api/mockconfig/',
    method: 'get'
  })
}

export const postMockconfig = (mockconfig) => {
  return axios.request({
    url: 'api/mockconfig/',
    method: 'post',
    data: mockconfig

  })
}

export const deleteMockconfig = (mockconfig) => {
  return axios.request({
    url: 'api/mockconfig/',
    method: 'delete',
    data: mockconfig
  })
}


export const getCurrentOutputsJson = () => {
  return axios.request({
    url: "api/currentoutputsjson/",
    method: 'get',
  })
}

export const postCurrentOutputsJson = (data) => {
  return axios.request({
    url: 'api/currentoutputsjson/',
    method: 'post',
    data: data

  })
}

// export const postGitpushmock = (testEnv,mockText) => {
//   return axios.request({
//     // url: 'jenkins/job/modify-mock-config/buildWithParameters',
//     url: 'api/jenkins/gitpushmock/',
//     method: 'post',
//     data: qs.stringify({
//       testEnv: testEnv,
//       mockText:mockText
//     }),
//     auth: {
//       username: 'fengyu',
//       password: 'eLoG1KL9'
//     },
//   })
// }

export const postGitpushmock = (jobName, params) => {
  return axios.request({
    url: 'api/jenkins/job/triger/',
    // url: 'api/gitpushmock/',
    method: 'post',
    // resolveWithFullResponse: true,
    data: {
      jobName: jobName,
      params: qs.stringify(params)
      // params: params

    }
  })
}

export const searchExecution = (data) => {
  return axios.request({
    url: 'api/search/execution/',
    method: 'post',
    data: data
  })
}



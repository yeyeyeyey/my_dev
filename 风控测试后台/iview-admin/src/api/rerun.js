import axios from '@/libs/api.request'
import qs from 'qs' // qs在安装axios后会自动安装，只需要组件里import一下即可

export const postReportList = (data) => {
  return axios.request({
    url: 'api/reportlist/',
    method: 'post',
    data:data
  })
}

export const getReportList = () => {
  return axios.request({
    url: 'api/reportlist/',
    method: 'get',
  })
}


export const getReportDetail = (id) => {
  return axios.request({
    url: `api/reportlist/${id}/`,
    method: 'get',
  })
}

export const checkApply = (data) => {
  return axios.request({
    url: 'api/checkapply/',
    method: 'post',
    data:data
  })
}

export const publishSqs = (data) => {
  return axios.request({
    url: 'api/publishsqs/',
    method: 'post',
    data:data
  })
}

export const s3Upload = (data) => {
  console.log(data)
  let fd = new FormData();
  fd.append('file',data.file)
  fd.append('bucket_name',data.bucketName)
  fd.append('key',data.key)
  return axios.request({
    url: 'api/upload/',
    // url: 'api/gitpushmock/',
    method: 'post',
    data: fd,
    auth:{
      username: 'admin',
      password: 'password123'
    },
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}
export const s3Download = (data) => {
  console.log(data)
  let fd = {
    bucket_name:data.bucketName,
    key:data.key
  };
  return axios.request({
    url: 'api/download/',
    // url: 'api/gitpushmock/',
    method: 'get',
    params:fd
  })
}


export const createIncomData = (jobName,params) => {
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

export const checkLastBuild = (jobName) => {
  return axios.request({
    url: 'api/jenkins/job/checkstatus/lastbuild/',
    method: 'post',
    data:{
      jobName:jobName
    }
  })
}

export const checkBuild = (jobName,id) => {
  return axios.request({
    url: "api/jenkins/job/checkstatus/id/",
    method: 'post',
    data: {
      jobName,jobName,
      id: id
    }
  })
}
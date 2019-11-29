import {
    postReportList,
    getReportList,
    getReportDetail,
    checkApply,
    publishSqs,
    s3Upload,
    s3Download,
    createIncomData,
    checkLastBuild,
    checkBuild
} from '@/api/rerun'

export default {
    state: {
        formItem: {
            reportTittle: '',
            sqs: 'kr-underwriter-batch-apiSalvationFail-kr-test1',
            options: ['kr-underwriter-batch-apiSalvationFail-kr-test1', 'kr-underwriter-batch-apiPatchSalvationFail-kr-test1'],
            cid: '',
            reportId: '',
            oldCid: '',
            oldTitle: '',
            something: ''
        },
        title: '',
        cid: '',
        reportList: [],
        //  报告包含的策略包
        content: {},
        reportfileds: [],
        activeReportStrategy: {},
        checkApplyData: [],
        s3FormItem: {
            bucketName: 'mm-kr-test',
            key: 'test1/credit/partner/QIDAI/2019/01/07/201901070000000131231546846487226',
            file: null,
            downloadLoading: false,
            uploadLoading: false
        },
        incomeData: {
            phone: '',
            name: '陈华景',
            idNum: '440881198911093616',
            issuingAuthority: '廉江市公安局',
        },
        jenkinsJobStatus: {
            building: false,
            id: '',
            queueId: '',
            result: '',
            description: ''
        },
        queueId: '',
        incoming: false

    },
    mutations: {
        setTitle(state, value) {
            state.title = value;
        },
        setCid(state, value) {
            state.cid = value;
        },
        setFormItem(state, value) {
            state.formItem = value;
        },
        setReportList(state, value) {
            state.reportList = value;
        },
        setContent(state, value) {
            if (value) {
                console.log(value)
                state.content = JSON.parse(value);
            }
        },
        setReportFileds(state, value) {
            state.reportfileds = value;
        },
        setActiveReportStrategy(state, value) {
            state.reportfileds = value;
        },
        setCheckApplyData(state, value) {
            state.checkApplyData = value;
        },
        setS3FormItem(state, value) {
            state.s3FormItem = value;
        },
        setIncomeData(state, value) {
            state.incomeData = value;
        },
        setJenkinsJobStatus(state, value) {
            state.jenkinsJobStatus = value
        },
        setQueueId(state, value) {
            state.queueId = value
        },
        setIncoming(state, value) {
            state.incoming = value
        }

    },
    actions: {
        createIncomData({ state, commit }, params) {
            var data = state.incomeData
            console.log(state.incomeData)
            return new Promise((resolve, reject) => {
                createIncomData('create-incoming-data', params).then(res => {
                    const data = res.data
                    console.log("createIncomData:")
                    console.log(data)
                    // commit('setCheckApplyData',data)
                    commit('setQueueId', data)
                    resolve(data)
                }).catch(err => {
                    reject(err)
                })
            })
        },
        checkLastBuild({ state, commit }) {
            return new Promise((resolve, reject) => {
                checkLastBuild('create-incoming-data').then(res => {
                    const data = res.data
                    console.log("checkLastBuild:")
                    console.log(data)
                    commit('setJenkinsJobStatus', JSON.parse(data))
                    resolve(data)
                }).catch(err => {
                    reject(err)
                })
            })
        },
        checkBuild({ state, commit }) {
            return new Promise((resolve, reject) => {
                checkBuild('create-incoming-data', state.jenkinsJobStatus.id).then(res => {
                    const data = res.data
                    console.log("checkBuild:")
                    console.log(data)
                    commit('setJenkinsJobStatus', JSON.parse(data))
                    resolve(data)
                }).catch(err => {
                    reject(err)
                })
            })
        },
        checkApply({ state, commit }, ) {
            var data = state.formItem
            console.log(state.formItem)
            return new Promise((resolve, reject) => {
                checkApply(data).then(res => {
                    const data = res.data
                    console.log("checkApply:")
                    console.log(data)
                    commit('setCheckApplyData', data)
                    resolve(data)
                }).catch(err => {
                    reject(err)
                })
            })
        },
        publishSqs({ state, commit }, ) {
            var data = state.formItem
            console.log(state.formItem)
            return new Promise((resolve, reject) => {
                publishSqs(data).then(res => {
                    resolve(data)
                }).catch(err => {
                    reject(err)
                })
            })
        },
        createReport({ state, commit }, data) {
            return new Promise((resolve, reject) => {
                postReportList(data).then(res => {
                    const data = res.data
                    // console.log("getMockconfigs:")
                    // console.log(data)
                    resolve(data)
                }).catch(err => {
                    reject(err)
                })
            })
        },
        getReportList({ state, commit }, data) {
            return new Promise((resolve, reject) => {
                getReportList(data).then(res => {
                    const data = res.data
                    for (var i = 0, len = data.length; i < len; i++) {
                        data[i].idNumber = i + 1
                        console.log(data[i].idNumber)
                    }
                    console.log(data)
                    commit('setReportList', data);
                    resolve()
                }).catch(err => {
                    reject(err)
                })
            })
        },
        deleteReportList({ state, commit }, reportId) {
            return new Promise((resolve, reject) => {
                var data = JSON.stringify({
                    id: reportId,
                    isDelete: true
                })
                postReportList(data).then(res => {
                    const data = res.data
                    resolve()
                }).catch(err => {
                    reject(err)
                })
            })
        },
        getReportDetail({ state, commit }, id) {
            return new Promise((resolve, reject) => {
                getReportDetail(id).then(res => {
                    const data = res.data
                    console.log(data['content'])
                    commit('setContent', data['content']);
                    commit('setReportFileds', data['reportfileds']);
                    resolve()
                }).catch(err => {
                    reject(err)
                })
            })
        },
        s3Upload({ state, commit }, ) {
            return new Promise((resolve, reject) => {
                s3Upload(state.s3FormItem).then(res => {
                    const data = res.data
                    console.log("data:" + data)
                    resolve(JSON.stringify(data))
                }).catch(err => {
                    reject(err)
                })
            })
        },


        s3Download({ state, commit }, ) {
            return new Promise((resolve, reject) => {
                s3Download(state.s3FormItem).then(res => {
                    const data = res.data
                    console.log(data)
                    resolve(JSON.stringify(data))
                }).catch(err => {
                    reject(err)
                })
            })
        },

    }
}
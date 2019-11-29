<template>
    <div>
        <Row :gutter="14">
            <i-col span="12">
                <Card style="height:400px">
                    <p slot="title">
                        <Icon type="md-albums" /> 进件
                    </p>
    
    
                    <Form :model="incomeData" :label-width="80">
                        <Row :gutter="0">
                            <Col span="9">
                            <FormItem label="手机号" style="width: 300px">
                                <Input v-model="incomeData.phone" placeholder="可以为空，为空时随机生成" />
                            </FormItem>
                            </Col>
                        </Row>
    
                        <Row :gutter="0">
                            <Col span="9">
                            <FormItem label="姓名" :required="true" style="width: 300px">
                                <Input v-model="incomeData.name" placeholder="请输入进件姓名" />
                            </FormItem>
                            </Col>
                        </Row>
                        <Row :gutter="0">
                            <Col span="9">
                            <FormItem label="身份证号" :required="true" style="width: 300px">
                                <Input v-model="incomeData.idNum" placeholder="请输入进件身份证号" />
                            </FormItem>
                            </Col>
                        </Row>
                        <Row :gutter="0">
                            <Col span="9">
                            <FormItem label="签发机关" :required="true" style="width: 300px">
                                <Input v-model="incomeData.issuingAuthority" placeholder="请输入进件签发机关" />
                            </FormItem>
                            </Col>
                        </Row>
                        
                        <br>
                        <FormItem>
                            <ButtonGroup>
                                <Button type="primary" :loading="incoming" @click="beginIncomeData"><span v-if="!incoming">开始进件</span><span v-else>进件中...</span></Button>
                            </ButtonGroup>
                        </FormItem>
                    <span v-if='queueId'>id:{{jenkinsJobStatus.id}}；description:{{jenkinsJobStatus.description}}；result:{{jenkinsJobStatus.result}}</span>
                    </Form>
                </Card>
    
    
            </i-col>
             <i-col span="12">
                <Card style="height:400px">
                    <p slot="title">
                        <Icon type="md-albums" /> 上传征信文件
                    </p>
    
    
                    <Form :model="s3FormItem" :label-width="80">
                        <Row :gutter="0">
                            <Col span="9">
                            <FormItem label="存储桶" :required="true">
                                <Input v-model="s3FormItem.bucketName" placeholder="请输入存储桶名称" />
                            </FormItem>
                            </Col>
                        </Row>
    
                        <Row :gutter="0">
                            <Col span="9">
                            <FormItem label="s3路径" :required="true" style="width: 600px">
                                <Input v-model="s3FormItem.key" placeholder="请输入s3路径，不含存储桶" />
                            </FormItem>
                            </Col>
                        </Row>
                        <div>
                            <FormItem label="选择文件" :required="true">
                                <Upload :before-upload="handleUpload" action="">
                                    <Button icon="ios-cloud-upload-outline">Select the file to upload</Button>
                                </Upload>
                            </FormItem>
                            <div v-if="s3FormItem.file !== null">文件: {{ s3FormItem.file.name }}</div>
                            <div v-if="s3FormItem.file == null">未选择文件！</div>
                        </div>
                        <br>
                        <FormItem>
                            <ButtonGroup>
                                <Button type="primary" :loading="s3FormItem.downloadLoading" @click="downCreditFile"><span v-if="!s3FormItem.downloadLoading">下载</span><span v-else>下载...</span></Button>
                                <Button type="primary" :loading="s3FormItem.uploadLoading" @click="uploadCreditFile"><span v-if="!s3FormItem.uploadLoading">上传</span><span v-else>上传...</span></Button>
                            </ButtonGroup>
                        </FormItem>
                    </Form>
                </Card>
    
    
            </i-col>
        </Row>
        <Row :gutter="14">
    
    
        </Row>
    </div>
</template>

<script>
    import {
        mapMutations,
        mapActions,
        mapState,
        mapGetters
    } from 'vuex'
    import jsoneditVue from '../mock-config/jsonedit.vue';
    
    export default {
    
        data() {
            return {
                // s3FormItem: {
                //     bucketName: '',
                //     key: '',
                //     file: null,
                //     downloadLoading: false,
                //     uploadLoading: false
                // },

                m: 0,
                n: 0,
            }
        },
        computed: {
            s3FormItem: {
                get: function() {
                    return this.$store.state.rerun.s3FormItem;
                },
                set: function(newValue) {
                    this.setIncomeData(newValue);
                }
            },
            incomeData:{
                get: function() {
                    return this.$store.state.rerun.incomeData;
                },
                set: function(newValue) {
                    this.setIncomeData(newValue);
                }
            },
            jenkinsJobStatus: {
                get: function() {
                    return this.$store.state.rerun.jenkinsJobStatus;
                },
                set: function(newValue) {
                    this.setJenkinsJobStatus(newValue);
                }
            },
            queueId: {
                get: function() {
                    return this.$store.state.rerun.queueId;
                },
                set: function(newValue) {
                    this.setQueueId(newValue);
                }
            },
            incoming: {
                get: function() {
                    return this.$store.state.rerun.incoming;
                },
                set: function(newValue) {
                    this.setIncoming(newValue);
                }
            },

        },
        methods: {
            ...mapMutations([
                'setS3FormItem',
                'setIncomeData',
                'setJenkinsJobStatus',
                'setQueueId',
                'setIncoming'
            ]),
            ...mapActions([
                's3Upload',
                's3Download',
                'createIncomData',
                'checkLastBuild',
                'checkBuild'
            ]),
            beginIncomeData(){
                this.checkLastBuild().then(res =>{
                    console.log('查询上一次任务成功！')
                }).catch(error => {
                    console.log("查询上一次任务失败！")
                    console.log(error);
                })
                if(this.jenkinsJobStatus.building){
                    this.$Message.error("有任务运行中，请稍后再创建！")
                    console.log("有任务运行中，请稍后再创建！")
                    this.setJenkinsJobStatus({})
                    return
                }
                console.log('this.jenkinsJobStatus:')
                console.log(this.jenkinsJobStatus)
                this.createIncomData(this.incomeData).then(res => {
                    this.$Message.success('创建任务成功！');
                    console.log('创建任务成功！')
                    this.incoming = true
                    this.checkJenkinsJobStatusLast()
                }).catch(error => {
                    this.$Message.error("创建进件任务失败！")
                    console.log(error);
                })
                // this.checkLastBuild()
            },
            checkJenkinsJobStatusById(){
                this.sleep(3000).then(() => {
                    this.checkBuild().then(res => {
                        if (this.jenkinsJobStatus.result){
                            this.incoming = false
                            return
                        }
                        this.checkJenkinsJobStatusById()
                    }).catch(error => {
                        this.$Message.error("查询任务失败！")
                        console.log(error);
                    })
                })
            },
            checkJenkinsJobStatusLast(){
                this.sleep(3000).then(() => {
                        this.checkLastBuild().then(res =>{
                        console.log('查询上一次任务成功！')
                        console.log('this.jenkinsJobStatus:')
                        console.log(this.jenkinsJobStatus)
                        console.log('this.jenkinsJobStatus.queueId:')
                        console.log(this.jenkinsJobStatus.queueId)
                        console.log('this.queueId:')
                        console.log(this.queueId)
                        if(this.jenkinsJobStatus.queueId == this.queueId){
                            this.checkJenkinsJobStatusById()
                        }else{
                            console.log(this.n)
                            if(this.n > 5){
                                this.$Message.error("未找到最后一次构建任务！")
                                return
                            }
                            this.setJenkinsJobStatus({})
                            this.n++
                            this.checkJenkinsJobStatusLast()
                            console.log("queueId不同,无法确定job状态")
                        }
                        }).catch(error => {
                            this.$Message.error("查询上一次任务失败！")
                            console.log(error);
                        })
                    })
            },
            handleUpload(file) {
                this.s3FormItem.file = file;
                return false;
            },
            downCreditFile() {
                this.s3Download().then(res => {
                    this.$Message.success('Success');
                    console.log("res:"+res)
                    let url = window.URL.createObjectURL(new Blob([res]))
                    console.log(url)
                    let link = document.createElement('a')
                    link.style.display = 'none'
                    link.href = url
                    link.setAttribute('download', this.s3FormItem.key.split("/").pop())
                    document.body.appendChild(link)
                    link.click()
                }).catch(error => {
                    this.$Message.error(this.s3FormItem.key.split("/").pop()+"文件不存在！")
                    console.log(error);
                })
            },
            uploadCreditFile() {
                if (this.s3FormItem.file == null) {
                    this.$Message.error("请先选择需要上传的文件！")
                    return
                }
                this.s3FormItem.uploadLoading = true;
                setTimeout(() => {
                    // this.s3FormItem.file = null;
                    this.s3Upload().then(res => {
                        this.$Message.success('Success');
                    }).catch(error => {
                        this.$Message.error('上传失败！请确认s3路径')
                        console.log(error);
                    })
                    this.s3FormItem.uploadLoading = false;
                }, 1500);
    
            },
            sleep (time) {
                return new Promise((resolve) => setTimeout(resolve, time));
            }
        },
        mounted() {
            this.$Message.config({
                top: 50,
                duration: 3
            });
        }
    
    }
</script>



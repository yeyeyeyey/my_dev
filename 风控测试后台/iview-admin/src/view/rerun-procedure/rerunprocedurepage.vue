<template>
    <div>
        <Row :gutter="14">
            <i-col span="12">
                <Card style="height:700px">
                    <p slot="title">
                        <Icon type="md-albums" /> 发Q重跑流程
                    </p>
                    <Form :model="formItem" :label-width="50">
                        <Row :gutter="0">
                            <Col span="15">
                            <FormItem label="SQS">
                                <Select v-model="formItem.sqs"><Option v-for="option in formItem.options" :value="option" :key="option">{{ option}}</Option></Select>
                            </FormItem>
                            </Col>
                        </Row>
                        <Row :gutter="0">
                            <Col span="9">
                            <FormItem label="CID">
                                <Input v-model="formItem.cid" placeholder="请输入cid" />
                            </FormItem>
                            </Col>
                        </Row>
    
    
                        <FormItem>
                            <ButtonGroup>
                                <Button type="primary" :loading="qIsloading" @click="submitQ"> <span v-if="!qIsloading">提交</span>
                                                                  <span v-else>提交...</span></Button>
                                <Button type="primary" :loading="checkIsloading" @click="checkApplyClick">
                                            <span v-if="!checkIsloading">查询审批进度</span>
                                                                  <span v-else>查询审批进度...</span></Button>
                            </ButtonGroup>
                        </FormItem>
                    </Form>
                    <Table :columns="columns1" :data="checkApplyData"></Table>
    
                </Card>
            </i-col>
            <i-col span="12">

                <Card style="height:700px">
                    <p slot="title">
                        <Icon type="md-albums" /> 通过cid创建报告
                    </p>
    
    
                    <Form :model="formItem" :rules="ruleValidate" :label-width="50">
                        <Row :gutter="0">
                            <Col span="9">
                            <FormItem label="标题">
                                <Input v-model="formItem.reportTittle" placeholder="请输入标题" />
                            </FormItem>
                            </Col>
                        </Row>
    
                        <Row :gutter="0">
                            <Col span="9">
                            <FormItem label="CID">
                                <Input v-model="formItem.cid" placeholder="请输入CID" />
                            </FormItem>
                            </Col>
                        </Row>
                        <Row :gutter="0">
                            <Col span="15">
                            <FormItem label="说明">
                                <Input v-model="formItem.something" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="Enter something..."></Input>
                            </FormItem>
                            </Col>
                        </Row>
    
                        <FormItem>
                            <Button type="primary" :loading="loading" @click="submitCid()">                          
                                                                    <span v-if="!loading">提交</span>
                                                                  <span v-else>提交...</span></Button> </FormItem>
                        <label v-if="!formItem.oldCid">通过cid查询报告未创建！</label>
                        <label v-if="formItem.oldCid">通过cid查询{{formItem.oldCid}}发送成功！报告号为：<Button @click="viewReport">{{formItem.reportId}}</Button></label>
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
                ruleValidate: {
                    reportTittle: [{
                        required: true,
                        message: '标题不能为空！',
                        trigger: 'blur'
                    }],
                    cid: [{
                        required: true,
                        message: 'cid不能为空！',
                        trigger: 'blur'
                    }],
                },
                loading: false,
                columns1: [{
                        title: '节点',
                        key: 'execute_action'
                    },
                    {
                        title: '是否通过',
                        key: 'examine_remark'
                    },
                    {
                        title: '操作时间',
                        key: 'operate_time'
                    }
                ],
                qIsloading: false,
                checkIsloading: false
            }
        },
        computed: {
            formItem: {
                get: function() {
                    return this.$store.state.rerun.formItem;
                },
                set: function(newValue) {
                    return this.setFormItem(newValue);
                }
            },
            activeReportStrategy: {
                get: function() {
                    return this.$store.state.rerun.activeReportStrategy;
                },
                set: function(newValue) {
                    this.setActiveReportStrategy(newValue);
                }
            },
            checkApplyData: {
                get: function() {
                    return this.$store.state.rerun.checkApplyData;
                },
            }
        },
        methods: {
            ...mapMutations([
                'setFormItem',
                'setActiveReportStrategy'
            ]),
            ...mapActions([
                'createReport',
                'checkApply',
                'publishSqs'
            ]),
            viewReport() {
                var title = this.formItem.oldTitle ? this.formItem.oldTitle : this.formItem.reportTittle
                console.log("title:")
                console.log(title)
                const route = {
                    name: 'resultdetail',
                    params: {
                        id: this.formItem.reportId,
                        title: title
                    }
                }
                this.$router.push(route)
                // this.activeReportStrategy[id] =[]
                this.$set(this.activeReportStrategy, this.formItem.reportId, [])
            },
            submitQ() {
                this.qIsloading = true
                this.publishSqs().then(res => {
                    this.$Message.success("q发送成功，请检查审批进度")
                    this.qIsloading = false
                }).catch(err => {
                    console.log(err)
                    this.qIsloading = false
                })
            },
            checkApplyClick() {
                this.checkIsloading = true
                this.checkApply().then(res => {
                    this.$Message.success("q发送成功，请检查审批进度")
                    this.checkIsloading = false
                }).catch(err => {
                    console.log(err)
                    this.checkIsloading = false
                })
            },
            submitCid() {
                this.loading = true;
                console.log("title:")
                console.log(this.formItem.reportTittle)
                if (this.formItem.reportTittle == undefined) {
                    this.$Message.error({
                        content: '保存时，标题不能为空',
                        duration: 1
                    })
                    return
                }
                if (this.formItem.cid == undefined) {
                    this.$Message.error({
                        content: '保存时，cid不能为空',
                        duration: 1
                    })
                    return
                }
                var data = JSON.stringify({
                    title: this.formItem.reportTittle,
                    createWay: "通过cid查询",
                    cid: this.formItem.cid
                })
                this.createReport(data).then(res => {
                    this.$Message.success('创建测试报告成功!');
                    console.log(res)
                    this.formItem.reportId = res.id;
                    this.formItem.oldCid = this.formItem.cid;
                    this.formItem.oldTitle = this.formItem.reportTittle;
                    this.loading = false;
                }).catch(err => {
                    console.log(err);
                    this.loading = false;
                })
    
            }
        },
    
    }
</script>



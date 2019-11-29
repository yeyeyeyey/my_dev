<template>
    <div>
        <Row :gutter="10">
            <i-col span="12">
                <Card :bordered="true" style="width: 600px">
                    <p slot="title">合并挡板</p>
    
                    <Button type="text">标题</Button>
                    <br>
                    <Input v-model="title" style="width: 500px" placeholder="请输入标题" type="textarea" :autosize="{minRows: 1,maxRows: 4}" />
                    <br> <br>
                    <div style="border-bottom: 1px solid #e9e9e9;padding-bottom:6px;margin-bottom:6px;">
                        <Checkbox :indeterminate="indeterminate" :value="checkAll" @click.prevent.native="handleCheckAll">全选</Checkbox>
                    </div>
                    <CheckboxGroup v-model="checkAllGroup" @on-change="checkAllGroupChange">
                        <Checkbox :label="item.id" v-for="item in mockItems" :key="item.index"><span>{{item.title}}</span></Checkbox>
                    </CheckboxGroup>
                    <br><br>
                    <Input v-model="backup" style="width: 500px" placeholder="备注" type="textarea" :autosize="{minRows: 1,maxRows: 4}" />
                    <br> <br>
                    <ButtonGroup>
                        <!-- <Button type="primary" @click="createMockconfig" v-if="!oneEditMode">生成挡板</Button> -->
                        <Button type="primary" @click="saveToHistory">保存到历史</Button>
                    </ButtonGroup>
    
                </Card>
            </i-col>
            <i-col span="12">
                <Card :bordered="true" style="width: 600px">
                    <p slot="title"><span>挡板历史</span><span v-if="!oneEditMode">--多选模式</span><span v-if="oneEditMode">--单选模式</span></p>
    
                    <br>
                    <!-- 测试环境：<Input v-model="testEnv" placeholder="请选择测试环境" style="width: 150px" />
              <br><br> -->
                    <CheckboxGroup v-model="checkMockHistory" @on-change="checkMockHistoryChange">
                        <Checkbox :label="item.id" v-for="item in mockHistory" :key="item.index"><span style="display:inline-block">{{item.title}}</span></Checkbox>
                    </CheckboxGroup>
                    <br> <br>
                    <ButtonGroup>
                        <Button type="primary" @click="changeEditMode" v-if="!oneEditMode">单选模式</Button>
                        <Button type="primary" @click="changeEditMode" v-if="oneEditMode">多选模式</Button>
                        <Button type="primary" @click="deleteMockHistoryClick" v-if="!oneEditMode">删除</Button>
                        <Button type="primary" v-if="oneEditMode" :loading="loading" @click="handleClickGitPushMock"><span v-if="!loading" >配置到gitlab</span><span v-else>配置到gitlab...</span></Button>
    
                    </ButtonGroup>
                    <br>
                    <br>
                    <p>默认多选模式下可以对历史挡板进行删除，并在右侧可以保存到历史。<br>单选模式下左侧数据会被历史挡板数据替换，并可以修改后保存。</p>
                    <br>
    
                </Card>
            </i-col>
        </Row>
    
        <Input v-model="combineJson" type="textarea" :autosize="{minRows: 4,maxRows: 20}" placeholder="合并节点挡板，生成挡板json" />
    
    
        <!-- <p>{{checkAllGroup}}</p> -->
    
    
    
    </div>
</template>

<script>
    import {
        mapMutations,
        mapActions,
        mapState,
        mapGetters
    } from 'vuex'
    export default {
        data: function() {
            return {
                indeterminate: true,
                checkAll: false,
                checkAllGroup: [],
                checkMockHistory: [],
                backup: '',
                title: '',
                activeBackup: '',
                // combineJson: "",
                loading: false,
                // 默认多选模式
                oneEditMode: true
            }
        },
        computed: {
            ...mapGetters([]),
            mockItems: {
                get: function() {
                    return this.$store.state.mockconfig.mockItems;
                },
                set: function(newValue) {
                    this.setMockItems(newValue);
                }
            },
            mockHistory: {
                get: function() {
                    return this.$store.state.mockconfig.mockHistory;
                }
            },
            mockConfig: {
                get: function() {
                    return this.$store.state.mockconfig.mockConfig;
                },
            },
            allItemId: {
                get: function() {
                    var allItemId = [];
                    for (const item of this.mockItems) {
                        allItemId.push(item.id)
                    }
                    return allItemId
                    // this.checkAllGroup = this.allItemId;
                }
            },
            combineJson: {
                get: function() {
                    return this.$store.state.mockconfig.combineJson;
                },
                set: function(value) {
                    this.setCombineJson(value);
                }
            },
			testEnv: {
				get: function() {
                    return this.$store.state.app.testEnv;
                },
                set: function(value) {
                    this.setTestEnv(value);
                }
			},
			decisionName: {
				get: function() {
                    return this.$store.state.app.decisionName;
                },
                set: function(value) {
                    this.setDecisionName(value);
                }
			},
			configBranch: {
				get: function() {
                    return this.$store.state.app.configBranch;
                },
                set: function(value) {
                    this.setConfigBranch(value);
                }
			},
    
    
        },
        methods: {
            ...mapMutations([
                'setActiveID',
                'setMockConfig',
                'setCombineJson',
                'setTestEnv',
				'setDecisionName',
				'setConfigBranch',
            ]),
            ...mapActions([
                'getMockconfigs',
                'gitPushMock',
                'getMockhistory',
                'saveMockhistory',
                'deleteMockhistory'
            ]),
            createMockconfig() {
                var combineJson = {}
                for (const item of this.mockItems) {
                    console.log(this.checkAllGroup.indexOf(item.id) != -1)
                    if (this.checkAllGroup.indexOf(item.id) != -1) {
                        var json = JSON.parse(item.json);
                        combineJson = Object.assign(combineJson, json)
                    }
                }
                console.log("checkAllGroup:");
                console.log(this.checkAllGroup)
                if (this.checkAllGroup.length == 0) {
                    this.$Message.error("请选择要合并的挡板！")
                    return
                }
                console.log("combineJson：" + JSON.stringify(combineJson))
                console.log(combineJson)
                this.combineJson = JSON.stringify(combineJson);
                this.$Message.success('已生成合并挡板!');
            },
            handleCheckAll() {
                // var allItemId = [];
                console.log("allItemId:")
                console.log(this.allItemId);
                if (this.indeterminate) {
                    this.checkAll = false;
                } else {
                    this.checkAll = !this.checkAll;
                }
                this.indeterminate = false;
    
                if (this.checkAll) {
                    // for (const item of thie.mockItems) {
                    //   allItemId.push(item.id)
                    // }
                    this.checkAllGroup = this.allItemId;
                } else {
                    this.checkAllGroup = [];
                }
            },
            checkAllGroupChange(data) {
                console.log(data)
                var combineJson = {}
                for (const item of this.mockItems) {
                    console.log(this.checkAllGroup.indexOf(item.id) != -1)
                    if (this.checkAllGroup.indexOf(item.id) != -1) {
                        var json = JSON.parse(item.json);
                        combineJson = Object.assign(combineJson, json)
                    }
                }
                console.log("checkAllGroup:");
                console.log(this.checkAllGroup)
                // if (this.checkAllGroup.length == 0) {
                //   this.$Message.error("请选择要合并的挡板！")
                //   return
                // }
                console.log("combineJson：" + JSON.stringify(combineJson))
                console.log(combineJson)
                this.combineJson = JSON.stringify(combineJson);
                // this.$Message.success('已生成合并挡板!');
            },
    
            checkMockHistoryChange(data) {
                console.log(data)
                if (this.oneEditMode) {
                    var id = data.pop()
                    this.checkMockHistory = []
                    this.checkMockHistory.push(id)
                    console.log(id)
                    var item = this.mockHistory.find(item => item.id === id)
                    console.log(item)
                    // this.combineJson = item.json
                    this.checkAllGroup = JSON.parse(item.subItems)
                    this.title = item.title
                    this.checkAllGroupChange()
                    this.saveToHistory()
                }
            },
    
            handleClickGitPushMock() {
                this.loading = true;
                if (this.combineJson === "") {
                    this.$Message.error({
                        content: "请先合并挡板！",
                        duration: 2
                    })
                    this.loading = false;
    
                } else {
                    var data = {
                        testEnv : this.testEnv,
			            decisionName : this.decisionName,
			            configBranch :  this.configBranch,
                        mockText: this.combineJson,
                    }
                    this.gitPushMock(data).then(res => {
                        this.$Message.success('挡板配置到gitlab成功!');
                        console.log(res)
                        this.loading = false;
                    }).catch(err => {
                        console.log(err)
                        this.$Message.error(err);
                        this.loading = false;
                    })
                }
            },
            changeEditMode() {
                this.checkMockHistory = []
                this.checkAllGroup = []
                this.oneEditMode = !this.oneEditMode
            },
            deleteMockHistoryClick() {
                console.log("deleteMockHistory:")
                console.log(this.checkMockHistory)
                this.deleteMockhistory(JSON.stringify(this.checkMockHistory)).then(res => {
                    this.$Message.success('删除数据成功!');
                    this.checkMockHistory = []
                }).catch(err => {
                    console.log(err);
                    this.loading = false;
                })
            },
            saveToHistory() {
                if (this.title === "") {
                    this.$Message.error({
                        content: "请输入标题！",
                        duration: 2
                    })
                } else if (this.combineJson === "") {
                    this.$Message.error({
                        content: "请先合并挡板！",
                        duration: 2
                    })
                } else {
                    console.log(this.checkAllGroup)
                    var data = JSON.stringify({
                        id: this.oneEditMode ? this.checkMockHistory[0] : "",
                        title: this.title,
                        description: this.backup,
                        json: this.combineJson,
                        subItems: JSON.stringify(this.checkAllGroup)
                    })
                    this.saveMockhistory(data).then(res => {
                        // this.$Message.success('保存挡板到历史记录!');
                    }).catch(err => {
                        console.log(err);
                        this.loading = false;
                    })
                }
    
    
            },
    
        },
        watch: {
        },
        mounted() {
            this.getMockconfigs();
            this.getMockhistory();
        }
    }
</script>


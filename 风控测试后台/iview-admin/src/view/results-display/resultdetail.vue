
  





<template>
    <div>
        <!-- 当前测试报告id {{$route.params.id }}
                    <div v-for="(value, key) in content" :key="key">
                        {{ key }}: {{ value }}
                    </div> -->
    
        <div class="ivu-collapse">
    
            <div class="ivu-collapse-item " v-bind:class="[activeReportStrategy[$route.params.id].indexOf(alias) != -1 ? 'ivu-collapse-item-active' : '']" v-for="(stragety, alias) in content" :key="alias">
                <div :class="headerClasses" @click="toggle(alias)">
                    <Icon type="ios-arrow-forward" /> {{stragety}}
    
                </div>
                <Tabs value="name1" v-if="activeReportStrategy[$route.params.id].indexOf(alias) != -1" size="small">
                    <TabPane label="入参" name="name1">
                        <div data-old-padding-top="" data-old-padding-bottom="" data-old-overflow="" :class="contentClasses">
    
                            <!-- <result-table v-if="activeReportStrategy[$route.params.id].indexOf(alias) != -1" :data1='reportfileds' /> -->
                            <result-table  :data1="reportfileds.filter(item=>item.strategyAlias==alias)" :paramType="input" />
    
                        </div>
                    </TabPane>
                    <TabPane label="出参" name="name2">
                        <div data-old-padding-top="" data-old-padding-bottom="" data-old-overflow="" :class="contentClasses">
    
                            <!-- <result-table v-if="activeReportStrategy[$route.params.id].indexOf(alias) != -1" :data1='reportfileds' /> -->
                            <result-table  :data1="reportfileds.filter(item=>item.strategyAlias==alias)" :paramType="output" />
    
                        </div>
                    </TabPane>
                </Tabs>
    
    
            </div>
    
        </div>
    </div>
</template>

<script>
    import ResultTable from '@/view/results-display/resulttable.vue'
    import {
        mapMutations,
        mapActions
    } from 'vuex'
    const prefixCls = 'ivu-collapse';
    
    export default {
        name: 'Panel',
        data() {
            return {
                index: 0, // use index for default when name is null
                hideArrow: false,
                activeId: '',
                activeTittle: '',
                items: [],
                // activeReportStrategy: [],
                input: "入参",
                output: "出参",
                isDisplayInput: true
            };
        },
        components: {
            ResultTable
        },
        computed: {
            headerClasses() {
                return `${prefixCls}-header`;
            },
            contentClasses() {
                return `${prefixCls}-content`;
            },
            boxClasses() {
                return `${prefixCls}-content-box`;
            },
            content: {
                get: function() {
                    return this.$store.state.rerun.content;
                },
                set: function(newValue) {
                    // this.setReportList(newValue);
                }
            },
            reportfileds: {
                get: function() {
                    return this.$store.state.rerun.reportfileds;
                },
                set: function(newValue) {
                    // this.setReportList(newValue);
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
        },
        methods: {
            ...mapMutations([
    
            ]),
            ...mapActions([
                'getReportDetail',
            ]),
            toggle(alias) {
                // this.isActive = !this.isActive;
                console.log(alias)
                var index = this.activeReportStrategy[this.$route.params.id].indexOf(alias);
                if (index != -1) {
                    console.log("关闭：")
                    this.activeReportStrategy[this.$route.params.id].splice(index, 1);
                } else {
                    console.log("展开：")
                    this.activeReportStrategy[this.$route.params.id].push(alias);
                    console.log(this.activeReportStrategy[this.$route.params.id])
                }
            },
        },
        mounted() {
            this.getReportDetail(this.$route.params.id).then(res => {
                this.$Message.success('报告数据加载成功!');
            }).catch(err => {
                console.log(err)
                this.$Message.error("报错了！");
            })
    
            // this.activeReportStrategy[this.id] = []
            console.log("content:")
            console.log(this.content)
            console.log(this.reportfileds)
    
    
    
            // 征信名称
            // creditName
            // 服务
            // service
            // 策略包
            // strategy
            // 相关接口
            // interface
            // 描述
            // description
            // 逻辑
            // logic
            // 测试结果
            // result
            // 备注
            // remarks
            // testSuccess
            this.items = [{
                    id: "1",
                    tittle: "反欺诈1",
                    data: [{
                            creditName: '邦盛设备指纹',
                            service: '设备号',
                            interface: 'APPLY_IDFA_DIFF_CID_3M_I',
                            description: '描述',
                            logic: '逻辑',
                            result: '测试结果',
                            remarks: '备注',
                            testSuccess: false
                        },
                        {
                            creditName: '邦盛设备指纹',
                            service: '设备号',
                            interface: 'APPLY_IDFA_DIFF_CID_3M_I',
                            description: `描述sjafjdlkjfksdjfksdjf;k
                                                                    描述描述sjafjdlkjfksdjfksdjf;k
                                                                    描述描述sjafjdlkjfksdjfksdjf;k
                                                                    描述描述sjafjdlkjfksdjfksdjf;k`,
                            logic: '逻辑',
                            result: '测试结果',
                            remarks: '备注',
                            testSuccess: true
                        },
                        {
                            creditName: '邦盛设备指纹',
                            service: '设备号',
                            interface: 'APPLY_IDFA_DIFF_CID_3M_I',
                            description: '描述',
                            logic: '逻辑',
                            result: '测试结果',
                            remarks: '备注',
                            testSuccess: true
                        },
                        {
                            creditName: '邦盛设备指纹',
                            service: '设备号',
                            interface: 'APPLY_IDFA_DIFF_CID_3M_I',
                            description: '描述',
                            logic: '逻辑',
                            result: '测试结果',
                            remarks: '备注',
                            testSuccess: true
                        },
                    ]
                },
                {
                    id: "2",
                    tittle: "反欺诈2",
                    data: [{
                            creditName: '邦盛设备指纹',
                            service: '设备号',
                            interface: 'APPLY_IDFA_DIFF_CID_3M_I',
                            description: '描述',
                            logic: '逻辑',
                            result: '测试结果',
                            remarks: '备注',
                            testSuccess: true
                        },
                        {
                            creditName: '邦盛设备指纹',
                            service: '设备号',
                            interface: 'APPLY_IDFA_DIFF_CID_3M_I',
                            description: '描述',
                            logic: '逻辑',
                            result: '测试结果',
                            remarks: '备注',
                            testSuccess: true
                        }
                    ]
                }
            ]
        },
    };
</script>
<template>
    <div>
        <Table :columns="columns1" :data="tTaskData"></Table>
        <Page :total="tTaskCount" :page-size="50" :current="tTaskCurrent" show-total @on-change="changepage"></Page>
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
        data() {
            return {
                // pageCurrent: 1,
                // dataCount: 100,
                columns1: [{
                        title: '任务id',
                        key: 'task_id'
                    },
                    {
                        title: '任务名称',
                        key: 'task_name'
                    },
                    {
                        title: '任务状态',
                        key: 'task_status'
                    },
                    {
                        title: '任务周期',
                        key: 'task_cycle'
                    },
                    {
                        title: '创建人',
                        key: 'create_user'
                    },
                    {
                        title: '创建时间',
                        key: 'create_time'
                    },
                    {
                        title: '更新时间',
                        key: 'update_time'
                    }
                ]
            }
        },
        computed: {
            ...mapState({
                tTaskCount: state => state.schedule.tTaskCount,
                tTaskData: state => state.schedule.tTaskData,
            }),
            tTaskCurrent: {
                get: function() {
                    return this.$store.state.schedule.tTaskCurrent;
                },
                set: function(newValue) {
                    this.setTaskCurrent(newValue);
                }
            },
            // tTaskData: {
            //     get: function() {
            //         return this.$store.state.mockconfig.tTaskData;
            //     },
            //     set: function(newValue) {
            //         this.setTaskData(newValue);
            //     }
            // },
        },
        methods: {
            ...mapMutations([
                'setTaskCurrent',
                'setTaskData'
            ]),
            ...mapActions([
                'getTaskList',
                'getTaskCount'
            ]),
            changepage(index) {
                console.log(index)
                this.setTaskCurrent(index);
                console.log("changepage:")
                console.log(this.tTaskCurrent)
                this.updateData();
            },
            updateData() {
                this.getTaskCount().then(res => {
                    this.getTaskList().then(res => {
                        console.log(res)
                        console.log("updateData:")
                        console.log(this.tTaskData)
                        this.$Message.success('查询数据成功!');
                    }).catch(err => {
                        console.log(err)
                        this.$Message.error("加载数据失败！");
                    });
    
                    // console.log(this.tTaskCount)
    
                }).catch(err => {
                    console.log(err)
                    this.$Message.error("获取数据总条数失败！");
                });
            }
        },
        mounted: function() {
    
            this.updateData();
    
    
        }
    
    }
</script>
<template>
    <div>
        <Table :columns="columns1" :data="tTaskDataPool"></Table>
        <Page :total="tTaskCountPool" :page-size="50" :current="tTaskCurrentPool" show-total @on-change="changepage"></Page>
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
                        title: '任务业务时间',
                        key: 'biz_date'
                    },
                    {
                        title: '任务状态',
                        key: 'status'
                    },
                    {
                        title: '任务尝试运行次数',
                        key: 'tried_times'
                    },
                    {
                        title: '任务开始时间',
                        key: 'start_time'
                    },
                    {
                        title: '任务结束时间',
                        key: 'end_time'
                    },
                    {
                        title: '任务更新时间',
                        key: 'update_time'
                    }
                ]
            }
        },
        computed: {
            ...mapState({
                tTaskCountPool: state => state.schedule.tTaskCountPool,
                tTaskDataPool: state => state.schedule.tTaskDataPool,
            }),
            tTaskCurrentPool: {
                get: function() {
                    return this.$store.state.mockconfig.tTaskCurrentPool;
                },
                set: function(newValue) {
                    this.setTaskCurrentPool(newValue);
                }
            }
        },
        methods: {
            ...mapMutations([
                'setTaskCurrentPool',
                'setTaskDataPool'
            ]),
            ...mapActions([
                'getTaskListPool',
                'getTaskCountPool'
            ]),
            changepage(index) {
                console.log(index)
                this.setTaskCurrentPool(index);
                this.updateData();
            },
            updateData() {
                this.getTaskCountPool().then(res => {
                    this.getTaskListPool().then(res => {
                        this.$Message.success('查询数据成功!');
                    }).catch(err => {
                        console.log(err)
                        this.$Message.error("加载数据失败！");
                    });
                    console.log(this.tTaskCount)
    
                }).catch(err => {
                    console.log(err)
                    this.$Message.error("获取数据总条数失败！");
                });
            }
        },
        mounted: function() {
            // console.log(this.tTaskCount)
            // console.log(this.tTaskCurrent)
            this.updateData();
        }
    
    }
</script>
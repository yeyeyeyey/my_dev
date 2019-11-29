<template>
    <Table border :columns="columns7" :data="reportList">
    </Table>
</template>

<script>
    import {
        mapMutations,
        mapActions
    } from 'vuex'
    
    export default {
        data() {
            return {
                columns7: [{
                        title: 'ID',
                        key: 'idNumber',
                        align: 'center',
                        width: 100,
                        render: (h, params) => {
                            return h('div', [
                                h('Icon', {
                                    props: {
                                        type: 'md-flower'
                                    }
                                }),
                                h('strong', params.row.idNumber)
                            ]);
                        }
                    },
                    {
                        title: '标题',
                        key: 'title',
                        width: 200
                    },
                    {
                        title: '创建方式',
                        width: 150,
                        key: 'createWay'
                    },
                    {
                        title: 'cid',
                        width: 200,
                        key: 'cid'
                    },
                    // {
                    //     title: 'sqs',
                    //     key: 'sqs'
                    // },
                    {
                        title: '备注',
                        key: 'remarks'
                    },
                    {
                        title: '创建时间',
                        key: 'created',
                        width: 210
                    },
                    {
                        title: '操作',
                        key: 'action',
                        width: 200,
                        align: 'center',
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                        type: 'primary',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            this.show(params.row.id, params.row.title)
                                        }
                                    }
                                }, '查看报告'),
                                h('Button', {
                                    props: {
                                        type: 'error',
                                        size: 'small'
                                    },
                                    on: {
                                        click: () => {
                                            this.remove(params.index, params.row.id, params.row.title)
                                        }
                                    }
                                }, '删除')
                            ]);
                        }
                    }
                ],
                // data6: []
            }
        },
        computed: {
            reportList: {
                get: function() {
                    return this.$store.state.rerun.reportList;
                },
                set: function(newValue) {
                    this.setReportList(newValue);
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
                'closeTag',
                'setReportList',
                'setActiveReportStrategy',
                'setActiveReportStrategy'
            ]),
            ...mapActions([
                'getReportList',
                'deleteReportList'
            ]),
            show(id, title) {
    
                const route = {
                    name: 'resultdetail',
                    params: {
                        id: id,
                        title: title
                    }
                }
                this.$router.push(route)
                // this.activeReportStrategy[id] =[]
                this.$set(this.activeReportStrategy, id, [])
            },
            remove(index, id, title) {
                this.reportList.splice(index, 1);
    
                this.deleteReportList(id).then(res => {
                    this.$Message.success('删除成功!');
                    this.closeTag({
                        name: 'resultdetail',
                        params: {
                            id: id,
                            title: title
                        }
                    })
                }).catch(err => {
                    console.log(err)
                    this.$Message.error(err);
                    this.loading = false;
                })
    
            }
        },
        mounted() {
            this.getReportList();
        }
    }
</script>
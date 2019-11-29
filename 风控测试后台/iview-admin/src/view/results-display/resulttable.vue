<style>
    .ivu-table .demo-table-info-row td {
        background-color: #2db7f5;
        color: #fff;
    }
    
    .ivu-table .demo-table-success-row td {
        background-color: #19be6b;
        color: #fff;
    }
    
    .ivu-table .demo-table-error-row td {
        background-color: #ff6600;
        color: #fff;
    }
</style>

<template>
    <div>
        <br/><br/>
        <Table :row-class-name="rowClassName" :tooltip='true' :columns="columns1" :data="data1"></Table>
        <br/><br/>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                columns1: [{
                        title: '征信名称',
                        key: 'creditName',
                        width: 150
                    },
                    {
                        title: '服务',
                        key: 'service',
                        width: 100
    
                    },
                    // {
                    //     title: '策略包',
                    //     key: 'strategy',
                    //     width: 100
                    // },
                    {
                        title: '相关接口',
                        key: 'interface',
                        width: 200
    
                    },
                    // {
                    //     title: '描述',
                    //     key: 'description',
                    // },
                    // {
                    //     title: '逻辑',
                    //     key: 'logic'
                    // },
                    {
                        title: '当前值类型',
                        key: 'currentValueType'
                    },
                    {
                        title: '当前值',
                        key: 'currentValue'
                    },
                    {
                        title: '测试结果',
                        key: 'result'
                    },
                    {
                        title: '备注',
                        key: 'remarks'
                    },
                ]
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
            }
        },
        methods: {
            rowClassName(row, index) {
                if (row.field) {
                    return 'demo-table-success-row';
                }
                return '';
            }
        },
        props: {
            data1: Array,
        }
    }
</script>
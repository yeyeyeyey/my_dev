<template>
    <div style="padding:50px;">
        <Divider>
            <Button type="success" ghost @click="addRow">Add Row</Button>
            <Button type="success" ghost @click="save">Save</Button>
            <Poptip @on-ok="deleteItem" confirm title="确认删除该项?" transfer>
                <Button type="success" ghost>Delete Item</Button>
            </Poptip>
        </Divider>
    
        <Table ref="myTable" :ellipsis='true' :columns="columns" :data="myData">
            <template slot="creditName" slot-scope="props"><Input v-model="props.row.creditName"/></template>

<template slot="paramType" slot-scope="props">
    <Select v-model="props.row.paramType"  transfer="true" >
                    <Option v-for="item in paramType" :value="item.value" :key="item.value">{{ item.label }}</Option>
            </Select>
</template>


<template slot="service" slot-scope="props">
    <Input v-model="props.row.service" />
</template>

<!--<template slot="strategy" slot-scope="props">
    <Input v-model="props.row.strategy" />
</template>-->
            
<template slot="interface" slot-scope="props">
    <Input v-model="props.row.interface" />
</template>


<template slot="description" slot-scope="props">
    <Input v-model="props.row.description" type="textarea" :autosize="{ minRows: 1, maxRows: 4 }" />
</template>

<template slot="logic" slot-scope="props">
    <Input v-model="props.row.logic" type="textarea" :autosize="{ minRows: 1, maxRows: 4 }" :autofocus='true' />
</template>



<template slot="remarks" slot-scope="props">
    <Input v-model="props.row.remarks" type="textarea" :autosize="{ minRows: 1, maxRows: 4 }" />
</template>
                <!-- 操作 -->
<template slot="action" slot-scope="props">
    <Poptip @on-ok="delRow(props.idx)" confirm title="确认删除该项?" transfer>
        <Button type="warning" size="small">删除</Button>
    </Poptip>
</template>

        </Table>  
          

        <!-- data调试信息 -->
            <!-- <Divider>data</Divider>
            {{ myData }} -->

        <div style="display:none;"> {{ act }}</div>
    </div>
</template>

<script>
    import {
        mapMutations,
        mapActions,
        mapState
    } from 'vuex'
    export default {
        data() {
            return {
                paramType: [{
                        value: 'input',
                        label: '入参'
                    },
                    {
                        value: 'output',
                        label: '出参'
                    },
                ],
                act: false, // 用于触发渲染
                name: 'editTable',
                myData: [],
                columns: [{
                        title: '征信名称',
                        key: 'creditName',
                        width: 130,
                        render: (h, params) => {
                            this.myData[params.index] = params.row
                            return h(
                                'div',
                                this.$refs.myTable.$scopedSlots.creditName({
                                    row: params.row,
                                    idx: params.row._index
                                })
                            )
                            // console.log(params.row.creditName)
                        }
                    },
                    {
                        title: '参数类型',
                        key: 'paramType',
                        width: 100,
                        render: (h, params) => {
                            this.myData[params.index] = params.row
                            return h(
                                'div',
                                this.$refs.myTable.$scopedSlots.paramType({
                                    row: params.row,
                                    idx: params.row._index
                                })
                            )
                        }
    
                    },
                    {
                        title: '服务',
                        key: 'service',
                        width: 100,
                        render: (h, params) => {
                            this.myData[params.index] = params.row
                            return h(
                                'div',
                                this.$refs.myTable.$scopedSlots.service({
                                    row: params.row,
                                    idx: params.row._index
                                })
                            )
                        }
    
                    },
                    // {
                    //     title: '策略包',
                    //     key: 'strategy',
                    //     width: 80,
                    //     render: (h, params) => {
                    //         this.myData[params.index] = params.row
                    //         return h(
                    //             'div',
                    //             this.$refs.myTable.$scopedSlots.strategy({
                    //                 row: params.row,
                    //                 idx: params.row._index
                    //             })
                    //         )
                    //     }
    
                    // },
                    {
                        title: '相关接口',
                        key: 'interface',
                        width: 200,
                        render: (h, params) => {
                            this.myData[params.index] = params.row
                            return h(
                                'div',
                                this.$refs.myTable.$scopedSlots.interface({
                                    row: params.row,
                                        idx: params.row._index
                                })
                            )
                        }
    
                    },
                    {
                        title: '描述',
                        key: 'description',
                        render: (h, params) => {
                            this.myData[params.index] = params.row
                            return h(
                                'div',
                                this.$refs.myTable.$scopedSlots.description({
                                    row: params.row,
                                    idx: params.row._index
                                })
                            )
                        }
    
                    },
                    {
                        title: '逻辑',
                        key: 'logic',
                        render: (h, params) => {
                            this.myData[params.index] = params.row
                            return h(
                                'div',
                                this.$refs.myTable.$scopedSlots.logic({
                                    row: params.row,
                                    idx: params.row._index
                                })
                            )
                        }
                    },
                    // {
                    //     title: '测试结果',
                    //     key: 'result'
                    // },
                    {
                        title: '备注',
                        key: 'remarks',
                        render: (h, params) => {
                            this.myData[params.index] = params.row
                            return h(
                                'div',
                                this.$refs.myTable.$scopedSlots.remarks({
                                    row: params.row,
                                    idx: params.row._index
                                })
                            )
                        }
                    },
                    {
                        title: '操作',
                        key: 'action',
                        render: (h, params) => {
                            return h(
                                'div',
                                this.$refs.myTable.$scopedSlots.action({
                                    idx: params.row._index
                                })
                            )
                        },
                        width: 60
                    }
                ]
            }
        },
        computed: {
            activeId: {
                get: function() {
                    return this.$store.state.fielddconfig.activeId;
                },
                set: function(newValue) {
                    this.setActiveID(newValue);
                }
            },
            items: {
                get: function() {
                    return this.$store.state.fielddconfig.items;
                },
                set: function(newValue) {
                    this.setItems(newValue);
                }
            },
        },
        methods: {
            ...mapActions([
                'getStrategys',
                'addStrategy',
                'deleteStrategy',
                'saveStrategy',
                'deleteField'
            ]),
            /** 删除行 */
            delRow(idx) {
                // this.myData[idx]['isDelete'] = true
                console.log('delRow:')
                console.log(this.myData[idx])
                var id = this.myData[idx]['id']
    
                this.myData.splice(idx, 1)
                this.$nextTick(() => {
                    this.act = !this.act
                })
                if (id) {
                    var field = JSON.stringify({
                        'id': id,
                        'strategy': this.id,
                        "isDelete": true
                    })
                    this.deleteField(field);
                }
            },
            /** 添加行 */
            addRow() {
                this.myData.push({
                    creditName: '',
                    paraType: '',
                    service: '',
                    interface: '',
                    description: '',
                    logic: '',
                    result: '',
                    remarks: '',
                    testSuccess: false
                })
                this.$nextTick(() => {
                    this.act = !this.act
                })
            },
            save() {
                console.log("this.data");
                console.log(this.data)
                console.log("this.myData1");
                console.log(this.myData)
                console.log("items:")
                console.log(this.items)
    
                this.$emit('save', this.myData);
                this.myData = [];
            },
            deleteItem() {
                this.$emit('deleteItem')
            },
            updateCurrentValue() {
    
            },
            initRow(data) {
                // this.data = data1;
                console.log("data:")
                console.log(this.data)
                this.myData = [];
                if (data) {
                    console.log(this.data);
                    for (const item of data) {
                        // if (item['isDelete'] === false) {
                        this.myData.push(item);
                        // }
                    }
                }
            },
            focus
    
        },
        mounted() {
            this.initRow(this.data);
        },
        updated() {
            // this.initRow()
        },
        watch: {
            act(nv, ov) {
                console.log("watch1:")
                console.log(nv);
            },
            data(nv, ov) {
                this.initRow(nv)
            }
        },
        props: {
            id: String,
            // tittle: String,
            data: Array,
        },
        destroyed() {
            // console.log('destroyed')
            // this.$emit('save',this.myData)
        }
    }
</script>

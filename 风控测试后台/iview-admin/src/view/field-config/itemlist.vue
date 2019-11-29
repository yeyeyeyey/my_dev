

<template>
    <div>
    
    
        <div class="ivu-collapse">
            <div class="ivu-collapse-item " v-bind:class="[item.id == activeId ? 'ivu-collapse-item-active' : '']" v-for="item in items" :key="item.index">
                <div :class="headerClasses" @click="toggle(item.id)">
                    <Icon type="ios-arrow-forward" /> {{item.strategy}}
                </div>
                <div data-old-padding-top="" data-old-padding-bottom="" data-old-overflow="" :class="contentClasses">
                    <!-- <div :class="boxClasses"> -->
                    <item-detail v-if="item.id == activeId" :data='item.strategyfiled' :id='item.id' :strategy='item.strategy' :alias='item.alias' :description='item.description' v-on:save="save()" v-on:deleteItem="deleteById()"></item-detail>
                    <!-- </div> -->
                </div>
            </div>
            <Button type="dashed" long @click="addItem()"><Icon type="ios-add-circle-outline" />Add Item</Button>
    
        </div>
    </div>
</template>

<script>
    import EditTable from '@/view/field-config/edittable.vue'
    import ItemDetail from '@/view/field-config/itemdetail.vue'
    const prefixCls = 'ivu-collapse';
    import {
        mapMutations,
        mapActions,
        mapState
    } from 'vuex'
    
    export default {
        name: 'Panel',
        data() {
            return {
                index: 0, // use index for default when name is null
                hideArrow: false,
                // activeId: '',
                // activeTittle: '',
                // items: [],
            };
        },
        components: {
            EditTable,
            ItemDetail,
        },
        computed: {
            ...mapState({
                // 'items': state => state.fielddconfig.items,
                // 'activeId': state => state.fielddconfig.activeId,
                'tittle': state => state.fielddconfig.tittle,
            }),
    
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
    
            headerClasses() {
                return `${prefixCls}-header`;
            },
            contentClasses() {
                return `${prefixCls}-content`;
            },
            boxClasses() {
                return `${prefixCls}-content-box`;
            },
            // items() {
            //     return this.$store.state.fielddconfig.items;
            // },
            // tittle() {
            //     return this.$store.state.fielddconfig.tittle;
            // }
        },
        methods: {
            ...mapMutations([
                'setActiveID',
                'setItems',
                'deleteByIndex'
            ]),
    
            ...mapActions([
                'getStrategys',
                'addStrategy',
                'deleteStrategy',
                'saveStrategy'
            ]),
    
            toggle(activeId, data) {
                // this.isActive = !this.isActive;
                // console.log(data);
                if (this.activeId == activeId) {
                    this.activeId = "";
                } else {
                    this.activeId = activeId;
                }
            },
            addItem() {
                var strategy = JSON.stringify({
                    strategy: "Untited",
                    description: ""
                })
                console.log("strategy:" + strategy)
                this.addStrategy(strategy)
            },
            // deleteByIndex: function(index) {
            //     this.items.splice(index, 1)
            // },
            deleteById() {
                console.log('deleteById(id):' + this.activeId)
                // var index = this.items.findIndex(item => item.id === id)
                // this.deleteByIndex(index)
                // console.log(this.$store.state.fielddconfig.items)

            },
            save() {
                // console.log("itemlist:")
                // console.log(this.items[this.getActiveIndex()].strategy)
                // this.getStrategys();
            },
            // updateTittle(tittle) {
            //     console.log("itemlist:" + tittle)
            //     var index = this.items.findIndex(item => item.id === this.activeId)
            //     this.$set(this.items[index], "tittle", tittle); // 改变对象
            // },
            // updateDescription(description) {
            //     console.log("=====" + "保存挡板描述信息")
            //     this.$set(this.items[this.getActiveIndex()], "description", description); // 改变对象
            // },
            getActiveIndex() {
                return this.items.findIndex(item => item.id === this.activeId)
            }
        },
        mounted() {
            // creditName: '邦盛设备指纹',
            // service: '设备号',
            // interface: 'APPLY_IDFA_DIFF_CID_3M_I',
            // description: '描述',
            // logic: '逻辑',
            // result: '测试结果',
            // remarks: '备注',
            // testSuccess: false
            // this.items = ''
            this.getStrategys();
            // this.items = this.$store.state.items;
            console.log(this.items);
        },
    };
</script>
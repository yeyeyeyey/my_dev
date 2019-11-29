

<template>
  <div>
     <div>
        <Input search placeholder="Enter something..." />
        <Input search enter-button placeholder="Enter something..." />
        <Input search enter-button="Search" placeholder="Enter something..." />
            <Button type="primary" shape="circle" icon="ios-search"></Button>

    </div>

    <div class="ivu-collapse">
      <div class="ivu-collapse-item " v-bind:class="[item.id == activeId ? 'ivu-collapse-item-active' : '']" v-for="item in mockItems" :key="item.index">
        <div :class="headerClasses" @click="toggle(item.id)">
          <Icon type="ios-arrow-forward" /> {{item.title}}
        </div>
        <div data-old-padding-top="" data-old-padding-bottom="" data-old-overflow="" :class="contentClasses">
          <!-- <div :class="boxClasses"> -->
          <json-edit v-if="item.id == activeId" :id='item.id' :title="item.title"  :description="item.description" :json="item.json" v-on:listenDelete="deleteById" @:listenSaveTittle="updateTittle" v-on:listenSaveDescription="updateDescription"></json-edit>
          <!-- </div> -->
        </div>
      </div>
      <Button type="dashed" long @click="addItem()">
                  <Icon type="ios-add-circle-outline" />
                  Add Item
                  </Button>
  
  
    </div>
  </div>
</template>

<script>
  import JsonEdit from '@/view/mock-config/jsonedit.vue'
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
        activeTittle: '',
        // items: [],
      };
    },
    components: {
      JsonEdit
    },
    computed: {
      activeId: {
        get: function() {
          return this.$store.state.mockconfig.activeId;
        },
        set: function(newValue) {
          this.setActiveID(newValue);
        }
      },
      mockItems: {
        get: function() {
          return this.$store.state.mockconfig.mockItems;
        },
        set: function(newValue) {
          this.setMockItems(newValue);
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
      }
    },
    methods: {
      ...mapMutations([
        'setActiveID',
        'setMockItems',
        'setActiveID'
      ]),
      ...mapActions([
        'getMockconfigs'
      ]),
      toggle(activeId) {
        // this.isActive = !this.isActive;
        console.log(this.activeId == activeId)
        if (this.activeId == activeId) {
          this.activeId = "";
        } else {
          this.activeId = activeId;
        }
      },
      addItem() {
        this.mockItems.push({
          title: "Untited",
          description: ''
        })
      },
      deleteItem(tittle) {
        console.log("deleteItem(tittle):" + tittle)
        var index = this.mockItems.findIndex(item => item.tittle === tittle)
        this.deleteByIndex(index)
      },
      deleteByIndex: function(index) {
        this.mockItems.splice(index, 1)
      },
      deleteById: function(id) {
        console.log('deleteById(id):' + id)
        var index = this.mockItems.findIndex(item => item.id === id)
        this.deleteByIndex(index)
      },
      updateTittle(tittle) {
        console.log("itemlist:" + tittle)
        var index = this.mockItems.findIndex(item => item.id === this.activeId)
        this.$set(this.mockItems[index], "tittle", tittle); // 改变对象
      },
      updateDescription(description) {
        console.log("=====" + "保存挡板描述信息")
        this.$set(this.mockItems[this.getActiveIndex()], "description", description); // 改变对象
      },
      getActiveIndex() {
        return this.mockItems.findIndex(item => item.id === this.activeId)
      }
    },
    mounted() {
      this.getMockconfigs();
      console.log("mounted:mockitems:")
      console.log(this.mockItems)
    },
  };
</script>
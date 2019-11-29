<template>
  <div>
    <Divider>
      <label>策略包名称：</label>
      <Tooltip content="修改策略包名称，点击save保存">
        <Input v-model="myTittle" placeholder="请输入策略包名称" style="width: 300px" />
      </Tooltip>
      <label>策略包别名：</label>
      <Tooltip content="修改策略包别名，点击save保存">
        <Input v-model="myAlias" placeholder="请输入策略包别名" style="width: 300px" />
      </Tooltip>
    </Divider>
  
    <Divider/>
  
    <edit-table :id="myId" v-on:deleteItem="deleteItem()" v-on:save="save" :data='data'></edit-table>
    <Divider>
      description
    </Divider>
    <Input v-model="myDescription" type="textarea" :autosize="true" placeholder="输入挡板内容" />
    <Divider/>
  </div>
</template>

<script>
  import EditTable from '@/view/field-config/edittable.vue'
  import {
    mapMutations,
    mapActions,
    mapState
  } from 'vuex'
  export default {
    data() {
      return {
        myTittle: this.strategy,
        myId: this.id,
        myDescription: this.description,
        myAlias: this.alias
        // myData: this.data
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
    components: {
      EditTable
    },
    methods: {
      ...mapActions([
        'getStrategys',
        'addStrategy',
        'deleteStrategy',
        'saveStrategy',
        'deleteField'
      ]),
      deleteItem() {
        var strategy = JSON.stringify({
          'id': this.activeId,
          'isDelete': true
        })
        this.deleteStrategy(strategy);
      },
      save(data) {
        console.log('myTittle:' + this.myTittle)
        var strategy = JSON.stringify({
          'id': this.id,
          'strategy': this.myTittle,
          'description': this.myDescription,
          'alias':this.myAlias,
          'strategyfiled': data
        })
        // this.saveStrategy(strategy)
        console.log("strategy:")
        console.log(strategy)
        this.saveStrategy(strategy).then(res => {
          this.$Message.info('保存策略包成功！');
          this.data = this.items.find(obj => obj.id === this.activeId).strategyfiled
        })
        // this.$emit("save")
      },
    },
    // props: ['id', 'tittle', 'description'],
    props: {
      id: String,
      strategy: String,
      description: String,
      data: Array,
      alias: String
    },
    watch: {
      data(nv, ov) {
        console.log("watch2:")
        console.log(nv);
        console.log(ov);
      },
    },
    mounted() {
  
    },
    updated() {
      // this.myData = this.data;
    }
  }
</script>

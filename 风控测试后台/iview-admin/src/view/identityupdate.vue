<template>
    <div>
        <Row :gutter="14">
            <i-col span="12">
                <Card style="height:350px">
                    <p slot="title">
                        <Icon type="md-albums" /> 身份证去重
                    </p>

                    <Form  :label-width="80">
                        <Row :gutter="0">
                            <Col span="9">
                            <FormItem label="身份证号" :required="true">
                                <Input v-model="identityID" placeholder="请输入需要去重的身份证号" />
                            </FormItem>
                            </Col>
                        </Row>
                        <br>
                        <FormItem>
                                <Button v-on:click="identityUpdate">重置</Button>
                        </FormItem>
                    </Form>
                </Card>

            </i-col>
        </Row>
        <Row :gutter="14">

        </Row>
    </div>
</template>

<script>
import {
  mapMutations,
  mapActions,
  mapState,
  mapGetters
} from 'vuex'
// import jsoneditVue from '../mock-config/jsonedit.vue';

export default {
  data () {
    return {
      identityID: '123456'
    }
  },
  methods: {
    ...mapActions([
      'updateIdCard'
    ]),
    identityUpdate: function () {
      if (this.identityID == null) {
        this.$Message.error('请先输入身份证号！')
        return
      }
      this.updateIdCard({ identity_no: this.identityID })
        .then(res => {
          this.$Message.success('重置成功')
        }).catch(error => {
          this.$Message.error('重置失败！')
          console.log(error)
        })

      // then(response => {this.$Message.success('重置成功')})
    }

  }

}
</script>

<template>
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
        <FormItem label="任务id" prop="">
            <Input v-model="formValidate.task_id" placeholder="修改时，请输入对应任务id"></Input>
        </FormItem>
        <FormItem label="任务名称" prop="">
            <Input v-model="formValidate.task_name" placeholder="请输入对应值"></Input>
        </FormItem>
        <FormItem label="任务类型" prop="">
            <Input v-model="formValidate.task_type_id" placeholder="请输入对应值"></Input>
        </FormItem>
        <FormItem label="任务周期" prop="">
            <p>(m-月/w-周/d-日/h-小时)</p>
            <Input v-model="formValidate.task_cycle" placeholder="请输入对应值"></Input>
        </FormItem>
        <FormItem label="任务状态" prop="">
            <p>(0为正常 1为冻结 默认0)</p>
            <Input v-model="formValidate.task_status" placeholder="请输入对应值"></Input>
        </FormItem>
    
        <FormItem label="分钟" prop="">
            <p>(0-59 默认0)</p>
            <Input v-model="formValidate.due_mi" placeholder="请输入对应值"></Input>
        </FormItem>
        <FormItem label="小时" prop="">
            <p>(0-23 默认0)</p>
            <Input v-model="formValidate.due_hh" placeholder="请输入对应值"></Input>
        </FormItem>
        <FormItem label="天" prop="">
            <p>(1-31 默认0)</p>
            <Input v-model="formValidate.due_dd" placeholder="请输入对应值"></Input>
        </FormItem>
        <FormItem label="周" prop="">
            <p>(1-7 默认0)</p>
            <Input v-model="formValidate.due_wd" placeholder="请输入对应值"></Input>
        </FormItem>
        <FormItem label="执行频率" prop="">
            <Input v-model="formValidate.frequency" placeholder="请输入对应值"></Input>
        </FormItem>
        <FormItem label="创建人" prop="">
            <Input v-model="formValidate.create_user" placeholder="请输入对应值"></Input>
        </FormItem>
        <FormItem label="更新人" prop="">
            <Input v-model="formValidate.update_user" placeholder="请输入对应值"></Input>
        </FormItem>
    
        </FormItem>
        <FormItem label="属性名称" prop="">
            <p>(src_sql/tar_command)</p>
    
            <Input v-model="formValidate.prop_name" placeholder="请输入对应值"></Input>
        </FormItem>
        </FormItem>
        <FormItem label="sql文本/指令" prop="">
            <Input v-model="formValidate.prop_value" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="请输入sql文本"></Input>
        </FormItem>
        <FormItem label="任务父id" prop="">
            <Input v-model="formValidate.parent_task_id" placeholder="请输入对应值"></Input>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="handleSubmit('formInline')">提交</Button>
        </FormItem>
    
    
    </Form>
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
                // formValidate: {
                //     task_id: '',
                //     task_name: '',
                //     task_type_id: '',
                //     task_cycle: '',
                //     due_mi: '',
                //     due_hh: '',
                //     due_dd: '',
                //     due_wd: '',
                //     frequency: '',
                //     create_user: '',
                //     update_user: '',
                //     prop_name: '',
                //     prop_value: '',
                //     parent_task_id: ''
                // },
                ruleValidate: {}
            }
        },
        computed: {
            formValidate: {
                get: function() {
                    return this.$store.state.schedule.formValidate;
                },
                set: function(value) {
                    return this.setFormValidate(value)
                }
            }
        },
        methods: {
            ...mapMutations([
                'setFormValidate'
            ]),
            ...mapActions([
                'postTask'
            ]),
            handleSubmit(name) {
                // this.$refs[name].validate((valid) => {
                //     if (valid) {
                //         this.$Message.success('Success!');
                //     } else {
                //         this.$Message.error('Fail!');
                //     }
                // })
                this.postTask().then(res => {
                    this.$Message.success('创建任务成功!');
                    console.log(res)
                }).catch(err => {
                    console.log(err)
                    this.$Message.error();
                })
            },
            handleReset(name) {
                this.$refs[name].resetFields();
            }
        }
    }
</script>
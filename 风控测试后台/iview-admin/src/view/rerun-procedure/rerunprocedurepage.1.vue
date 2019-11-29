<template>
    <div>
        <Row :gutter="14">
            <i-col span="12">
                <Card>
                    <p slot="title">
                        <Icon type="md-albums" /> 发Q重跑
                    </p>
                    <Row type="flex" justify="center" align="middle" class="countto-page-row">
                        <div class="count-to-con">
                            <label>请选择挡板：</label>
    
                            <Select v-model="selected" style="width:200px">
            <Option v-for="option in options" :value="option.tittle" :key="option.tittle">{{ option.tittle }}</Option>
        </Select>
                            <br/><br/>
                            <Input v-model="reportTittle" placeholder="请输入标题" style="width: 300px" />
    
    
                            <br/><br/>
                            <Input v-model="qValue" placeholder="请输入队列号" style="width: 300px " />
                            <br/><br/>
                            <Button type="info" @click="submitQ">Submit</Button>
                            <br/><br/>
                            <label v-if="!oldQValue">q报告未创建！</label>
                            <label v-if="oldQValue">{{oldQValue}}发送成功！报告号为：<a href="http://www.w3school.com.cn" target="_blank">{{qReportId}}</a></label>
                        </div>
                    </Row>
                </Card>
            </i-col>
            <i-col span="12">
                <Card>
                    <p slot="title">
                        <Icon type="md-albums" /> 通过cid创建报告
                    </p>
                    <Row type="flex" justify="start" align="middle" class="countto-page-row">
    
    
                        <div class="count-to-con">
                            <label>请选择挡板：</label>
                            <select v-model="selected">
                                                    <option v-for="option in options" v-bind:value="option.id" :key="option.index">
                                                    {{ option.tittle }}
                                                    </option>
                                                </select>
                            <br/><br/>
                            <Input v-model="reportTittle" placeholder="请输入标题" style="width: 300px" />
                            <br/><br/>
    
                            <Input v-model="cidValue" placeholder="请输入用户cid" style="width: 300px " />
                            <br/><br/>
    
                            <Button type="info" @click="submitCid">Submit</Button>
                            <br/>
                            <br>
                            <label v-if="!oldcid">cid报告未创建！</label>
    
                            <label v-if="oldcid">{{oldcid}}发送成功！报告号为：<a href="http://www.w3school.com.cn" target="_blank">{{cidReportId}}</a></label>
    
    
                            </br>
    
                        </div>
                    </Row>
                </Card>
            </i-col>
    
        </Row>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                reportTittle: '',
                selected: '2',
                options: [{
                        id: '1',
                        tittle: '第一个挡板'
                    },
                    {
                        id: '2',
                        tittle: '第二个挡板'
                    },
                    {
                        id: '3',
                        tittle: '第三个挡板'
                    }
                ],
                qValue: '',
                qReportId: '',
                oldQValue: '',
                cidValue: '',
                cidReportId: '',
                oldcid: ''
            }
        },
        methods: {
            submitQ() {
                if (this.qValue != this.oldQValue) {
                    this.qReportId = '报告号';
                }
                this.oldQValue = this.qValue;
            },
            submitCid() {
                if (this.cidValue != this.oldcid) {
                    this.cidReportId = '报告号';
                }
                this.oldcid = this.cidValue
            }
        },
    
    }
</script>

<style lang="less">
    @baseColor: ~"#dc9387";
    .countto-page-row {
        height: 400px;
        padding: 10px;
    }
    
    .count-to-con {
        display: block;
        width: 100%;
        text-align: center;
    }
    
    .count-text {
        font-size: 50px;
        color: @baseColor;
    }
    
    .slot-text {
        font-size: 22px;
    }
    
    .unit-class {
        font-size: 30px;
        color: @baseColor;
    }
</style>
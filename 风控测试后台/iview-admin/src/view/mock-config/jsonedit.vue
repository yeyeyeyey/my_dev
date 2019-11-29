<template>
    <div>
        <row>
            <i-col span='12'>
                <label>挡板名称：</label>
                <Input v-model="myTittle" placeholder="请输入挡板名称" style="width: 300px" />
                <br><br>
    
            </i-col>
            <i-col span='12'>
                <!-- <label>请输入cid：</label>
                                                                                                                                <Input v-model="cid" placeholder="请输入cid" style="width: 300px" /> -->
                <!-- <br><br> -->
                
    
                <label>选择节点名称：</label>
                <!-- <form-item prop="DIGESTID" label="操作名称" label-width="80" label-position="right">
                    <i-select v-model="searchForm.DIGESTID" style="width: 220px" clearable="true">
                        <i-option v-for="item in digestList" :value="item.DIGESTID" :key="item.DIGESTNAME">{{item.DIGESTID}} - {{item.DIGESTNAME}}</i-option>
                    </i-select>
                </form-item> -->
                <Select  filterable clearable v-model="execute_action" remote :remote-method='searchExecutionMethod' placeholder='输入关键字可搜索审批节点' style="width:200px">
                    <Option v-for="item in execute_action_list" :value="item" :key="item">{{ item }}</Option>
                </Select>
                <Input v-model="cid" placeholder="输入cid，为空则不加此条件" style="width: 200px" />
                <br><br>
    
            </i-col>
        </row>
    
        <Row :gutter="14">
    
            <i-col span="12">
                <Card style="height:600px">
                    <p slot="title">
                        <Icon type="md-albums" /> 设置节点挡板
                    </p>
                    <div>
                        <ButtonGroup>
                            <Button type="primary" @click="myCompress">压缩 </Button>
                            <Button type="primary" @click="myBeauty">美化 </Button>
                            <Button type="primary" @click="saveItem">保存 </Button>
                            <Button type="primary" @click="deleteItem">删除 </Button>
    
                        </ButtonGroup>
                    </div>
                    <Input v-model="myJson" type="textarea" :autosize="{minRows: 4,maxRows: 20}" placeholder="单节点挡板配置，保存时不能为空" />
                </Card>
            </i-col>
            <i-col span="12">
                <Card style="height:600px">
                    <p slot="title">
                        <Icon type="md-albums" /> 获取实时出参
                    </p>
                    <ButtonGroup>
                        <Button type="primary" @click="getParams">获取节点出参</Button>
                        <Button type="primary" @click="copyToLeft">复制到左侧</Button>
    
                    </ButtonGroup>
                    <Input v-model="currentOutputsJson" type="textarea" :autosize="{minRows: 4,maxRows: 20}" placeholder="节点实时出参，通过审批节点和cid查询。cid为空时，只查询节点条件" />
    
                </Card>
            </i-col>
    
        </Row>
        <br><br>
        <br><br>
    
        <br>
        <br><br>
        <Label>描述：</Label>
        <br>
        <Input v-model="myDescription" type="textarea" :autosize="true" placeholder="输入挡板内容" />
        <Divider/>
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
                myJson: this.json,
                myTittle: this.title,
                myDescription: this.description,
                // cid: '',
                // execute_action: '',
                // execute_action_list: ['查询反欺诈1','查询反欺诈2','查询终审包','查询评分卡','查询额度包','查询被拒包','查询补丁包','查询额度宝api准入包'],
                // execute_action_list:  ["查询反欺诈", "查询反欺诈包"],
                // currentOutputsJson: '',
                myJsonHasError: false,
                currentOutputsJsonHasError: false
            }
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
            currentOutputsJson: {
                get() {
                    return this.$store.state.mockconfig.currentOutputsJson;
                },
                set(value) {
                    // this.$store.commit('updateMessage', value)
                    this.setCurrentOutputsJson(value)
                }
            },
            cid: {
                get() {
                    return this.$store.state.mockconfig.cid;
                },
                set(value) {
                    this.setCid(value);
                }
            },
            execute_action: {
                get() {
                    return this.$store.state.mockconfig.execute_action;
                },
                set(value) {
                    this.setExecuteAction(value);
                }
            },
            execute_action_list: {
                get() {
                    return this.$store.state.mockconfig.execute_action_list;
                }
            }
    
        },
        methods: {
            ...mapMutations([
                'setCurrentOutputsJson',
                'setCid',
                'setExecuteAction'
            ]),
            ...mapActions([
                'getMockconfigs',
                'deleteMockconfig',
                'saveMockconfig',
                'postCurrentOutputsJson',
                'searchExecution'
            ]),
            myCompress() {
                this.myJson = this.compress(this.myJson)
            },
            myBeauty() {
                if (!(this.myJson == undefined)) {
                    this.myJson = this.beauty(this.myJson)
                }
            },
            compress: function(source) {
                // var source = this.myJson;
                var index = 0,
                    length = source.length,
                    symbol, position, result = ""
                while (index < length) {
                    symbol = source[index];
                    if ("\t\r\n ".indexOf(symbol) > -1) {
                        // Skip whitespace tokens.
                        index++;
                    } else if (symbol == "/") {
                        symbol = source[++index];
                        if (symbol == "/") {
                            // Line comment.
                            position = source.indexOf("\n", index);
                            if (position < 0) {
                                position = source.indexOf("\r", index);
                            }
                            index = position < 0 ? length : position;
                        } else if (symbol == "*") {
                            // Block comment.
                            position = source.indexOf("*/", index);
                            if (position < 0) {
                                throw SyntaxError("Unterminated block comment.");
                            }
                            // Advance the scanner position past the end of the comment.
                            index = position += 2;
                        } else {
                            throw SyntaxError("Invalid comment.");
                        }
                    } else if (symbol == '"') {
                        // Save the current scanner position.
                        position = index;
                        // Parse JavaScript strings separately to ensure that comment tokens
                        // within them are preserved correctly.
                        while (index < length) {
                            symbol = source[++index];
                            if (symbol == "\\") {
                                // Advance the scanner past escaped characters.
                                index++;
                            } else if (symbol == '"') {
                                // An unescaped double-quote character marks the end of the string.
                                break;
                            }
                        }
                        if (source[index] == '"') {
                            result += source.slice(position, ++index);
                        } else {
                            throw SyntaxError("Unterminated string.");
                        }
                    } else {
                        result += symbol;
                        index++;
                    }
                }
                // this.myJson = result;
                return result;
            },
            beauty: function(source) {
                var newJSON;
                try {
                    newJSON = JSON.stringify(JSON.parse(source), '', 4)
    
                } catch (ex) {
                    this.$Message.error({
                        content: '新 JSON 解析错误\r\n' + ex.message,
                        duration: 10
                    })
    
                    return
                }
                return newJSON;
    
            },
            saveItem() {
                console.log("saveItem:");
                console.log(this.myJson);
                if (this.myJson == undefined) {
                    this.$Message.error({
                        content: '保存时，json不能为空',
                        duration: 5
                    })
                    return
                }
                if (this.myJsonHasError) {
                    this.$Message.error({
                        content: 'json有错误不能保存',
                        duration: 5
                    })
                    return
                }
                var mockconfig = JSON.stringify({
                    'id': this.id,
                    "title": this.myTittle,
                    "description": this.myDescription,
                    "json": this.compress(this.myJson)
                })
                this.saveMockconfig(mockconfig).then(res => {
                    this.$Message.success('保存成功!');
                    console.log(res)
                }).catch(err => {
                    console.log(err)
                    this.$Message.error();
                })
            },
            deleteItem() {
                console.log("deleteItem-this.id:")
                console.log(this.id)
                var mockconfig = JSON.stringify({
                    'id': this.id,
                })
                this.deleteMockconfig(mockconfig)
            },
            getParams() {
                var data = JSON.stringify({
                    "execute_action": this.execute_action,
                    "cid": this.cid
                })
                console.log("execute_action:"+this.execute_actio)
                this.postCurrentOutputsJson(data).then(res => {
                    this.$Message.success('获取参数成功!');
                    console.log(res)
                }).catch(err => {
                    console.log(err)
                    this.$Message.error();
                });
            },
            copyToLeft() {
                if (this.currentOutputsJsonHasError) {
                    this.$Message.error({
                        content: "右侧json有错误，请修改后移动到左侧",
                        duration: 5
                    })
                    return
                }
                console.log("this.currentOutputsJson:");
                console.log(this.currentOutputsJson);
                this.myJson = this.currentOutputsJson;
            },
            searchExecutionMethod(query){
                console.log(query.length)
                this.searchExecution(query)
                // console.log("execute_action_list:")
                // console.log(this.execute_action_list)
            }
    
        },
        watch: {
            currentOutputsJson(newValue, oldValue) {
                if (!(newValue == undefined)) {
                    if (this.id === this.activeId) {
                        try {
                            JSON.stringify(JSON.parse(newValue), '', 4)
                            this.currentOutputsJsonHasError = false;
                        } catch (ex) {
                            this.$Message.error({
                                content: '新 OutputsJson 解析错误\r\n' + ex.message,
                                duration: 5
                            })
    
                            this.currentOutputsJsonHasError = true
                        }
                    }
                }
            },
            myJson(newValue, oldValue) {
                if (!(newValue == undefined)) {
                    try {
                        JSON.stringify(JSON.parse(newValue), '', 4)
                        this.myJsonHasError = false;
                    } catch (ex) {
                        this.$Message.error({
                            content: '新 myJson 解析错误\r\n' + ex.message,
                            duration: 5
                        })
    
                        this.myJsonHasError = true
                    }
                }
            }
        },
        mounted() {
            this.myBeauty();
            this.searchExecution('')
        },
        props: {
            id: String,
            title: String,
            json: String,
            description: String
        }
    }
</script>
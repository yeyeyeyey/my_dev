export default {
    state: {
        title:'',
        cid:'',
        strategyAliasMap:
        {
            "M_QD_FA1": "查询反欺诈1",
            "M_QD_FB1": "查询反欺诈2",
            "M_QD_FL1": "查询终审包",
            "M_QD_SE1": "查询评分卡",
            "M_QD_CT1": "查询额度包"
        }

    },
    mutations: {
        setTitle(state,value){
            state.title = value;
        },
        setCid(state,value){
            state.cid = value;
        }
    }
}
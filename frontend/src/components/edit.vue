<div>
  <el-dialog title="添加设备" :visible.sync="editFormVisible" :close-on-click-modal="false">
      <el-form :model="ruleForm" :rules="rules" label-width="100px">
        <el-table-column label="资产id" prop="propery_id">
          <el-input v-model="editForm.propery_id"></el-input>
      </el-table-column>
        <el-form-item label="系统名称" prop="system">
          <el-input v-model="editForm.system"></el-input>
        </el-form-item>
        <el-form-item label="设备型号" prop="model">
          <el-input v-model="editForm.model"></el-input>
        </el-form-item>
        <el-form-item label="系统版本" prop="version">
          <el-input v-model="editForm.version"></el-input>
        </el-form-item>
        <el-form-item label="资产管理员" prop="propery_admin">
          <el-input v-model="editForm.propery_admin"></el-input>
        </el-form-item>
        <el-form-item label="借用人" prop="borrow_people">
          <el-input v-model="editForm.borrow_people"></el-input>
        </el-form-item>
        <el-form-item label="备注" prop="desc">
          <el-input type="textarea" v-model="editForm.desc"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer">
        <el-button type="primary" @click="edit()">保 存</el-button>
        <el-button @click.native="editFormVisible = false">取 消</el-button>
      </div>
    </el-dialog>
</div>

<script>
  export default {
    props:['isShowData'],
    data() {
      return {
        editForm: {
          propery_id: '',
          system: '',
          model: '',
          version: '',
          propery_admin: '',
          borrow_people: '',
          desc: ''
        },
      rules: {
        system: [
          { required: true, message: '请输入系统名称', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        model: [
          { required: true, message: '请输入设备型号', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        version: [
          { required: true, message: '请输入系统版本', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        propery_admin: [
          { required: true, message: '请输入资产管理员', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        borrow_people: [
          { required: true, message: '请输入借用人', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ]
      }
      };
    },
    methods:{
      edit () {
        axios.get('http://127.0.0.1:8000/devicestore/edit', {
          params: {
            system: this.ruleForm.system,
            model: this.ruleForm.model,
            version: this.ruleForm.version,
            propery_admin: this.ruleForm.propery_admin,
            borrow_people: this.ruleForm.borrow_people,
            desc: this.ruleForm.desc
          }
        })
          .then(function (response) {
            console.log(response)
            alert('修改成功')
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    }
  }
</script>


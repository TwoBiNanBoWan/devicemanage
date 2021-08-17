```vue

<template>
<div class="home">
  <el-row>
    系统名称：
    <el-input v-model="system" placeholder="请输入系统名称" clearable style="width: 10%;margin-right: 20px"></el-input>
    型号：
    <el-input v-model="model" placeholder="请输入型号" clearable style="width: 10%;margin-right: 20px"></el-input>
    版本号：
    <el-input v-model="version" placeholder="请输入版本号" clearable style="width: 10%;margin-right: 20px"></el-input>
    资产管理员：
    <el-input v-model="propery_admin" placeholder="请输入资产管理员" clearable style="width: 10%;margin-right: 20px"></el-input>
    借用人：
    <el-input v-model="borrow_people" placeholder="请输入借用人" clearable style="width: 10%;margin-right: 20px"></el-input>
    资产id：
    <el-input v-model="propery_id" placeholder="请输入设备资产id" clearable style="width: 10%;margin-right: 20px"></el-input>
    <el-button type="primary" @click="queryDevices()" style="margin: 2px;">查询</el-button>
    <el-button type="primary" @click="restart()" style="margin: 2px;">重置</el-button>
    <el-button type="primary" @click="dialogFormVisible = true" style="margin: 2px;">添加设备</el-button>
  </el-row><br><br><br>
  <!--表格-->
  <el-row>
    <el-table :data="devices" style="width: 100%" border>
      <el-table-column prop="propery_id" label="资产id" min-width="100">
      <template slot-scope="scope"> {{ scope.row.fields.propery_id }} </template>
      </el-table-column>
      <el-table-column prop="system" label="系统名称" min-width="100">
      <template slot-scope="scope"> {{ scope.row.fields.system }} </template>
      </el-table-column>
      <el-table-column prop="model" label="型号" min-width="100">
      <template slot-scope="scope"> {{ scope.row.fields.model }} </template>
      </el-table-column>
      <el-table-column prop="version" label="版本" min-width="100">
      <template slot-scope="scope"> {{ scope.row.fields.version }} </template>
      </el-table-column>
      <el-table-column prop="propery_admin" label="资产管理员" min-width="100">
      <template slot-scope="scope"> {{ scope.row.fields.propery_admin }} </template>
      </el-table-column>
      <el-table-column prop="borrow_people" label="借用人" min-width="100">
      <template slot-scope="scope"> {{ scope.row.fields.borrow_people }} </template>
      </el-table-column>
      <el-table-column prop="QRCodeurl" label="二维码" min-width="100">
        <img :src= "QRCodeurl" alt="Smiley face" width="42" height="42">
      </el-table-column>
      <el-table-column prop="ct" label="创建时间" min-width="100">
      <template slot-scope="scope"> {{ scope.row.fields.ct }} </template>
      </el-table-column>
      <el-table-column prop="ut" label="更新时间" min-width="100">
      <template slot-scope="scope"> {{ scope.row.fields.ut }} </template>
      </el-table-column>
      <el-table-column prop="operator" label="操作人" min-width="100">
      <template slot-scope="scope"> {{ scope.row.fields.operator }} </template>
      </el-table-column>
      <el-table-column label="操作" min-width="100">
      <template slot-scope="scope">
        <el-button size="small" @click="handleEdit(scope.$index, scope.row.fields)" style="margin-left: 10px">编辑</el-button>
        <el-button size="small" @click="deleteDevices(scope.row.fields.propery_id)">删除</el-button>
        <el-button size="small" @click="codeFish(scope.row.fields.propery_id)">生成二维码</el-button>
        <el-button size="small" @click="queryQRCode(scope.row.fields.propery_id)">查看二维码</el-button>
      </template>
      </el-table-column>
    </el-table>
  </el-row>
  <!--添加设备-->
  <div>
    <el-dialog title="添加设备" :visible.sync="dialogFormVisible">
      <el-form :model="ruleForm" :rules="rules" label-width="100px">
        <el-form-item label="系统名称" prop="system">
          <el-input v-model="ruleForm.system"></el-input>
        </el-form-item>
        <el-form-item label="设备型号" prop="model">
          <el-input v-model="ruleForm.model"></el-input>
        </el-form-item>
        <el-form-item label="系统版本" prop="version">
          <el-input v-model="ruleForm.version"></el-input>
        </el-form-item>
        <el-form-item label="资产管理员" prop="propery_admin">
          <el-input v-model="ruleForm.propery_admin"></el-input>
        </el-form-item>
        <el-form-item label="借用人" prop="borrow_people">
          <el-input v-model="ruleForm.borrow_people"></el-input>
        </el-form-item>
        <el-form-item label="备注" prop="desc">
          <el-input type="textarea" v-model="ruleForm.desc"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitForm()">立即创建</el-button>
        <el-button @click="dialogFormVisible = false">取 消</el-button>
      </div>
    </el-dialog>
  </div>
  <!--编辑设备-->
  <div>
  <el-dialog title="编辑设备" :visible.sync="editFormVisible" :close-on-click-modal="false">
      <el-form :model="editForm" :rules="rules" label-width="100px">
        <el-form-item label="资产id" prop="propery_id">
          <el-input v-model="editForm.propery_id" disabled="true"></el-input>
        </el-form-item>
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
        <el-button @click="editFormVisible = false">取 消</el-button>
      </div>
    </el-dialog>
  </div>

</div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'home',
  data () {
    return {
      QRCodeurl: '',
      // 筛选条件
      system: '',
      model: '',
      version: '',
      propery_admin: '',
      borrow_people: '',
      propery_id: '',
      devices: [],
      // 删除设备id
      deleteForm: {
        propery_id: ''
      },
      // 添加设备弹框
      dialogFormVisible: false,
      // 编辑弹框
      editFormVisible: false,
      // 编辑界面
      editForm: {
        propery_id: '',
        system: '',
        model: '',
        version: '',
        propery_admin: '',
        borrow_people: '',
        desc: ''
      },
      // 添加设备
      ruleForm: {
        system: '',
        model: '',
        version: '',
        propery_admin: '',
        borrow_people: '',
        desc: ''
      },
      // 添加设备校验
      rules: {
        propery_id: [
          { required: true, message: '请输入系统名称', trigger: 'blur' },
          { max: 20, message: '长度限制20个字符', trigger: 'blur' }
        ],
        system: [
          { required: true, message: '请输入系统名称', trigger: 'blur' },
          { max: 20, message: '长度限制20个字符', trigger: 'blur' }
        ],
        model: [
          { required: true, message: '请输入设备型号', trigger: 'blur' },
          { max: 20, message: '长度限制20个字符', trigger: 'blur' }
        ],
        version: [
          { required: true, message: '请输入系统版本', trigger: 'blur' },
          { max: 20, message: '长度限制20个字符', trigger: 'blur' }
        ],
        propery_admin: [
          { required: true, message: '请输入资产管理员', trigger: 'blur' },
          { max: 20, message: '长度限制20个字符', trigger: 'blur' }
        ],
        borrow_people: [
          { required: true, message: '请输入借用人', trigger: 'blur' },
          { max: 20, message: '长度限制20个字符', trigger: 'blur' }
        ]
      }
    }
  },
  mounted: function () {
    this.queryDevices()
  },
  methods: {
    // 重置方法
    restart () {
      this.system = ''
      this.model = ''
      this.version = ''
      this.propery_admin = ''
      this.borrow_people = ''
      this.propery_id = ''
      this.queryDevices()
    },
    // 生成二维码
    codeFish (properyId) {
      axios.get('http://127.0.0.1:8000/devicestore/qrcodefish', {
        params: {
          propery_id: properyId
        }
      })
        .then(function (response) {
          console.log(response)
          alert('生成成功')
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    // 查看二维码
    queryQRCode (properyId) {
      var QRCode = ''
      axios.get('http://127.0.0.1:8000/devicestore/queryqrcode', {
        responseType: "blob",
        params: {
          propery_id: properyId
        }
      })
        .then(function (response) {
          QRCode = response.data.qr_code
          return QRCode
        })
        .catch(function (error) {
          console.log(error)
        })
        const blob = new Blob([QRCode])
        this.QRCodeurl = window.URL.createObjectURL(blob)
    },
    // 删除设备
    deleteDevices (properyId) {
      this.deleteForm.propery_id = properyId
      axios.get('http://127.0.0.1:8000/devicestore/delete', {
        params: {
          propery_id: this.deleteForm.propery_id
        }
      })
        .then(function (response) {
          console.log(response)
          alert('删除成功')
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    // 查询设备信息
    queryDevices () {
      this.$http.get('http://127.0.0.1:8000/devicestore/showdevices', {params: {
        propery_id: this.propery_id,
        borrow_people: this.borrow_people,
        system: this.system,
        model: this.model,
        version: this.version,
        propery_admin: this.propery_admin}
      }).then((response) => {
        var res = JSON.parse(response.bodyText)
        // const {list} = res || {};
        // const {fields} = list[0] || {}
        // let codeArr = []
        // Array.isArray(list) && list.forEach((item, index) => {
        //   const { qr_code } = item.fields || {};
        //   codeArr.push(qr_code);
        //   this.devices.push(qr_code)
        // })
        //
        // console.log(codeArr, fields['qr_code']);
        this.devices = res['list']
      })
    },
    // 编辑
    handleEdit: function (index, row) {
      this.editFormVisible = true
      this.editForm = Object.assign({}, row)
    },
    // 编辑
    edit () {
      axios.get('http://127.0.0.1:8000/devicestore/edit', {
        params: {
          propery_id: this.editForm.propery_id,
          system: this.editForm.system,
          model: this.editForm.model,
          version: this.editForm.version,
          propery_admin: this.editForm.propery_admin,
          borrow_people: this.editForm.borrow_people,
          desc: this.editForm.desc
        }
      })
        .then(function (response) {
          console.log(response)
          alert('修改成功')
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    // 创建设备
    submitForm () {
      axios.get('http://127.0.0.1:8000/devicestore/adddevices', {
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
          alert('添加成功')
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
```

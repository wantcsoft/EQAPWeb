(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0b328c"],{"26d6":function(e,t,o){"use strict";o.r(t);var i=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{staticClass:"root"},[o("h1",{staticStyle:{"text-align":"center"}},[e._v("Device information setup")]),e._v(" "),o("el-form",{ref:"form",staticStyle:{"margin-left":"30%"},attrs:{model:e.form,"label-width":"20%"}},[o("el-form-item",{attrs:{label:"Deive name"}},[o("el-input",{staticStyle:{width:"30%"},model:{value:e.form.DeviceName,callback:function(t){e.$set(e.form,"DeviceName",t)},expression:"form.DeviceName"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"Deive serialNo"}},[o("el-input",{staticStyle:{width:"30%"},model:{value:e.form.DeviceSerialNo,callback:function(t){e.$set(e.form,"DeviceSerialNo",t)},expression:"form.DeviceSerialNo"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"Deive location"}},[o("el-input",{staticStyle:{width:"30%"},model:{value:e.form.DeviceLocation,callback:function(t){e.$set(e.form,"DeviceLocation",t)},expression:"form.DeviceLocation"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"Device desc"}},[o("el-input",{staticStyle:{width:"30%"},model:{value:e.form.DeviceDesc,callback:function(t){e.$set(e.form,"DeviceDesc",t)},expression:"form.DeviceDesc"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"Server IP addr"}},[o("el-input",{staticStyle:{width:"30%"},model:{value:e.form.ServerIP,callback:function(t){e.$set(e.form,"ServerIP",t)},expression:"form.ServerIP"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"Server port"}},[o("el-input",{staticStyle:{width:"30%"},model:{value:e.form.ServerPort,callback:function(t){e.$set(e.form,"ServerPort",t)},expression:"form.ServerPort"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"Connect timeout"}},[o("el-input",{staticStyle:{width:"30%"},model:{value:e.form.ConnToServerTimeOut,callback:function(t){e.$set(e.form,"ConnToServerTimeOut",t)},expression:"form.ConnToServerTimeOut"}})],1)],1),e._v(" "),o("div",{staticStyle:{"text-align":"center"}},[o("el-button",{attrs:{type:"success"},on:{click:function(t){return e.updateDevice(e.form)}}},[e._v("Update")])],1),e._v(" "),o("div",{staticStyle:{"text-align":"center"}},[o("el-button",{attrs:{type:"text"},on:{click:e.toHome}},[e._v("Home Page")])],1)],1)},r=[],c={data:function(){return{form:{}}},mounted:function(){this.getSystem()},methods:{toHome:function(){this.$router.push({path:"/"})},getSystem:function(){var e=this,t=this;this.req({url:"/getDeviceSetup",method:"GET"}).then((function(e){t.form=e.data}),(function(t){console.log(t),e.$message({type:"success",message:"配置获取失败"})}))},updateDevice:function(e){var t=this;this.req({url:"/updateDevice",data:{DeviceID:e.DeviceID,DeviceName:e.DeviceName,DeviceSerialNo:e.DeviceSerialNo,DeviceLocation:e.DeviceLocation,DeviceDesc:e.DeviceDesc,ServerIP:e.ServerIP,ServerPort:e.ServerPort,ConnToServerTimeOut:e.ConnToServerTimeOut},method:"POST"}).then((function(e){t.$message({type:"success",message:e.data.message})}),(function(e){console.log("err :",e),t.$message({type:"info",message:"修改失败"})}))}}},a=c,n=o("2877"),l=Object(n["a"])(a,i,r,!1,null,"1b0a5c4d",null);t["default"]=l.exports}}]);
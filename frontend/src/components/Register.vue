<script>
import { useRouter } from 'vue-router'
import success from './success.vue'
import failure from './failure.vue'
import info from './info.vue'
export default{
    components:{
        success,
        failure,
        info,
    },
   data(){
    return{
        fields: {
        "first_name" :{
            fieldName: "First Name",
            name: "first_name",
            fieldType: "text",
            mandatory: true
            },
        "last_name":{
            fieldName: "Last Name",
            name: "last_name",
            fieldType: "text",
            mandatory: true
            },
        "date_of_birth": {
            fieldName: "Date of Birth",
            name: "date_of_birth",
            fieldType: "Date",
            mandatory: true
            },
        "phone_number": {
            fieldName: "Phone Number",
            name: "phone_number",
            fieldType: "tel",
            mandatory: true
            },  
          },
        entries:{},
        header_msg: '',
        info_value: '',
        showPass: false,
        banner_img: this.baseImgUrl + "/img/fn_banner.png",
        selectedData: {},
        reqData: "Brand",
        added: false,
        failed: false,
        info_msg: false
    }
   },
   methods:{
    QueryParams(param){
            return Object.entries(param).reduce((acc, [key, value]) => {
            if (typeof value === 'object') {
                acc[key] = JSON.stringify(value);
            } else {
                acc[key] = value;
            }
            return acc;
            }, {});
        },
        check_mandatory(){
            let result = true
            for(let field in this.fields){
                if(this.fields[field]['mandatory']){
                    result &= (this.entries.hasOwnProperty(this.fields[field]['name']) && this.entries[this.fields[field]['name']].length > 0)
                }
            }
            
            return result
        },
        async addUser(){ 
            console.log(this.entries)
            if(!this.check_mandatory()){
                this.info_msg = true
                return
            }
            this.$http.post('/customer/register/', this.entries)
            .then(response => {
                this.added = true;
            })
            .catch(error => {
                
                if (error.response.status_code == 409){
                    this.info_msg = true
                    this.header_msg = 'Duplicate customer added'
                    for (let key in error.response.data){
                        this.info_value += key + ': ' + error.response.data[key][0] + '; '
                    }
                }
                else if(error.response.status_code = 400) {
                    this.info_msg = true
                    this.header_msg = 'Field is missing'
                    for (let key in error.response.data){
                        this.info_value += key + ': ' + error.response.data[key][0] + '; '
                    }
                }
                else {
                    this.failed = true;
                    console.error("Error while adding User", error.response);
                }
            });  
        },
        async logout(){
          this.$http.post('/logout/',{
            refresh_token: localStorage.getItem('refresh_token'),
            })
            .then(response => {
                localStorage.clear();
                sessionStorage.clear();
                this.$router.push('/quantaco/login')
            })
            .catch(error => {
                console.log(error.response.data);
            });
        },
        closePopUp(){
            this.added=false;
            this.failed=false;
            this.info_msg = false;
            this.info_value = '';
            this.header_msg = '';
        },
    },
    
}

</script>
<template>
<div id="main_wrap">
    <div id="top_wrap" class="relative flex-none h-[15.375rem] w-full bg-cover bg-center" :style="{ backgroundImage: 'url(' + banner_img + ')', paddingLeft: '6.125rem', paddingRight: '3.125rem' }">
        
        <div class="grid grid-rows-2 grid-cols-2 h-[50%]" style="margin-top:-3%">
            <div class="relative w-full col-span-2">
                <div>
                    <p class="text-4xl leading-10 text-[#FFFFFF]">
                         Add New Customer
                    </p>
                </div>
            </div>
        </div>
        <div class="absolute top-5 right-10 flex items-center cursor-pointer" @click="logout">
            <span class="text-white mr-2 text-sm">Logout</span>
            <img :src="baseImgUrl+'/icon/logout.png'" class="mt-1" />
        </div>

    </div>
    <div id="bottom_wrap" class="flex ml-4 pl-20 pt-3">
        <div class="flex justify-center bottom_tab w-[95%] pt-5 shadow-md bg-[#FFFFFF] hover:shadow-lg z-10 mt-[-10rem]">
            <div id="myTabContent" class="w-full bg-gray-50 dark:bg-gray-800">
                <div class="w-full">
                    <form class="bg-grey-lighter flex flex-row" autocomplete="off">
                        <div class="bg-white px-6 py-8 shadow-md text-black w-full">
                            <div class="step-container">
                                <div class="grid grid-cols-1">
                                    <div v-for="(field, index) in fields" class="w-full" :key="index">
                                        <div class="pr-6">
                                            <div class="flex">
                                                <p>{{ field.fieldName + " "}}<span v-if="field.mandatory" class="text-red-500">*</span></p>
                                            </div>
                                            <div class="flex">
                                                <input :type="(field.fieldType =='password' && showPass)? 'text' : field.fieldType" class="block border border-grey-light w-full p-3 rounded mb-2" :name="field.fieldName" :placeholder="field.fieldName" v-model="entries[field.name]"/>
                                                <img v-if="field.fieldName =='Password'" :src="Show" @click="showPass = !showPass" style="margin-left: -6%; margin-top:3%; z-index:9; width: 17px; height: 17px; cursor: pointer;" alt="">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <div class="flex justify-between mt-3">
        <button @click="addUser" type="button" class="bg-[#0099D2] hover:bg-[blue] text-white font-sm py-2 px-4 rounded transform transition-transform duration-300 hover:scale-110 mr-[4.7%] ml-auto">
            Submit
        </button>
    </div>
    <info v-if="info_msg" @closePopUp="closePopUp">
        <template v-slot:message>
            <h3 class=" text-lg font-normal text-gray-500 dark:text-gray-400">{{ header_msg }}</h3>
            <p class="mb-5">{{ info_value }}</p>
        </template>
    </info>
    <success v-if="added" @closePopUp="closePopUp" />
    <failure v-if="failed" @closePopUp="closePopUp" />
</div>
</template>

<style scoped>
.slide-fade-enter-active {
      transition: all 0.5s ease-out;
    }

.slide-fade-enter-from,
.slide-fade-leave-to {
      transform: translateX(20px);
      opacity: 0;
    }
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  transition: opacity 0.3s ease;
}
.modal-container {
  max-width: 100%;
  width: auto;
  max-height: 100%;
  overflow-y: auto;
  margin: auto;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.4s ease;
}
#myTabContent{
    transition: all 0.5s ease;
  }
#main_wrap{
        height: 100%;
        width:100%;
    }
#top_wrap{
        display: flex;
        padding-top: 5%;
        padding-left: 8%;
        padding-bottom: 0%;
    }
  .rounded {
    border-radius: 5px;
  }

  input {
    padding-bottom: 0.50rem;
    margin-bottom: 0.9rem;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  select {
    border: 1px solid #ccc;
  }
  
  .flex {
    display: flex;
  }

  .text-grey-dark {
    color: #555;
  }

</style>

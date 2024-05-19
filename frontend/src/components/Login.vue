<script>
import { useRouter } from 'vue-router'
export default{
    
    props: {
        LoginImages: {
            type: Object,
            default:{
            }
        }
    },
    data(){
        return {
            userName: '',
            wrongCred: false,
            emptyCred: false,
            imgLogin: this.baseImgUrl+'/img/SideBanner.jpg',
            Show: this.baseImgUrl+'/icon/show.png',
            showPass: false,
        }
    },
    methods: {
        async handleLogin() {
          
            console.log("baseurl",this.BaseURL)
            this.$http.post('/user/token/access',{
                username: this.username,
                password: this.password
            })
                .then(response => {
                    console.log(response.data.detail);
                    localStorage.setItem('username', this.username);
                    localStorage.setItem('access_token', response.data.access);
                    localStorage.setItem('refresh_token', response.data.refresh);
                    this.$router.push('/quantaco/register')
                })
                .catch(error => {
                    console.error(error)
                    if(this.username=="" || this.password == ""){
                        this.emptyCred = true;
                    }
                    else{
                        this.wrongCred = true;
                    }
                        
                    console.log(error.response.data);
                });
        
        }
    },
    mounted() {
    if (!document.body.style.paddingLeft) {
        document.body.style.paddingLeft = '0px'
    }
    }
}
</script>

<template>
  <div class="main-login">
    <div id="leftImg">
      <img :src="imgLogin" alt="" class="imgMain">
    </div>
    <div id="FormLogin">
      <div id="LoginData">
        <div class="ProductLogo">
          <p class="secondary-font-color text-3xl leading-10 text-[#0099D2]" style="font-weight: 400;">
            Welcome back
          </p>
          <p class="text-sm secondary-font-color text-[white] mb-[4vh]">
            Log in with your account details below.
          </p>
          <p :class="!wrongCred? 'hidden':''" class="text-[red] text-sm">Username/Password is wrong</p>
                    <p :class="!emptyCred? 'hidden':''" class="text-[red] text-sm">Username/Password cannot be empty</p>
        </div>
        <div class="FormInput">
            <div class="elem ">
                <label for="">Username</label><br>
                <input type="text" v-model="username" placeholder="" class="box" style="padding-left: 2%">
            </div>
            <div class="elem box">
                <label for="">Password</label><br>
                <div class="flex">
                    <input :type="showPass? 'text':'password'" v-model="password" placeholder="" class="box" style="padding-left: 2%; display: inline;">
                    <img :src="Show" @click="showPass = !showPass" style="margin-left: -5%; margin-top:4%; z-index:9; width: 15px; height: 15px; cursor: pointer;" alt="">
                </div>
                
            </div>
        
            <br>
            <div class="Buttons">
                <div class="elem">
                    
                    <button type="submit" placeholder="Log-In" class="butt" @click="handleLogin">
                        Log-In
                    </button>
                </div>
                <div class="elem">
                    <!-- <span class="ForgotPass">Forgot Password</span> -->
                </div>
            </div>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');
* {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      /* font-family: 'Be Vietnam Pro'; */

    }
    body {
      transition: all 0.5s ease;
    }
.imgMain{
    width: 100%;
    height: 100%;
    object-fit: fill;

}

.h1{
    font-family: 'Playfair Display', serif;
    color: rgb(250, 247, 247);
    font-size: 4rem;
}

.imgHead{
    width: 12rem;
    margin: 0 !important;
    padding-bottom: 30px;
}

.main-login{
    display: flex;
    align-items: stretch;
    background: #28282B;
    /* background: linear-gradient(277.09deg, #313545 15.4%, #121118 100.07%); */
    /* background: rgb(44, 43, 43); */
    height: 100%;
    width: 100%;
    position: absolute;
}
#leftImg{
    width: 50%;
    height: 100%;
}
#FormLogin{
    /* width:100%; */
    height: 100%;
    flex-grow: 1;
    align-items: stretch;
}
/* html,body { height:100%; } */

#LoginData{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
}

input{
    margin-top: 2%;
}

.elem {
    margin: 1rem;
    /* margin-left: 3rem; */
}

label{
    font-size: 14px;
    color: white;
}
.opts{
    color: black;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  margin-left: 1rem;
  top: 2px;
  font-size: 12px;
  position: absolute;

  /* opacity: 0.5; */
}
/* input:text{
  left-margin: 10px;
} */
.box{
    /* box-sizing: border-box; */
    position: relative;
    border: none;
    /* -webkit-appearance: none; */
    -ms-appearance: none;
    -moz-appearance: none;
    /* appearance: none; */
    /* background: #f2f2f2; */
    /* padding: 12px; */
    /* border-radius: 3px; */
    width: 28rem;
    height: 2.1rem;
    font-size: 14px;
    border-radius: 1px;
    
}

::placeholder {
  position: absolute;
  /* left: 12px;
  bottom: 50%;
  top: 22px; */
  /* transform: translateY(-50%); */
  /* width: calc(100% - 24px); */
  color: #878282;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  margin-left: 10px;
  top: 2px;
  opacity: 0.5;
  left: 2px;

}

.butt{
    width: 28rem;
    height: 2.1rem;
    font-size: 14px;
    background-color: #0099D2;
    /* background-color: #b3b3b3; */
    cursor: pointer;
    border: #000000;
    border-radius: 2px;
    color: white;
    /* box-shadow: rgb(255, 255, 255) 0px 20px 30px -10px; */

}
.ForgotPass{
    color: white;
    text-decoration: underline;
    font-size: 10px;
    text-align: center;
}
.butt:hover{
    box-shadow: rgba(0, 0, 0, 0.25) 0px 25px 50px -12px;   
}

.FormInput{
    padding-top: 2%;
}

.Buttons{
    /* padding-left: 13%; */
    text-align: center;
}
.logo{
    width: 100%;
    padding-top: 5%;
    display: flex;
    justify-content: space-evenly;
}

.ProductLogo{
    margin-top: 10%;
    margin-left: -29.5%;
}
</style>

<template>
    <div :class="['login', className]">
      <div class="overlap">
        <div class="BG">
          <div class="overlap-group">
            <div class="ellipse" />
            <div class="div" />
          </div>
          <img class="vector" alt="Vector" src="image.svg" />
        </div>
        <div class="login-btn">
          <div class="overlap-2">
            <div class="student">STUDENT</div>
            <div class="instructor">INSTRUCTOR</div>
            <div class="admin">ADMIN</div>
          </div>
          <div class="login-as">LOGIN AS:</div>
        </div>
        <div class="form">
          <div class="username">
            <div class="overlap-group-2">
              <div class="text-wrapper">USERNAME...</div>
              <img class="img" alt="User" src="user.svg" />
            </div>
          </div>
          <div class="password">
            <div class="overlap-group-2">
              <div class="text-wrapper">PASSWORD...</div>
              <img class="img" alt="Lock" src="lock.svg" />
            </div>
          </div>
          <div class="frame">
            <div class="text-wrapper-2">Forgot password?</div>
          </div>
        </div>
        <img class="vector-2" alt="Vector" src="vector.svg" />
      </div>
    </div>
  </template>
  
  <script>
  //???
  export default {
    name: "Login",
    props: {
      property1: {
        type: String,
        default: "default",
        validator: function (value) {
          return ["default"].indexOf(value) !== -1;
        },
      },
      className: {
        type: String,
        default: "",
      },
    },
  };
  </script>
  
  <style>
  .login {
    background-color: #c02121;
    height: 720px;
    overflow: hidden;
    width: 1280px;
  }
  
  .login .overlap {
    height: 1083px;
    left: -362px;
    position: relative;
    top: -1px;
    width: 1642px;
  }
  
  .login .BG {
    height: 1083px;
    left: 0;
    position: absolute;
    top: 0;
    width: 1642px;
  }
  
  .login .overlap-group {
    background-color: #fa4242;
    border-radius: 362px;
    height: 724px;
    left: 0;
    position: absolute;
    top: 359px;
    width: 724px;
  }
  
  .login .ellipse {
    background-color: #b82626;
    border-radius: 286px;
    height: 572px;
    left: 76px;
    position: absolute;
    top: 76px;
    width: 572px;
  }
  
  .login .div {
    background-color: #c72727;
    border-radius: 219px;
    height: 438px;
    left: 143px;
    position: absolute;
    top: 143px;
    width: 438px;
  }
  
  .login .vector {
    height: 720px;
    left: 778px;
    position: absolute;
    top: 1px;
    width: 864px;
  }
  
  .login .login-btn {
    height: 80px;
    left: 807px;
    position: absolute;
    top: 463px;
    width: 353px;
  }
  
  .login .overlap-2 {
    background-color: #ffffff;
    border-radius: 4px;
    box-shadow: 0px 4px 4px #0000004c;
    height: 50px;
    left: 45px;
    position: absolute;
    top: 30px;
    width: 300px;
  }
  
  .login .student {
    color: #cb2a2a;
    font-family: "Montserrat-SemiBold", Helvetica;
    font-size: 12px;
    font-weight: 600;
    left: 12px;
    letter-spacing: 0;
    line-height: 20px;
    position: absolute;
    text-align: center;
    text-decoration: underline;
    top: 18px;
    white-space: nowrap;
    width: 62px;
  }
  
  .login .instructor {
    color: #cb2a2a;
    font-family: "Montserrat-SemiBold", Helvetica;
    font-size: 12px;
    font-weight: 600;
    left: 116px;
    letter-spacing: 0;
    line-height: 20px;
    position: absolute;
    text-align: center;
    text-decoration: underline;
    top: 18px;
    white-space: nowrap;
    width: 84px;
  }
  
  .login .admin {
    color: #cb2a2a;
    font-family: "Montserrat-SemiBold", Helvetica;
    font-size: 12px;
    font-weight: 600;
    left: 233px;
    letter-spacing: 0;
    line-height: 20px;
    position: absolute;
    text-align: center;
    text-decoration: underline;
    top: 18px;
    white-space: nowrap;
    width: 46px;
  }
  
  .login .login-as {
    color: #ffffff;
    font-family: "Montserrat-SemiBold", Helvetica;
    font-size: 12px;
    font-weight: 600;
    left: 0;
    letter-spacing: 0;
    line-height: 20px;
    position: absolute;
    text-align: center;
    top: 0;
    width: 176px;
  }
  
  .login .form {
    height: 262px;
    left: 852px;
    position: absolute;
    top: 335px;
    width: 300px;
  }
  
  .login .username {
    height: 45px;
    left: 0;
    position: absolute;
    top: 0;
    width: 302px;
  }
  
  .login .overlap-group-2 {
    border: 1px solid;
    border-color: #ffffff;
    border-radius: 4px;
    height: 45px;
    position: relative;
    width: 300px;
  }
  
  .login .text-wrapper {
    color: #ffffff;
    font-family: "Montserrat-Light", Helvetica;
    font-size: 14px;
    font-weight: 300;
    left: 46px;
    letter-spacing: 0;
    line-height: 20px;
    position: absolute;
    text-align: center;
    top: 12px;
    white-space: nowrap;
  }
  
  .login .img {
    height: 20px;
    left: 11px;
    position: absolute;
    top: 12px;
    width: 20px;
  }
  
  .login .password {
    height: 45px;
    left: 0;
    position: absolute;
    top: 65px;
    width: 302px;
  }
  
  .login .frame {
    height: 20px;
    left: 154px;
    position: absolute;
    top: 242px;
    width: 146px;
  }
  
  .login .text-wrapper-2 {
    color: #ffffff;
    font-family: "Montserrat-Medium", Helvetica;
    font-size: 16px;
    font-weight: 500;
    left: 0;
    letter-spacing: 0;
    line-height: normal;
    position: absolute;
    text-align: center;
    text-decoration: underline;
    top: -1px;
  }
  
  .login .vector-2 {
    height: 166px;
    left: 930px;
    position: absolute;
    top: 149px;
    width: 139px;
  }
  </style>
  
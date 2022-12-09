// 登錄
var login=document.getElementById("login");
var bg=document.getElementById("bg");
var dig=document.getElementById("dig");
var close=document.getElementById("close");
var ok=document.getElementById("ok");
var register=document.getElementById("register")

// 綁定刪除按鈕的單擊事件
login.onclick=function(){
    //顯示背景元素和彈框元素
    bg.style.display="block";
    dig.style.display="block";
}
// 綁定確定按鈕的單擊事件
ok.onclick=function(){
    //隱藏背景元素
    bg.style.display="none";
    //隱藏對話框元素
    dig.style.display="none";
}
close.onclick=function(){
    //隱藏背景元素
    bg.style.display="none";
    //隱藏對話框元素
    dig.style.display="none";
}
login.onmouseover=function(){
        login.style.color="#f00";
        }
login.onmouseout=function(){
        login.style.color="#000";
        }

// 注冊
register.onclick=function(){
        window.location.href="./templates/register.html"
        }
register.onmouseover=function(){
        register.style.color="#f00";
        }
register.onmouseout=function(){
        register.style.color="#000";
        }
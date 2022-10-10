function execfun(){
var pos=editor.getCursor();
var code=editor.getLine(pos.line);
window.eval(code);
}

function blankline(){
    editor.setValue(editor.getValue().replaceAll(/\n\s+\n/ig,'\n').replaceAll('\n\n','\n'));
}

function password(pasLen){
var pasArr = [];
var password = '';
//abc
for (var i = 97; i <=122; i++) {
    pasArr.push(String.fromCharCode(i))
}
//ABC
for (var i = 65; i <=90; i++) {
    pasArr.push(String.fromCharCode(i))
}
//123
for (var i = 48; i <=57; i++) {
    pasArr.push(String.fromCharCode(i))
}
//!#%
for (var i = 33; i <=47; i++) {
    pasArr.push(String.fromCharCode(i))
}
var pasArrLen = pasArr.length;
for (var i=0; i<pasLen; i++){
var x = Math.floor(Math.random()*pasArrLen);
password += pasArr[x];
}
session.insert(session.getLength(),password);
session.setValue(session.getValue());
session.selection.setSelectionRange(new Range(0,0,1,0));
}

function uuid() {
 function s4() {
 return (((1+Math.random())*0x10000)|0).toString(16).substring(1);
 }
 session.insert(session.getLength(),(s4()+s4()+"-"+s4()+"-"+s4()+"-"+s4()+"-"+s4()+s4()+s4()));
 session.setValue(session.getValue());
 session.selection.setSelectionRange(new Range(0,0,0,0));
}

function base64() {
var val=session.getValue();
val=val.substr(val.indexOf("\n")+1,val.length);
session.insert(session.getLength(),window.btoa(val));
session.setValue(session.getValue());
session.selection.setSelectionRange(new Range(0,0,0,0));
}
function $h(line){host(line);}
function host(line){
var arrline=line.split("|");
var privatekey = "";
if (arrline[5] != '')
    privatekey=encodeURIComponent(localStorage.getItem(arrline[5]));
var newtab=window.open("http://127.0.0.1:8888/?title="+arrline[0]+"&hostname="+arrline[1]+"&port="+arrline[2]+"&username="+arrline[3]+"&password="+encodeURIComponent(arrline[4])+"&privatekey="+privatekey+"&passphrase="+encodeURIComponent(arrline[6]));
return 'ok!';
}

function cmpd(m,n){
m=Number(m)
n=Number(n)
if (m < n) return -1
else if (m > n) return 1
else return 0
}
function cmpdr(m,n){
m=Number(m)
n=Number(n)
if (m < n) return 1
else if (m > n) return -1
else return 0
}
function cmpa(s, t){
 var a = s.toLowerCase();
 var b = t.toLowerCase();
 if (a < b) return -1;
 if (a > b) return 1;
 return 0;
}

function sort(){
var cursor = editor.getCursorPosition();
var line = editor.session.doc.getLine(cursor.row);
editor.removeLines();
var val = session.getValue();
var opt = line.split(":")[1];
if (opt == "h" || opt == ""){session.insert(session.getLength(),"sort:a|d|h\n");return true;}
if (opt == "a"){session.setValue(val.split("\n").sort(cmpa).join("\n"));return true;}
if (opt == "d"){session.setValue(val.split("\n").sort(cmpd).join("\n"));return true;}
if (opt == "dr"){session.setValue(val.split("\n").sort(cmpdr).join("\n"));return true;}
}

function rand(){
var cursor = editor.getCursorPosition();
var line = editor.session.doc.getLine(cursor.row);
editor.removeLines();
var val = session.getValue();
var opt = line.split(":")[1];
if (opt == "h" || opt == ""){session.insert(session.getLength(),"rand:99\n");return true;}
//if (opt == "a"){session.setValue(val.split("\n").sort(cmpa).join("\n"));return true;}
var arr = [];
for (var i=1,len=opt; i<=len; i++){arr.push(i);}
session.setValue(arr.join("\n"));
}

function ip(){

}

function mysql(){

}

function file(ops){
if(ops=="ls"){
$.get("/file","",function(data){editor.setValue(data);},"text");
}else{
$(document).attr("title",ops);
$.get("/file?filename="+ops,"",function(data,textStatus,jqxhr){
editor.doc.file_name=jqxhr.getResponseHeader("file_name");
editor.doc.file_path=jqxhr.getResponseHeader("file_path");
editor.setValue(data);
var date = new Date();
$("#doc-status").text(editor.doc.file_name+" "+date.getHours()+"-"+date.getMinutes()+"-"+date.getSeconds()+" opened ");
},"text");
}
}

function savefile(){
var filename=editor.doc.file_name;
var filepath=editor.doc.file_path;
var filedata=editor.doc.getValue();
var xhr = new XMLHttpRequest();
xhr.open("post", "/file", true);
xhr.setRequestHeader("Content-Type", "application/json");
var data = JSON.stringify({"file_name":filename,"file_data": filedata});
xhr.send(data);
var date = new Date();
$("#doc-status").text(filename+" "+date.getHours()+"-"+date.getMinutes()+"-"+date.getSeconds()+" saved ");
}

function mysql(url){
var code=editor.getValue();
console.log(code);
$.get("/mysql?sql="+url,"",function(data,textStatus,jqxhr){
editor.setValue(data);
},"text");
}

function pgsql(host, user, passwd, db, port){
var url="host, user, passwd, db, port"
}
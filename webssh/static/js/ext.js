function  blankline(){
    session.setValue(session.getValue().replaceAll(/\n\s+\n/ig,'\n').replaceAll('\n\n','\n'));
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

function host(){
var pos=editor.getCursor();
var line=editor.getLine(pos.line);
var line=line.substring(line.indexOf(":")+1,line.length);
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

function file(){
var pos=editor.getCursor();
var line=editor.getLine(pos.line);
var ops=line.substring(line.indexOf(":")+1,line.length);
if(ops=="ls"){
$.get("/file","",function(data){editor.setValue(data);},"text");
}else{
$(document).attr("title",ops);
$.get("/file?filename="+ops,"",function(data){editor.setValue(data);},"text");
}
}
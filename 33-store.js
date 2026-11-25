(function(){
var KEY="pivc_progress_v1";
function load(){try{return Object.assign({quiz:{},sim:[],puzzle:[],sa:[]},JSON.parse(localStorage.getItem(KEY)||"{}"));}catch(e){return {quiz:{},sim:[],puzzle:[],sa:[]};}}
function save(d){try{localStorage.setItem(KEY,JSON.stringify(d));}catch(e){}}
window.Store={
 get:load,
 quiz:function(mid,score,total){var d=load();var q=d.quiz[mid]||{best:0,attempts:0,total:total};q.best=Math.max(q.best,score);q.attempts++;q.total=total;q.last=Date.now();d.quiz[mid]=q;save(d);},
 add:function(kind,obj){var d=load();obj.ts=Date.now();d[kind].unshift(obj);d[kind]=d[kind].slice(0,50);save(d);},
 reset:function(){localStorage.removeItem(KEY);}
};})();
